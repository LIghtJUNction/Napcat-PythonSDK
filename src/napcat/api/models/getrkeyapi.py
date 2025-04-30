# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: 密钥相关
@homepage: https://napcat.apifox.cn/283136230e0
@llms.txt: https://napcat.apifox.cn/283136230e0.md
@last_update: 2025-04-27 00:53:41

@description: 

summary:获取rkey

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.43"
__endpoint__ = "get_rkey"
__id__ = "283136230e0"
__method__ = "POST"

# endregion METADATA


# region code
import logging
from typing import Literal
from pydantic import BaseModel, Field

logger = logging.getLogger(__name__)

# region req
class GetRkeyReq(BaseModel):
    """
    获取rkey请求模型
    """

    pass
# endregion req



# region res
class GetRkeyRes(BaseModel):
    """
    获取rkey响应模型
    """

    class DataItem(BaseModel):
        """
        Rkey数据项模型
        """
        type: str = Field(..., description="Rkey类型")
        rkey: str = Field(..., description="Rkey值")
        created_at: int = Field(..., description="创建时间戳")
        # Note: OpenAPI spec says string, which is unusual for TTL. Assuming it's a duration string.
        ttl: str = Field(..., description="Rkey的生存时间")

    status: Literal["ok"] = Field("ok", description="状态码，固定为 'ok'")
    retcode: int = Field(..., description="状态码")
    data: list[DataItem] = Field(..., description="Rkey数据列表")
    message: str = Field(..., description="消息")
    wording: str = Field(..., description="附带文案")
    echo: str | None = Field(None, description="回显数据")

# endregion res

# region api
class GetRkeyAPI(BaseModel):
    """get_rkey接口数据模型"""
    endpoint: str = "get_rkey"
    method: str = "POST"
    Req: type[BaseModel] = GetRkeyReq
    Res: type[BaseModel] = GetRkeyRes
# endregion api




# endregion code