"""
检查是否可以发送图片 API
用于检查是否可以向指定目标发送图片
接口地址: https://napcat.apifox.cn/227493677e0.md

参数：
无需参数

返回：
- 是否可以发送图片的检查结果

# NapCat 开发中
"""

from napcat.api.base.types import BaseHttpResponse
from pydantic import BaseModel

class CanSendImageReq(BaseModel):
    """
    检查是否可以发送图片 API 请求参数
    """
    pass  # 无需参数

class SendImageStatus(BaseModel):
    """
    发送图片检查状态
    """
    yes: bool  # 是否可以发送图片

class CanSendImageRes(BaseHttpResponse[SendImageStatus]):
    """
    检查是否可以发送图片 API 响应参数
    """
    pass