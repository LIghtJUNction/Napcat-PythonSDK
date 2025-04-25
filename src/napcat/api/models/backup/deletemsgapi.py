# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: 
@homepage: https://napcat.apifox.cn/226919954e0
@llms.txt: https://napcat.apifox.cn/226919954e0.md
@last_update: 2025-04-26 01:17:45

@description: 

summary:撤回消息

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "delete_msg"
__id__ = "226919954e0"
__method__ = "POST"

# endregion METADATA


# region code
import logging
from pydantic import BaseModel, Field

logger = logging.getLogger(__name__)

# region req
class DeleteMsgReq(BaseModel):
    """
    撤回消息 请求参数
    """
    message_id: int | str = Field(..., description="要撤回的消息ID")
# endregion req



# region res
class DeleteMsgRes(BaseModel):
    """
    撤回消息 响应参数
    """
    status: str = Field(..., description="状态，例如 'ok'")
    retcode: int = Field(..., description="返回码")
    data: None = Field(..., description="响应数据，此处为null")
    message: str = Field(..., description="错误消息，如果status不是ok")
    wording: str = Field(..., description="错误描述，如果status不是ok")
    echo: str | None = Field(None, description="可以忽略")
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
