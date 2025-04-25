# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: 账号相关
@homepage: https://napcat.apifox.cn/226659167e0
@llms.txt: https://napcat.apifox.cn/226659167e0.md
@last_update: 2025-04-26 01:17:44

@description: 设置群聊已读

summary:设置群聊已读

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "mark_group_msg_as_read"
__id__ = "226659167e0"
__method__ = "POST"

# endregion METADATA


# region code
import logging
from pydantic import BaseModel, Field

logger = logging.getLogger(__name__)

# region req
class MarkGroupMsgAsReadReq(BaseModel):
    """
    设置群聊已读 请求参数
    """

    group_id: int | str = Field(..., description="群号")
# endregion req



# region res
class MarkGroupMsgAsReadRes(BaseModel):
    """
    设置群聊已读 响应参数
    """
    status: str = Field(..., description="状态，'ok' 表示成功")
    retcode: int = Field(..., description="返回码")
    data: None = Field(..., description="响应数据，固定为 null")
    message: str = Field(..., description="消息")
    wording: str = Field(..., description="补充消息")
    echo: str | None = Field(None, description="回显")
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