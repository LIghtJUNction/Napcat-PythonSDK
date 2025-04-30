# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: [
    "账号相关"
]
@homepage: https://napcat.apifox.cn/226659167e0
@llms.txt: https://napcat.apifox.cn/226659167e0.md
@last_update: 2025-04-27 00:53:40

@description: 

summary:设置群聊已读

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.43"
__endpoint__ = "mark_group_msg_as_read"
__id__ = "226659167e0"
__method__ = "POST"

# endregion METADATA


# region code
from pydantic import BaseModel, Field
from typing import Literal

# region req
class MarkGroupMsgAsReadReq(BaseModel):
    """
    请求体模型: 设置群聊已读
    """

    group_id: int | str = Field(..., description="群号")
# endregion req



# region res
class MarkGroupMsgAsReadRes(BaseModel):
    """
    响应体模型: 设置群聊已读
    """

    status: Literal["ok"] = Field("ok", description="状态码，固定为 'ok'")
    retcode: int = Field(..., description="返回码")
    data: None = Field(None, description="响应数据")
    message: str = Field(..., description="错误信息")
    wording: str = Field(..., description="错误提示")
    echo: str | None = Field(None, description="发送消息的echo回显")
# endregion res

# region api
class MarkGroupMsgAsReadAPI(BaseModel):
    """mark_group_msg_as_read接口数据模型"""
    endpoint: str = "mark_group_msg_as_read"
    method: str = "POST"
    Req: type[BaseModel] = MarkGroupMsgAsReadReq
    Res: type[BaseModel] = MarkGroupMsgAsReadRes
# endregion api




# endregion code