"""
群组单人禁言 API
用于禁言群组中的指定成员
接口地址: https://napcat.apifox.cn/227425675e0.md

参数：
- group_id: 群号
- user_id: 用户QQ号
- duration: 禁言时长，单位秒，0表示取消禁言

返回：
- 操作结果

# NapCat 开发中
"""

from pydantic import BaseModel
from napcat.api.base.models import BaseHttpResponse

class SetGroupBanReq(BaseModel):
    """
    群组单人禁言 API 请求参数
    """
    group_id: int  # 群号
    user_id: int   # 用户QQ号
    duration: int  # 禁言时长，单位秒，0表示取消禁言

class SetGroupBanRes(BaseHttpResponse[dict[str, bool]]):
    """
    群组单人禁言 API 响应参数
    """
    pass