"""
API构建模块

提供CLI工具用于构建API的Pydantic模型，更新API元数据等功能
"""
import datetime
import json
import logging
import sys
from pathlib import Path
import click
import toml

# 使用绝对导入
from build.utils import get_api_json_files, get_template, replace_var, save_to_model_file, replace_region
from build.pydantic_generator import generate_pydantic_models

# 设置项目根目录
root = Path(__file__).parent.parent

# 设置日志
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger(__name__)

api_json_path = root / "data" / "api_json"
base_url = "https://napcat.apifox.cn/"

# 尝试读取版本号
try:
    version = toml.load(root / "pyproject.toml")["project"]["version"]
    logger.debug(f"读取到版本号: {version}")
except Exception as e:
    version = "0.1.0"
    logger.warning(f"未能读取版本号，使用默认值: {version}, 错误: {e}")


@click.group(invoke_without_command=True)
@click.pass_context
def cli(ctx: click.Context) -> None:
    """构建API pydanticV2模型。"""
    logger.debug(f"启动CLI工具，Python版本: {sys.version}")
    
    # 如果没有指定子命令，显示帮助
    if ctx.invoked_subcommand is None:
        logger.debug("未指定子命令，显示帮助")
        click.echo(ctx.get_help())


@cli.command(name="update")
def update_metadata() -> None:
    """更新API元数据。"""
    files = get_api_json_files()
    api2id: dict[str, str] = {}
    if not files:
        logger.warning("没有找到 API JSON 文件")
        click.echo("没有找到 API JSON 文件")
        return
    
    logger.info(f"开始更新元数据，共找到 {len(files)} 个API文件")
    
    for file in files:
        endpoint_id: str = file.stem 
        
        # 初始化新的元数据字典
        new_metadata: dict[str, str] = {}
        new_metadata["api_id"] = endpoint_id
        
        # 设置元数据文件路径
        meta_path = root / "data" / "api_meta" / f"{endpoint_id}.py"
        
        # 检查元数据文件是否存在，如果存在则读取
        existing_metadata: dict[str, str] = {}
        if meta_path.exists():
            logger.debug(f"找到现有元数据文件: {meta_path}")
            try:
                existing_metadata = json.load(meta_path.open("r", encoding="utf-8"))
                logger.info(f"成功读取现有元数据: {endpoint_id}")
            except json.JSONDecodeError:
                logger.warning(f"元数据文件格式错误，将创建新文件: {endpoint_id}")
        
        # 从API JSON加载新数据
        data = json.load(file.open(encoding="utf-8"))
        
        # 设置或更新必要的元数据
        new_metadata["version"] = version
        # 总是更新最后更新时间
        new_metadata["last_update"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        for endpoint, endpoint_data in data["paths"].items():
            # 删除开头的斜杠
            endpoint_clean = endpoint[1:] if endpoint.startswith("/") else endpoint
            
            new_metadata["endpoint"] = endpoint_clean  # 已确保不包含开头的 /
            new_metadata["homepage"] = base_url + endpoint_id
            new_metadata["llms.txt"] = base_url + endpoint_id + ".md"

            try:
                method_data = endpoint_data["post"]
                new_metadata["method"] = "POST"
            except KeyError:
                method_data = endpoint_data["get"]
                new_metadata["method"] = "GET"
            
            # 更新描述信息
            new_metadata["description"] = method_data.get("description", "") + "\n\nsummary:" + method_data.get("summary", "")

            # 构建EndpointReq和EndPointRes EndPointAPI 名称
            # 使用清理过的endpoint（不包含前导斜杠）
            EndPoint = endpoint_clean.split("_")
            # 如果第一个符号是.或者_ , 则去掉
            if EndPoint and EndPoint[0] in [".", "_"] or EndPoint[0].startswith('.'):
                EndPoint[0] = EndPoint[0].lstrip('._')
            
            # 确保生成的名称不包含前导斜杠或点号
            EndPointReq = "".join([i.capitalize() for i in EndPoint if i]) + "Req"
            new_metadata["EndPointReq"] = EndPointReq
            
            EndPointRes = "".join([i.capitalize() for i in EndPoint if i]) + "Res"
            new_metadata["EndPointRes"] = EndPointRes
            
            EndPointAPI = "".join([i.capitalize() for i in EndPoint if i]) + "API"
            new_metadata["EndPointAPI"] = EndPointAPI
            
            logger.debug(f"生成了API名称: {EndPointAPI}")

        # 合并元数据：优先保留现有数据，但新数据会更新last_update
        merged_metadata = {**existing_metadata, **new_metadata}
        
        # 确保更新last_update字段
        merged_metadata["last_update"] = new_metadata["last_update"]
        
        logger.debug(f"准备保存元数据: {endpoint_id}, 字段数: {len(merged_metadata)}")
        
        # 保存合并后的元数据
        meta_path.parent.mkdir(parents=True, exist_ok=True)  # 确保目录存在
        meta_path.touch(exist_ok=True)
        json.dump(merged_metadata, meta_path.open("w", encoding="utf-8"), indent=4, ensure_ascii=False)
        logger.info(f"更新了 {endpoint_id} 的元数据")
        click.echo(f"更新了 {endpoint_id} 的元数据")

        api_template = get_template()
        
        # 开始更新文件
        model_content = replace_var(
            api_template,
            merged_metadata
        )

        api2id[merged_metadata["EndPointAPI"].lower()] = merged_metadata["api_id"]

        api2id_json_path = root / "data" / "api2id.json"
        api2id_json_path.parent.mkdir(parents=True, exist_ok=True)
        api2id_json_path.touch(exist_ok=True)
        with api2id_json_path.open("w", encoding="utf-8") as f:
            json.dump(api2id, f, indent=4, ensure_ascii=False)
            logger.info(f"更新了 {api2id_json_path} 文件")

        # 写回文件
        save_to_model_file(
            merged_metadata["EndPointAPI"].lower(),
            model_content
        )

        click.echo(f"更新了 {merged_metadata['EndPointAPI'].lower()} 模型文件")


@cli.command(name="generate")
@click.option("--all", is_flag=True, help="生成所有API的Pydantic模型")
@click.option("--id", help="指定API ID生成单个Pydantic模型")
def generate_models(all: bool, id: str | None = None) -> None:
    """生成API的Pydantic模型。"""
    files = []
    
    if all:
        files = get_api_json_files()
        logger.info(f"将为所有API生成Pydantic模型，共{len(files)}个")
    elif id:
        api_file = root / "data" / "api_json" / f"{id}.json"
        if api_file.exists():
            files = [api_file]
            logger.info(f"将为API ID {id} 生成Pydantic模型")
        else:
            logger.error(f"未找到API ID {id} 对应的JSON文件")
            click.echo(f"未找到API ID {id} 对应的JSON文件")
            return
    else:
        logger.error("请使用 --all 或 --id 选项指定要生成的API")
        click.echo("请使用 --all 或 --id 选项指定要生成的API")
        return
    
    total = len(files)
    success = 0
    
    for i, file in enumerate(files):
        endpoint_id: str = file.stem
        logger.info(f"正在处理 [{i+1}/{total}] API ID: {endpoint_id}")
        
        try:
            # 读取API JSON数据
            with open(file, "r", encoding="utf-8") as f:
                api_data = json.load(f)
            
            # 读取元数据
            meta_path = root / "data" / "api_meta" / f"{endpoint_id}.py"
            if not meta_path.exists():
                logger.warning(f"未找到元数据文件: {endpoint_id}，先运行update命令生成元数据")
                click.echo(f"未找到元数据文件: {endpoint_id}，先运行update命令生成元数据")
                continue
            
            try:
                with open(meta_path, "r", encoding="utf-8") as f:
                    metadata = json.load(f)
            except json.JSONDecodeError:
                logger.error(f"元数据文件格式错误: {endpoint_id}")
                click.echo(f"元数据文件格式错误: {endpoint_id}")
                continue
            
            # 获取API名称相关信息
            endpoint_clean = metadata.get("endpoint", "")
            api_name = metadata.get("EndPointAPI", "")
            req_name = metadata.get("EndPointReq", "")
            res_name = metadata.get("EndPointRes", "")
            
            if not api_name or not endpoint_clean:
                logger.warning(f"元数据中缺少必要信息: {endpoint_id}")
                click.echo(f"元数据中缺少必要信息: {endpoint_id}")
                continue
            
            # 处理API名称，确保符合Python命名规范
            clean_api_name = api_name.lstrip('/').lstrip('.').lstrip('_').lower()
            
            # 获取模型文件路径
            models_dir = root / "data" / "models"
            models_dir.mkdir(parents=True, exist_ok=True)
            model_file = models_dir / f"{clean_api_name}.py"
            
            # 如果模型文件不存在，先创建基本结构
            if not model_file.exists():
                logger.info(f"创建新的模型文件: {clean_api_name}.py")
                api_template = get_template()
                basic_model = replace_var(api_template, metadata)
                with open(model_file, "w", encoding="utf-8") as f:
                    f.write(basic_model)
            
            # 读取现有模型文件内容
            with open(model_file, "r", encoding="utf-8") as f:
                model_content = f.read()
            
            # 生成Pydantic模型
            logger.debug(f"开始为 {endpoint_id} 生成Pydantic模型")
            model_parts = generate_pydantic_models(api_data)
            
            # 更新导入语句 - 处理重复导入问题
            imports_set = model_parts.imports.copy()
            
            # 标准化导入，确保pydantic导入格式一致
            standard_imports = {
                "import logging",
                "from typing import Any",
                "from pydantic import BaseModel, Field"
            }
            
            # 移除可能的部分导入，以便替换为标准化导入
            imports_to_remove = []
            for imp in imports_set:
                if "pydantic import BaseModel" in imp and "Field" not in imp:
                    imports_to_remove.append(imp)
                if "typing import " in imp and "Any" in imp and not imp.startswith("from typing import Any"):
                    imports_to_remove.append(imp)
                    
            for imp in imports_to_remove:
                imports_set.discard(imp)
            
            # 添加标准化导入
            imports_set.update(standard_imports)
            
            # 以排序方式输出导入语句
            imports_code = "\n".join(sorted(imports_set)) + "\n\n" + "logger = logging.getLogger(__name__)"
            
            logger.debug(f"处理导入语句，最终导入数量: {len(imports_set)}")
            
            # 替换模板变量
            req_code = model_parts.req.replace("{{EndPointReq}}", req_name)
            res_code = model_parts.res.replace("{{EndPointRes}}", res_name)
            api_code = model_parts.api.replace("{{EndPointReq}}", req_name).replace("{{EndPointRes}}", res_name).replace("{{EndPointAPI}}", api_name)
            
            # 处理组件模型
            component_models_code = ""
            if model_parts.component_models:
                # 将所有组件模型合并为一个字符串
                component_models_code = "\n\n".join(model_parts.component_models)
                logger.debug(f"生成了 {len(model_parts.component_models)} 个组件模型")
            
            # 组装最终代码 - 修复区域标记格式
            final_code = f"\n{imports_code}\n\n"
            
            # 添加组件模型代码（如果有）
            if component_models_code:
                final_code += f"# region component_models\n{component_models_code}\n# region component_models/\n\n"
            
            # 添加请求模型、响应模型和API模型代码 - 使用与模板一致的区域标记
            final_code += f"# region req\n{req_code}\n# region req/\n\n\n# region res\n{res_code}\n# region res/\n\n# region api\n{api_code}\n\n# region api/"
            
            # 更新模型内容
            updated_content = replace_region(model_content, "code", final_code)
            
            # 保存更新后的模型文件
            with open(model_file, "w", encoding="utf-8") as f:
                f.write(updated_content)
            
            logger.info(f"成功生成并保存 {clean_api_name} 的Pydantic模型，包含 {len(model_parts.component_models)} 个组件模型")
            click.echo(f"成功生成并保存 {clean_api_name} 的Pydantic模型")
            success += 1
            
        except Exception as e:
            logger.exception(f"处理 {endpoint_id} 时发生错误: {e}")
            click.echo(f"处理 {endpoint_id} 时发生错误: {e}")
    
    logger.info(f"Pydantic模型生成完成: 成功 {success}/{total}")
    click.echo(f"Pydantic模型生成完成: 成功 {success}/{total}")


@cli.command(name="build")
@click.pass_context
def build(ctx: click.Context) -> None:
    """完整构建所有API的Pydantic模型。"""
    logger.info("开始执行完整构建流程...")
    
    try:
        # 第1步：更新元数据
        logger.info("步骤1：更新所有API元数据")
        click.echo("步骤1：更新所有API元数据")
        ctx.invoke(update_metadata)
        
        # 第2步：生成所有模型
        logger.info("步骤2：生成所有API的Pydantic模型")
        click.echo("步骤2：生成所有API的Pydantic模型")
        ctx.invoke(generate_models, all=True, id=None)
        
        logger.info("构建完成！")
        click.echo("构建完成！")
    except Exception as e:
        logger.error(f"构建过程中出现错误: {e}")
        logger.exception("错误详情:")
        click.echo(f"构建失败: {e}", err=True)
        return


@cli.command()
@click.argument("name")
def agent(name: str) -> None:
    """
    选择调用哪个agent工作流
    
    Args:
        name: Agent名称 (可选值: build, audit, docs)
    """
    match name:
        case "build":
            click.echo("开始运行 Builder Agent")
            from .build_agent import main as build_agent
            build_agent()
        case "audit":
            click.echo("开始运行 Auditor Agent")
            from .audit_agent import main as audit_agent
            audit_agent()

        case "docs":
            click.echo("开始运行 Docs Agent")
            from .docs_agent import main as docs_agent
            docs_agent()

        case _:
            click.echo("未知的Agent名称，请选择: build, audit, docs")

        
    


# 直接执行脚本时的入口点
if __name__ == "__main__":
    cli()





