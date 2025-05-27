# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/226657379e0
@llms.txt: https://napcat.apifox.cn/226657379e0.md
@last_update: 2025-05-28 01:34:09

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
from pydantic import BaseModel, Field
from typing import Literal, Any

# region component_models
class result(BaseModel):
    """
    Generic API response structure.
    Note: This is based on '#/components/schemas/result' and might be overridden
    for specific API responses.
    """
    status: Literal["ok"] = Field("ok", description="Status of the operation. Always 'ok' for success.")
    retcode: float = Field(0.0, description="Return code of the operation.")
    data: dict[str, Any] = Field({}, description="Generic data payload. As per component schema, this is an object.")
    message: str = Field("", description="Message describing the operation result.")
    wording: str = Field("", description="Wording associated with the operation result.")
    echo: str | None = Field(None, description="Echo field for tracing or additional info.")

    model_config = {
        "extra": "allow",
    }
# region component_models/

# region req
class GetOnlineClientsReq(BaseModel):
    """获取当前账号在线客户端列表 Request Model"""
    # No request parameters as per OpenAPI spec
    pass

    model_config = {
        "extra": "allow",
    }
# region req/


# region res
class GetOnlineClientsRes(BaseModel):
    """获取当前账号在线客户端列表 Response Model"""
    # Based on paths./get_online_clients.post.responses.200
    status: Literal["ok"] = Field("ok", description="Status of the operation. Always 'ok' for success.")
    retcode: float = Field(0.0, description="Return code of the operation.")
    data: list[str] = Field([], description="List of online client IDs. Overrides generic 'result' data type.")
    message: str = Field("", description="Message describing the operation result.")
    wording: str = Field("", description="Wording associated with the operation result.")
    echo: str | None = Field(None, description="Echo field for tracing or additional info.")

    model_config = {
        "extra": "allow",
    }
# region res/

# region api
class GetOnlineClientsAPI(BaseModel):
    """get_online_clients接口数据模型"""
    endpoint: str = "get_online_clients"
    method: str = "POST"
    Req: type[BaseModel] = GetOnlineClientsReq
    Res: type[BaseModel] = GetOnlineClientsRes

# region api/
# endregion code