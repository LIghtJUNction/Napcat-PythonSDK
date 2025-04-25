# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: 消息相关/发送群聊消息
@homepage: https://napcat.apifox.cn/226659074e0
@llms.txt: https://napcat.apifox.cn/226659074e0.md
@last_update: 2025-04-26 01:17:44

@description: 

summary:消息转发到群

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "forward_group_single_msg"
__id__ = "226659074e0"
__method__ = "POST"

# endregion METADATA


# region code
from pydantic import BaseModel, Field, Literal


# region req
class ForwardGroupSingleMsgReq(BaseModel):
    """
    消息转发到群 请求模型
    """

    group_id: int | str = Field(..., description="群号")
    message_id: int | str = Field(..., description="消息ID")
# endregion req



# region res
class ForwardGroupSingleMsgRes(BaseModel):
    """
    消息转发到群 响应模型
    """

    status: Literal["ok"] = Field("ok", description="响应状态，固定为 'ok'")
    retcode: int = Field(..., description="返回码")
    data: None = Field(None, description="响应数据，固定为 null")
    message: str = Field(..., description="响应消息")
    wording: str = Field(..., description="响应词语")
    echo: str | None = Field(None, description="回显字段")
# endregion res

# region api
class ForwardGroupSingleMsgAPI(BaseModel):
    """forward_group_single_msg接口数据模型"""
    endpoint: str = "forward_group_single_msg"
    method: str = "POST"
    Req: type[BaseModel] = ForwardGroupSingleMsgReq
    Res: type[BaseModel] = ForwardGroupSingleMsgRes
# endregion api




# endregion code
