"""
删除好友 API
用于删除指定好友关系
接口地址: https://napcat.apifox.cn/227233981e0.md

参数：
- user_id: 要删除的好友QQ号

返回：
- 操作结果及状态信息
"""

from typing import TypedDict
from napcat.api.base.models import BaseHttpResponse
# region TypedDicts
class DeleteFriendReq(TypedDict):
    """
    删除好友 API 请求参数
    """
    user_id: int  # 要删除的好友QQ号

class OperationResult(TypedDict):
    """
    操作结果详情
    """
    success: bool    # 是否成功
    message: str     # 操作结果描述

class DeleteFriendRes(BaseHttpResponse[OperationResult]):
    """
    删除好友 API 响应参数
    """
    pass
