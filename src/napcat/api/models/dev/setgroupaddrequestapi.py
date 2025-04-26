# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: 群聊相关
@homepage: https://napcat.apifox.cn/226656947e0
@llms.txt: https://napcat.apifox.cn/226656947e0.md
@last_update: 2025-04-27 00:53:40

@description: 

summary:处理加群请求

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.43"
__endpoint__ = "set_group_add_request"
__id__ = "226656947e0"
__method__ = "POST"

# endregion METADATA


# region code
import logging
from typing import Literal
from pydantic import BaseModel, Field

logger = logging.getLogger(__name__)

# region req
class SetGroupAddRequestReq(BaseModel):
    """
    请求参数模型
    """

    flag: str = Field(..., description="请求id")
    approve: bool = Field(..., description="是否同意")
    reason: str | None = Field(None, description="拒绝理由")

# endregion req



# region res
class SetGroupAddRequestRes(BaseModel):
    """
    响应参数模型
    """

    status: Literal["ok"] = Field(..., description="状态")
    retcode: int = Field(..., description="返回码")
    data: None = Field(..., description="数据") # Explicitly null in spec
    message: str = Field(..., description="消息")
    wording: str = Field(..., description="提示")
    echo: str | None = Field(None, description="回显")

# endregion res

# region api
class SetGroupAddRequestAPI(BaseModel):
    """set_group_add_request接口数据模型"""
    endpoint: str = "set_group_add_request"
    method: str = "POST"
    Req: type[BaseModel] = SetGroupAddRequestReq
    Res: type[BaseModel] = SetGroupAddRequestRes
# endregion api




# endregion code
