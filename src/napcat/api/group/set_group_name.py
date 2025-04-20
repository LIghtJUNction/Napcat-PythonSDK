"""
设置群名 API
用于修改群名称
接口地址: https://napcat.apifox.cn/227425625e0.md

参数：
- group_id: 群号
- group_name: 新的群名称

返回：
- 操作结果

# NapCat 开发中
"""

from typing import TypedDict
from napcat.api.base.models import BaseHttpResponse
# region TypedDicts
class SetGroupNameReq(TypedDict):
    """
    设置群名 API 请求参数
    """
    group_id: int    # 群号
    group_name: str  # 新的群名称

class SetGroupNameRes(BaseHttpResponse[dict[str, bool]]):
    """
    设置群名 API 响应参数
    """
    pass