# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: 账号相关
@homepage: https://napcat.apifox.cn/226657389e0
@llms.txt: https://napcat.apifox.cn/226657389e0.md
@last_update: 2025-04-27 00:53:40

@description: 

summary:设置消息已读

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.43"
__endpoint__ = "mark_msg_as_read"
__id__ = "226657389e0"
__method__ = "POST"

# endregion METADATA


# region code
import logging
from pydantic import BaseModel, Field
from typing import Literal

logger = logging.getLogger(__name__)

# region req
class MarkMsgAsReadReq(BaseModel):
    """
    设置消息已读请求模型
    """

    group_id: int | str | None = Field(
        default=None,
        description="群号，与user_id二选一",
    )
    user_id: int | str | None = Field(
        default=None,
        description="用户ID，与group_id二选一",
    )

# endregion req



# region res
class MarkMsgAsReadRes(BaseModel):
    """
    设置消息已读响应模型
    """
    
    status: Literal["ok"] = Field(
        description="状态"
    )
    retcode: int = Field(
        description="返回码"
    )
    data: None = Field(
        default=None,
        description="数据，总是null"
    )
    message: str = Field(
        description="消息"
    )
    wording: str = Field(
        description="wording"
    )
    echo: str | None = Field(
        default=None,
        description="echo"
    )

# endregion res

# region api
class MarkMsgAsReadAPI(BaseModel):
    """mark_msg_as_read接口数据模型"""
    endpoint: str = "mark_msg_as_read"
    method: str = "POST"
    Req: type[BaseModel] = MarkMsgAsReadReq
    Res: type[BaseModel] = MarkMsgAsReadRes
# endregion api




# endregion code
