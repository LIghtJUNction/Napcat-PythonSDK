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
import json

# 设置日志
logger = logging.getLogger(__name__)

load_dotenv()

BUILD_INSTRUCTIONS = """
你是NapcatAPI文档编写专家，你负责给API写详细的使用和说明文档

"""

class BuildResult(BaseModel):
    """
    构建结果类，包含构建的代码和日志
    """
    md: str = Field(..., description="md格式的API文档内容")
    log: str = Field(..., description="编辑日志")



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

api_docs_base_url = "https://github.com/LIghtJUNction/Napcat-PythonSDK/tree/main/docs/napcat/api/"

root = Path(__file__).parent.parent

input_dir = root / "data" / "api_json" 

output_dir = root / "docs" / "napcat" / "api"

lock_file = root / "build" / "docs.lock"

# 确保锁文件存在
lock_file.touch(exist_ok=True)

lock = lock_file.read_text(encoding="utf-8").splitlines() if lock_file.exists() else []



def main():

    if not output_dir.exists():
        output_dir.mkdir(parents=True, exist_ok=True)

    README = output_dir / "README.MD"

    if not README.exists():
        README.touch()
        logger.info(f"创建README文件: {README}")


    # INIT README.MD文件
    with open(README, "w", encoding="utf-8") as f:
        f.write("# NapcatAPI文档\n\n")
        f.write("## API列表\n\n")

    for model_file in input_dir.glob("*.json"):

        if model_file.name in lock:
            continue

        # 读取文件内容
        with open(model_file, "r", encoding="utf-8") as f:
            api_json = f.read()

        api_json = json.loads(api_json)

        # 构建提示词
        prompt = f"{BUILD_INSTRUCTIONS}\n\n请理解以下api文档：\n\n{api_json}"

        endpoints = api_json["paths"].keys()
        
        _endpoints = ""
        for endpoint in endpoints:
            _endpoints += endpoint
            prompt += f"Endpoint: {endpoint}\n"

        # 补充提示词
        prompt += "为API json数据，写一份详细的人类友好的API文档，md格式：\n\n"

        # 开始生成代码
        output = asyncio.run(Runner.run(
            auditor,
            input=prompt,
        ))
        final_output = output.final_output

        logger.info(f"编辑日志: {final_output.log}")

        with open(output_dir / f"{model_file.stem}.md", "w", encoding="utf-8") as f:
            f.write(final_output.md)


        with open(README, "a", encoding="utf-8") as f:
            f.write(f"* {_endpoints} - [查看文档]({api_docs_base_url}{model_file.stem}.md)\n")

        # 保存日志
        log_file = output_dir / f"{model_file.stem}_edit_log.txt"
        with open(log_file, "w", encoding="utf-8") as f:
            f.write(final_output.log)
        
        logger.info(f"编辑完成: {model_file.name}")
        # 更新锁文件，避免重复构建
        lock.append(model_file.name)
        lock_file.write_text("\n".join(lock), encoding="utf-8")
        logger.info(f"锁文件更新完成: {lock_file.name}")



if __name__ == "__main__":
    main()