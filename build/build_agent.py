"""
构建代理 - 用于自动构建 NapcatAPI 的 Pydantic 模型
"""
import asyncio
import os
import logging
from pathlib import Path
import re
from agents import Agent, OpenAIChatCompletionsModel, Runner
from openai import AsyncOpenAI
from dotenv import load_dotenv
from pydantic import BaseModel, Field

# 设置日志
logger = logging.getLogger(__name__)

load_dotenv()

BUILD_INSTRUCTIONS = """
你是NapcatAPI-pydanticV2模型的构建专家
你的任务是基于构建文档，生成符合pydanticV2的请求响应数据模型
或者修复机械生成的模型
基于python3.13
编码指南：
强制类型标注
禁止从typing模块导入被弃用的：Dict、List、Tuple、Set、Union、Optional，改用：dict、list、tuple、set、any、str、int、float等内置类型即可,Optional改为使用|None , Union改为使用|

重要：请返回一个JSON格式的输出，包含以下两个字段：
1. code: 包含生成的Python代码
2. log: 包含你的构建过程日志

输出示例:
{
  "code": "# 这里是Python代码...",
  "log": "构建日志内容..."
}
"""

class BuildResult(BaseModel):
    """
    构建结果类，包含构建的代码和日志
    """
    code: str = Field(..., description="生成的代码")
    log: str = Field(..., description="构建日志")



openai_client = AsyncOpenAI(
    api_key=os.getenv("API_KEY"),
    base_url=os.getenv("BASE_URL"),
)

builder = Agent(
    name="napcat-api-builder",
    instructions=BUILD_INSTRUCTIONS,
    output_type=BuildResult,
    model=OpenAIChatCompletionsModel(
        model=os.getenv("MODEL", "别用思维链的模型"),
        openai_client=openai_client,
    ),
)

root = Path(__file__).parent.parent

input_dir = root / "data" / "api_yaml_raw"

original_dir = root / "data" / "models" 

output_dir = root / "src" / "napcat" / "api" / "models" / "dev"

lock_file = root / "build" / "builder.lock"

# 确保锁文件存在
lock_file.touch(exist_ok=True)

lock = lock_file.read_text(encoding="utf-8").splitlines() if lock_file.exists() else []

def main():
    for model_file in original_dir.glob("*.py"):
        if model_file.name == "__init__.py" or model_file.name in lock:
            continue
        # 读取文件内容
        with open(model_file, "r", encoding="utf-8") as f:
            code = f.read()

        # 构建提示词
        prompt = f"{BUILD_INSTRUCTIONS}\n\n请修复以下代码：\n\n{code}"

        # 从api_yaml_raw目录读取完整的api定义
        # STEP-1 提取api_id
        # 正则表达式匹配api_id
        api_id = re.search(r'__id__ = "(.*?)"', code)
        if api_id:
            api_id = api_id.group(1)
        else:
            logger.error(f"未找到api_id: {model_file.name}")
            continue

        api_yaml_file = input_dir / f"{api_id}.yaml"
        if not api_yaml_file.exists():
            logger.error(f"未找到对应的yaml文件: {api_yaml_file}")
            continue
    
        # STEP-2补充提示词
        prompt += BUILD_INSTRUCTIONS
        prompt += f"\n\n以下为api定义：\n\n{api_yaml_file.read_text(encoding='utf-8')}"
        prompt += "修改点：检查并修复以下问题：\n"
        prompt += "1. 检查是否有多余的导入\n"
        prompt += "2. 确保所有字段都有类型标注\n"
        prompt += "3. 确保所有字段都有描述和初始值\n"
        prompt += "4. 将外部嵌套类移动到类里面，例如XxxRes类嵌套一个Data类作为Data字段的类型\n"
        prompt += "5. 响应类字段，status ok 使用Literal类型[\"ok\"] , 其他简单枚举也是直接使用Literal类型即可\n"

        prompt += "建议：使用Field写好默认值，以及描述，移除未使用的导入，遇到嵌套模型，请定义嵌套类。如果需要枚举，请定义枚举类，驼峰命名法\n\n"

        # 开始生成代码
        output = asyncio.run(Runner.run(
            builder,
            input=prompt,
        ))
        final_output = output.final_output

        logger.info(f"构建日志: {final_output.log}")
        with open(output_dir / model_file.name, "w", encoding="utf-8") as f:
            f.write(final_output.code)
        
        # 保存日志
        log_file = output_dir / f"{model_file.stem}_log.txt"
        with open(log_file, "w", encoding="utf-8") as f:
            f.write(final_output.log)
        
        logger.info(f"构建完成: {model_file.name}")
        # 更新锁文件，避免重复构建
        lock.append(model_file.name)
        lock_file.write_text("\n".join(lock), encoding="utf-8")


if __name__ == "__main__":
    main()