"""
设置在线机型 API
用于修改当前账号的在线机型显示
接口地址: https://napcat.apifox.cn/227233981e0.md

参数：
- model: 需要设置的机型ID

返回：
- 操作结果状态及设置后的机型信息
"""

from typing import TypedDict
from napcat.api.base.models import BaseHttpResponse
# region TypedDicts
class SetModelShowReq(TypedDict):
    """
    设置在线机型 API 请求参数
    """
    model: str  # 需要设置的机型ID
    
class ModelSettingResult(TypedDict):
    """
    机型设置结果
    """
    current_model: str  # 当前生效的机型ID
    display_name: str   # 显示名称
    
class SetModelShowRes(BaseHttpResponse[ModelSettingResult]):
    """
    设置在线机型 API 响应参数
    """
    pass
