# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: 账号相关
@homepage: https://napcat.apifox.cn/226657379e0
@llms.txt: https://napcat.apifox.cn/226657379e0.md
@last_update: 2025-04-26 01:17:44

@description:

summary:获取当前账号在线客户端列表

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "get_online_clients"
__id__ = "226657379e0"
__method__ = "POST"

# endregion METADATA


# region code
import logging
from pydantic import BaseModel, Field, Literal

logger = logging.getLogger(__name__)

# region req
class GetOnlineClientsReq(BaseModel):
    """
    获取当前账号在线客户端列表 - 请求模型
    """

    no_cache: bool = Field(default=False, description="是否不使用缓存")

# endregion req



# region res
class GetOnlineClientsRes(BaseModel):
    """
    获取当前账号在线客户端列表 - 响应模型
    """

    class GetOnlineClientsResData(BaseModel):
        """
        响应数据模型
        """
        clients: dict = Field(description="在线客户端列表，key为客户端类型，value为客户端信息(目前为空对象)") # Schema specifies an object with no properties

    status: Literal["ok"] = Field("ok", description="状态码，通常为 'ok'")
    retcode: int = Field(..., description="返回码")
    data: GetOnlineClientsResData = Field(..., description="响应数据")
    message: str = Field(..., description="消息")
    wording: str = Field(..., description="描述信息")
    echo: str | None = Field(None, description="回显信息，可选")

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
