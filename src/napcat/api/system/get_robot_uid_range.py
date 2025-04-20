"""
获取机器人账号范围 API
用于获取机器人账号的使用范围及权限信息
接口地址: https://napcat.apifox.cn/226658975e0.md

参数：
无需参数

返回：
- 包含机器人账号范围的对象，通常包括账号的权限级别、可用功能范围等信息
- 可能包含账号类型(普通/高级/企业等)以及相应的功能限制说明

注意：
- 此API可用于判断当前机器人账号可以使用的功能范围
- 不同类型账号的权限和功能限制可能不同
- 账号范围信息可能随服务政策变更而改变

# NapCat 开发中
"""

from pydantic import BaseModel
from napcat.api.base.models import BaseHttpResponse

class GetRobotUidRangeReq(BaseModel):
    """
    获取机器人账号范围 API 请求参数
    """
    pass  # 无需参数

class FeatureLimit(BaseModel):
    """
    功能限制信息
    """
    feature: str      # 功能名称
    limit: int        # 限制值
    description: str  # 限制说明

class AccountInfo(BaseModel):
    """
    账号信息
    """
    type: str                # 账号类型(普通/高级/企业等)
    permission_level: int    # 权限级别
    features: list[str]      # 可用功能列表
    limits: list[FeatureLimit]  # 功能限制列表
    expire_time: int         # 过期时间戳(如果适用)

class GetRobotUidRangeRes(BaseHttpResponse[AccountInfo]):
    """
    获取机器人账号范围 API 响应参数
    """
    pass