# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: 账号相关
@homepage: https://napcat.apifox.cn/226659194e0
@llms.txt: https://napcat.apifox.cn/226659194e0.md
@last_update: 2025-04-26 01:17:45

@description: 

summary:_设置所有消息已读

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "_mark_all_as_read"
__id__ = "226659194e0"
__method__ = "POST"

# endregion METADATA


# region code
import logging
from pydantic import BaseModel, Field

logger = logging.getLogger(__name__)

# region req
class MarkAllAsReadReq(BaseModel):
    """
    _设置所有消息已读 请求体
    对应 OpenAPI schema: type: object, properties: {}
    """
    pass
# endregion req



# region res
class MarkAllAsReadRes(BaseModel):
    """
    _设置所有消息已读 响应体
    对应 OpenAPI schema for 200 response content.
    """
    status: str = Field(
        default="ok",
        const=True,
        description="响应状态"
        )
    retcode: int = Field(..., description="状态码")
    data: None = Field(
        default=None,
        description="响应数据，此处为null"
        )
    message: str = Field(..., description="错误信息")
    wording: str = Field(..., description="错误提示，适用于人类阅读")
    echo: str | None = Field(
        default=None,
        description="回传 echo，字符串或 null"
        )
# endregion res

# region api
class MarkAllAsReadAPI(BaseModel):
    """_mark_all_as_read接口数据模型"""
    endpoint: str = "_mark_all_as_read"
    method: str = "POST"
    Req: type[BaseModel] = MarkAllAsReadReq
    Res: type[BaseModel] = MarkAllAsReadRes
# endregion api




# endregion code
