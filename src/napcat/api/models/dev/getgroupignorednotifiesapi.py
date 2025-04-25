# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: 群聊相关
@homepage: https://napcat.apifox.cn/226659323e0
@llms.txt: https://napcat.apifox.cn/226659323e0.md
@last_update: 2025-04-26 01:17:45

@description: 

summary:获取群过滤系统消息

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "get_group_ignored_notifies"
__id__ = "226659323e0"
__method__ = "POST"

# endregion METADATA


# region code
import logging
from pydantic import BaseModel, Field

logger = logging.getLogger(__name__)

# region req
class GetGroupIgnoredNotifiesReq(BaseModel):
    """
    获取群过滤系统消息的请求模型
    """
    group_id: str | int = Field(..., description="群号")

# endregion req



# region res
class JoinRequestItem(BaseModel):
    """
    群过滤系统消息中的加群请求详情
    """
    request_id: str = Field(..., description="请求ID")
    requester_uin: str = Field(..., description="请求者的UIN")
    requester_nick: str = Field(..., description="请求者的昵称")
    group_id: str = Field(..., description="群号")
    group_name: str = Field(..., description="群名称")
    checked: bool = Field(..., description="是否已处理")
    actor: str | int = Field(..., description="处理者UIN")

class GetGroupIgnoredNotifiesData(BaseModel):
    """
    获取群过滤系统消息的响应数据详情
    """
You have provided an invalid JSON object. Please check the output JSON structure.```json
{
  