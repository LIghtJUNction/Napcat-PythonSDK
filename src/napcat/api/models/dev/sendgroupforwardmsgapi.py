# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: 消息相关/发送群聊消息
@homepage: https://napcat.apifox.cn/226657396e0
@llms.txt: https://napcat.apifox.cn/226657396e0.md
@last_update: 2025-04-27 00:53:40

@description: 

summary:发送群合并转发消息

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.43"
__endpoint__ = "send_group_forward_msg"
__id__ = "226657396e0"
__method__ = "POST"

# endregion METADATA


# region code
import logging
from typing import Literal
from pydantic import BaseModel, Field

logger = logging.getLogger(__name__)

# region req
class ForwardMessageNodeData(BaseModel):
    """一级合并转发消息数据"""
    user_id: int | str = Field(..., description="用户ID")
    nickname: str = Field(..., description="用户昵称")
    # content can be complex, using any to cover all possibilities based on OpenAPI anyOf
    content: list[any] = Field(..., description="消息内容列表 (多种类型)")

class ForwardMessageNode(BaseModel):
    """一级合并转发消息节点"""
    type: Literal["node"] = Field("node", description="消息类型, 固定为 'node'")
    data: ForwardMessageNodeData = Field(..., description="合并转发消息数据")

class NewsItem(BaseModel):
    """外显文本条目"""
    text: str = Field(..., description="外显文本内容")

class SendGroupForwardMsgReq(BaseModel):
    """发送群合并转发消息请求"""

    group_id: int | str = Field(..., description="群组 ID")
    messages: list[ForwardMessageNode] = Field(..., description="合并转发消息节点列表")
    news: list[NewsItem] = Field(..., description="外显文本列表")
    prompt: str = Field(..., description="外显文本")
    summary: str = Field(..., description="底部文本")
    source: str = Field(..., description="内容标题")

# endregion req



# region res
class SendGroupForwardMsgResData(BaseModel):
    """发送群合并转发消息响应数据"""
    message_id: int = Field(..., description="消息 ID")
    res_id: str = Field(..., description="响应 ID")

class SendGroupForwardMsgRes(BaseModel):
    """发送群合并转发消息响应"""
    status: Literal["ok"] = Field(..., description="响应状态")
    retcode: int = Field(..., description="响应返回码")
    data: SendGroupForwardMsgResData = Field(..., description="响应数据")
    message: str = Field(..., description="响应消息")
    wording: str = Field(..., description="响应文案")
    echo: str | None = Field(None, description="Echo 参数")

# endregion res

# region api
class SendGroupForwardMsgAPI(BaseModel):
    """send_group_forward_msg接口数据模型"""
    endpoint: str = "send_group_forward_msg"
    method: str = "POST"
    Req: type[BaseModel] = SendGroupForwardMsgReq
    Res: type[BaseModel] = SendGroupForwardMsgRes
# endregion api




# endregion code