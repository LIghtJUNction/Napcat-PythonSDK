"""
构建代理 - 用于自动构建 NapcatAPI 的 Pydantic 模型
"""
import asyncio
import os
import logging
from pathlib import Path
from agents import Agent, OpenAIChatCompletionsModel, Runner
from openai import AsyncOpenAI
from dotenv import load_dotenv
from pydantic import BaseModel, Field

# 设置日志
logger = logging.getLogger(__name__)

load_dotenv()

BUILD_INSTRUCTIONS = """
你是NapcatAPI-pydanticV2模型的审核专家，你负责审核不合规范的api模型代码
并按照规则输出为符合规范的api模型代码
"""

class BuildResult(BaseModel):
    """
    构建结果类，包含构建的代码和日志
    """
    code: str = Field(..., description="新的代码内容")
    log: str = Field(..., description="审核日志")



openai_client = AsyncOpenAI(
    api_key=os.getenv("API_KEY"),
    base_url=os.getenv("BASE_URL"),
)

auditor = Agent(
    name="napcat-api-auditor",
    instructions=BUILD_INSTRUCTIONS,
    output_type=BuildResult,
    model=OpenAIChatCompletionsModel(
        model=os.getenv("MODEL", "最好不要使用带思维链的模型"),
        openai_client=openai_client,
    ),
)

root = Path(__file__).parent.parent

input_dir = root / "src" / "napcat" / "api" / "models" / "dev"

output_dir = root / "src" / "napcat" / "api" / "models" 

lock_file = root / "build" / "auditor.lock"

# 确保锁文件存在
lock_file.touch(exist_ok=True)

lock = lock_file.read_text(encoding="utf-8").splitlines() if lock_file.exists() else []

def main():
    for model_file in input_dir.glob("*.py"):
        if model_file.name == "__init__.py" or model_file.name in lock:
            continue
        # 读取文件内容
        with open(model_file, "r", encoding="utf-8") as f:
            code = f.read()

        # 构建提示词
        prompt = f"{BUILD_INSTRUCTIONS}\n\n请审核以下代码：\n\n{code}"



        # 补充提示词
        prompt += "关注点：检查并修复以下问题：\n"
        prompt += "1. 检查是否有多余的导入\n"
        prompt += "2. 如果有status字段，统一写法为：status: Literal[\"ok\"] = Field(\"ok\", description=\"状态码，固定为 'ok'\")\n"
        prompt += """3.
        嵌套类标准写法如下：
        class OuterClass(BaseModel):
            class InnerClass(BaseModel):
                field: str = Field(..., description="字段描述")
            ...      
        """
        prompt += "4. 检查是否有语法错误\n"
        prompt += "检查字段默认值,类名是否为驼峰命名法\n\n"

        # 开始生成代码
        output = asyncio.run(Runner.run(
            auditor,
            input=prompt,
        ))
        final_output = output.final_output

        logger.info(f"审核日志: {final_output.log}")
        with open(output_dir / model_file.name, "w", encoding="utf-8") as f:
            f.write(final_output.code)
        
        # 保存日志
        log_file = output_dir / f"{model_file.stem}_audit_log.txt"
        with open(log_file, "w", encoding="utf-8") as f:
            f.write(final_output.log)
        
        logger.info(f"审核完成: {model_file.name}")
        # 更新锁文件，避免重复构建
        lock.append(model_file.name)
        lock_file.write_text("\n".join(lock), encoding="utf-8")








if __name__ == "__main__":
    main()