# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: [
    "消息相关"
]
@homepage: https://napcat.apifox.cn/226919954e0
@llms.txt: https://napcat.apifox.cn/226919954e0.md
@last_update: 2025-04-27 00:53:41

@description: 

summary:
    撤回消息

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.43"
__endpoint__ = "delete_msg"
__id__ = "226919954e0"
__method__ = "POST"

# endregion METADATA


# region code
import logging
from typing import Literal
from pydantic import BaseModel, Field

logger = logging.getLogger(__name__)

# region req
class DeleteMsgReq(BaseModel):
    """
    撤回消息请求参数
    """

    message_id: int | str = Field(
        ...,
        description="要撤回的消息ID",
        examples=[1768656698]
    )

# endregion req



# region res
class DeleteMsgRes(BaseModel):
    """
    撤回消息响应参数
    """
    # 定义响应参数
    status: Literal["ok"] = Field("ok", description="状态码，固定为 'ok'")
    retcode: int = Field(..., description="返回码")
    data: None = Field(..., description="数据")
    message: str = Field(..., description="错误信息")
    wording: str = Field(..., description="错误信息的友好表述")
    echo: str | None = Field(None, description="echo", examples=["some_echo_string"])

# endregion res

# region api
class DeleteMsgAPI(BaseModel):
    """delete_msg接口数据模型"""
    endpoint: str = "delete_msg"
    method: str = "POST"
    Req: type[BaseModel] = DeleteMsgReq
    Res: type[BaseModel] = DeleteMsgRes
# endregion api




# endregion code