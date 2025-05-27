# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/226659051e0
@llms.txt: https://napcat.apifox.cn/226659051e0.md
@last_update: 2025-05-28 01:34:09

@description:

summary:消息转发到私聊

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.43"
__endpoint__ = "forward_friend_single_msg"
__id__ = "226659051e0"
__method__ = "POST"

# endregion METADATA


# region code
from pydantic import BaseModel, Field
from typing import Literal

# region req
class ForwardFriendSingleMsgReq(BaseModel):
    """消息转发到私聊 请求模型"""
    # 根据OpenAPI规范，user_id和message_id是联合类型 (number | string)，而非对象。
    user_id: int | str = Field(..., description="目标用户ID，可以是数字或字符串")
    message_id: int | str = Field(..., description="要转发的消息ID，可以是数字或字符串")

    model_config = {
        "extra": "allow",
    }
# endregion req/


# region res
class ForwardFriendSingleMsgRes(BaseModel):
    """消息转发到私聊 响应模型"""
    # 此特定端点的OpenAPI响应模式明确将'data'字段覆盖为类型 'null'。
    # 因此，此响应模型中的'data'字段应为 None。
    # 原始代码中的嵌套Data类在此上下文中不适用。

    status: Literal["ok"] = Field(default="ok", description="status字段，固定为 'ok'")
    retcode: float = Field(default=0.0, description="retcode字段，通常为0表示成功")
    # 根据OpenAPI规范，此接口的'data'字段明确为'null'。
    data: None = Field(default=None, description="data字段，此接口响应为null")
    message: str = Field(default="", description="message字段，描述响应信息")
    wording: str = Field(default="", description="wording字段，提供更详细的描述或提示")
    echo: str | None = Field(default=None, description="echo字段，可选，用于请求-响应匹配")

    model_config = {
        "extra": "allow",
    }
# endregion res/

# region api
class ForwardFriendSingleMsgAPI(BaseModel):
    """forward_friend_single_msg接口数据模型"""
    endpoint: str = "forward_friend_single_msg"
    method: str = "POST"
    Req: type[BaseModel] = ForwardFriendSingleMsgReq
    Res: type[BaseModel] = ForwardFriendSingleMsgRes

# endregion api/
# endregion code
