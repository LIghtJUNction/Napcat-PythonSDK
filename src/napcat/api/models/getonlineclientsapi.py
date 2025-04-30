# -*- coding: utf-8 -*-# region METADATA
"""
@tags: 
@homepage: https://napcat.apifox.cn/226657379e0
@llms.txt: https://napcat.apifox.cn/226657379e0.md
@last_update: 2025-04-27 00:53:40

@description: 

summary:获取当前账号在线客户端列表

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.43"
__endpoint__ = "get_online_clients"
__id__ = "226657379e0"
__method__ = "POST"

# endregion METADATA


# region code
import logging
from pydantic import BaseModel, Field
from typing import Literal

logger = logging.getLogger(__name__)

# region req
class GetOnlineClientsReq(BaseModel):
    """
    {{DESC_EndPointReq}}
    """
    # Request body is an empty object according to OpenAPI spec
    pass
# endregion req



# region res
class GetOnlineClientsRes(BaseModel):
    """
    获取当前账号在线客户端列表 响应模型
    """
    status: Literal["ok"] = Field("ok", description="状态码，固定为 'ok'")
    retcode: int = Field(..., description="返回码")
    data: list[str] = Field(..., description="在线客户端列表")
    message: str = Field(..., description="信息")
    wording: str = Field(..., description="额外信息")
    echo: str | None = Field(None, description="回显")

# endregion res

# region api
class GetOnlineClientsAPI(BaseModel):
    """get_online_clients接口数据模型"""
    endpoint: str = "get_online_clients"
    method: str = "POST"
    Req: type[BaseModel] = GetOnlineClientsReq
    Res: type[BaseModel] = GetOnlineClientsRes
# endregion api




# endregion code
