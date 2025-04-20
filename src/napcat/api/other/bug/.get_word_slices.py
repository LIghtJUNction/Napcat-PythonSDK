"""
获取中文分词 API
用于将中文文本进行分词处理，将连续的文本切分为有语义的词语单元
接口地址: https://napcat.apifox.cn/228534368e0.md

参数：
- content: 需要进行分词的文本内容

返回：
- 包含分词结果的对象，通常是词语数组或带位置信息的分词列表

注意：
- 此API目前标记为bug状态，可能存在稳定性或功能问题
- 分词结果的准确性可能受到文本复杂度和语境的影响
- 特殊领域的专业词汇可能无法被正确识别
- 如无特殊需求，建议等待API修复后再使用

# NapCat 开发中
"""

from pydantic import BaseModel
from python_napcat.api.base.types import BaseHttpResponse

class GetWordSlicesReq(BaseModel):
    """
    获取中文分词 API 请求参数
    """
    content: str  # 需要进行分词的文本内容

class WordSlice(BaseModel):
    """
    分词信息
    """
    word: str    # 分词结果
    start: int   # 在原文中的起始位置
    length: int  # 词语长度

class GetWordSlicesRes(BaseHttpResponse[list[WordSlice]]):
    """
    获取中文分词 API 响应参数
    """
    pass