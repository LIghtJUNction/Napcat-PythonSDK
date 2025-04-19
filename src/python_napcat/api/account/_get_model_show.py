"""
获取在线机型 API
用于获取当前账号设置的在线机型信息
接口地址: https://napcat.apifox.cn/227233981e0.md

参数：
无需参数

返回：
- 当前在线机型信息，包含机型ID、机型名称和显示信息等

# NapCat 开发中
"""

from typing import TypedDict
from python_napcat.api.base.types import BaseHttpResponse

class GetModelShowReq(TypedDict):
    """
    获取在线机型 API 请求参数
    """
    model : str  # 机型ID

class ModelVariant(TypedDict):
    """
    机型变体信息
    """
    model_show : str  # 机型名称
    need_pay : bool   # 是否需要付费

class ModelData(TypedDict):
    """
    机型数据
    """
    variants : ModelVariant  # 机型变体信息

# 使用ModelData类型作为泛型参数
class GetModelShowRes(BaseHttpResponse[ModelData]):
    """
    获取在线机型 API 响应参数
    """
    pass  # 继承基类的所有字段，无需重复定义