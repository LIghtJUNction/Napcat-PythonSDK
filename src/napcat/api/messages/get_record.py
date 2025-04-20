"""
获取语音 API
用于获取语音文件
接口地址: https://napcat.apifox.cn/227229115e0.md

参数：
- file: 语音文件名
- out_format: 输出格式，默认mp3

返回：
- 语音文件信息

# NapCat 开发中
"""

from pydantic import BaseModel
from napcat.api.base.models import BaseHttpResponse

class GetRecordReq(BaseModel):
    """
    获取语音 API 请求参数
    """
    file: str         # 语音文件名
    out_format: str   # 输出格式

class RecordInfo(BaseModel):
    """
    语音信息
    """
    file: str      # 语音文件名
    length: int    # 语音长度（秒）
    filename: str  # 语音文件名
    url: str       # 语音下载链接

class GetRecordRes(BaseHttpResponse[RecordInfo]):
    """
    获取语音 API 响应参数
    """
    pass