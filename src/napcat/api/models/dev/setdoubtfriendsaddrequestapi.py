# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: 其他
@homepage: https://napcat.apifox.cn/289565525e0
@llms.txt: https://napcat.apifox.cn/289565525e0.md
@last_update: 2025-04-27 00:53:41

@description: 

summary:set_doubt_friends_add_request

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.43"
__endpoint__ = "set_doubt_friends_add_request"
__id__ = "289565525e0"
__method__ = "GET"

# endregion METADATA


# region code
from pydantic import BaseModel, Field

# region req
class SetDoubtFriendsAddRequestReq(BaseModel):
    """
    set_doubt_friends_add_request接口请求模型
    对应 OpenAPI Parameters
    """
    # OpenAPI spec shows no parameters
    pass
# endregion req



# region res
class SetDoubtFriendsAddRequestRes(BaseModel):
    """
    set_doubt_friends_add_request接口响应模型
    对应 OpenAPI 200 Response Body
    """
    # OpenAPI spec shows an empty response object {}
    pass
# endregion res

# region api
class SetDoubtFriendsAddRequestAPI(BaseModel):
    """set_doubt_friends_add_request接口数据模型"""
    endpoint: str = Field("set_doubt_friends_add_request", description="接口端点")
    method: str = Field("GET", description="HTTP方法")
    Req: type[BaseModel] = Field(SetDoubtFriendsAddRequestReq, description="请求数据模型")
    Res: type[BaseModel] = Field(SetDoubtFriendsAddRequestRes, description="响应数据模型")
# endregion api




# endregion code
