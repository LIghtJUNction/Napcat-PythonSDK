"""
英译中 API
用于将英文翻译成中文
接口地址: https://napcat.apifox.cn/282546119e0.md

参数：
- text: 需要翻译的英文文本内容
- engine: 翻译引擎(可选)，指定使用的翻译服务

返回：
- 翻译结果，包含翻译后的中文文本和其他相关信息

注意：
- 单次翻译文本长度可能有限制
- 翻译质量受原文表达和引擎能力影响
- 专业术语翻译可能需要特定的翻译引擎

# NapCat 开发中
"""

from pydantic import BaseModel
from napcat.api.base.models import BaseHttpResponse

class TranslateEn2zhReq(BaseModel):
    """
    英译中 API 请求参数
    """
    text: str                  # 需要翻译的英文文本
    engine: str | None = None                # 翻译引擎(可选)，如"default", "baidu", "google"等

class TranslateResult(BaseModel):
    """
    翻译结果
    """
    original_text: str         # 原始英文文本
    translated_text: str       # 翻译后的中文文本
    engine_used: str           # 使用的翻译引擎
    confidence: float          # 翻译置信度(0-1)
    alternatives: list[str]    # 其他可能的翻译结果

class TranslateEn2zhRes(BaseHttpResponse[TranslateResult]):
    """
    英译中 API 响应参数
    """
    pass