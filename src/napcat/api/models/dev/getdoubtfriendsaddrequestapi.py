# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: 其他
@homepage: https://napcat.apifox.cn/289565516e0
@llms.txt: https://napcat.apifox.cn/289565516e0.md
@last_update: 2025-04-27 00:53:41

@description: get_doubt_friends_add_request endpoint

summary:get_doubt_friends_add_request

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.43"
__endpoint__ = "get_doubt_friends_add_request"
__id__ = "289565516e0"
__method__ = "GET" # Corrected method

# endregion METADATA


# region code
from typing import Literal
from pydantic import BaseModel, Field

# region req
class GetDoubtFriendsAddRequestReq(BaseModel):
    """
    Request model for get_doubt_friends_add_request
    """
    # No parameters according to OpenAPI spec
    pass
# endregion req


# region res
class GetDoubtFriendsAddRequestRes(BaseModel):
    """
    Response model for get_doubt_friends_add_request
    """
    # Typical Napcat API response structure wrapping the spec's empty object
    status: Literal["ok"] = Field("ok", description="Response status")
    retcode: int = Field(..., description="Response return code")
    data: dict = Field({}, description="Response data payload")
# endregion res

# region api
class GetDoubtFriendsAddRequestAPI(BaseModel):
    """get_doubt_friends_add_request interface data model"""
    endpoint: str = "get_doubt_friends_add_request"
    method: str = "GET"
    Req: type[BaseModel] = GetDoubtFriendsAddRequestReq
    Res: type[BaseModel] = GetDoubtFriendsAddRequestRes
# endregion api

# endregion code
