"""
踢出群成员 API
用于将成员踢出群组
接口地址: https://napcat.apifox.cn/227425658e0.md

参数：
- group_id: 群号
- user_id: 用户QQ号
- reject_add_request: 是否拒绝此人的加群请求

返回：
- 操作结果

# NapCat 开发中
"""

from pydantic import BaseModel
from napcat.api.base.models import BaseHttpResponse

class SetGroupKickReq(BaseModel):
    """
    踢出群成员 API 请求参数
    """
    group_id: int           # 群号
    user_id: int            # 用户QQ号
    reject_add_request: bool # 是否拒绝此人的加群请求

class SetGroupKickRes(BaseHttpResponse[dict[str, bool]]):
    """
    踢出群成员 API 响应参数
    """
    pass