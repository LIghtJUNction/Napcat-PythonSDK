# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: 消息相关
@homepage: https://napcat.apifox.cn/226656707e0
@llms.txt: https://napcat.apifox.cn/226656707e0.md
@last_update: 2025-04-26 01:17:44

@description: 

summary:获取消息详情

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "get_msg"
__id__ = "226656707e0"
__method__ = "POST"

# endregion METADATA


# region code
import logging
from pydantic import BaseModel, Field
from typing import Literal # Use Literal for const status

logger = logging.getLogger(__name__)

# region req
class GetMsgReq(BaseModel):
    """
    获取消息详情请求模型
    """
    message_id: int | str = Field(..., description="消息ID，可以是数字或字符串")
# endregion req



# region res
class GetMsgRes(BaseModel):
    """
    获取消息详情响应模型
    """
    status: Literal["ok"] = Field(..., description="响应状态，固定为 'ok'")
    retcode: int = Field(..., description="响应码") # Assuming retcode is an integer
    data: dict = Field(..., description="响应数据") # Based on schema override, data is an empty object
    message: str = Field(..., description="响应消息")
    wording: str = Field(..., description="响应提示")
    echo: str | None = Field(None, description="echo，可能是字符串或null") # Field(None, ...) makes it optional/nullable correctly
# endregion res

# region api
class GetMsgAPI(BaseModel):
    """get_msg接口数据模型"""
    endpoint: str = "get_msg"
    method: str = "POST"
    Req: type[BaseModel] = GetMsgReq
    Res: type[BaseModel] = GetMsgRes
# endregion api




# endregion code
