"""
未知接口 API
用于测试未定义的API功能
接口地址: https://napcat.apifox.cn/227495462e0.md

参数：
- action: 接口动作名称
- params: 接口参数，为JSON对象

返回：
- 接口调用结果

# NapCat 开发中
"""

from typing import Any
from pydantic import BaseModel
from napcat.api.base.types import BaseHttpResponse

class UnknownReq(BaseModel):
    """
    未知接口 API 请求参数
    """
    action: str            # 接口动作名称
    params: dict[str, Any] # 接口参数

class UnknownRes(BaseHttpResponse[dict[str, Any]]):
    """
    未知接口 API 响应参数
    """
    pass