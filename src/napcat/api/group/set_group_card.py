"""
设置群名片 API
用于设置群成员的名片（群昵称）
接口地址: https://napcat.apifox.cn/227425609e0.md

参数：
- group_id: 群号
- user_id: 用户QQ号
- card: 新的群名片内容，不填或空字符串表示删除群名片

返回：
- 操作结果

# NapCat 开发中
"""

from pydantic import BaseModel
from napcat.api.base.models import BaseHttpResponse

class SetGroupCardReq(BaseModel):
    """
    设置群名片 API 请求参数
    """
    group_id: int  # 群号
    user_id: int   # 用户QQ号
    card: str      # 新的群名片内容，不填或空字符串表示删除群名片

class SetGroupCardRes(BaseHttpResponse[dict[str, bool]]):
    """
    设置群名片 API 响应参数
    """
    pass