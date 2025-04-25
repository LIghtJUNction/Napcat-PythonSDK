# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: 其他/接口
@homepage: https://napcat.apifox.cn/226659311e0
@llms.txt: https://napcat.apifox.cn/226659311e0.md
@last_update: 2025-04-26 01:17:45

@description: 

summary: get_guild_list

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "get_guild_list"
__id__ = "226659311e0"
__method__ = "POST"

# endregion METADATA


# region code
import logging
from pydantic import BaseModel

logger = logging.getLogger(__name__)

# region req
class GetGuildListReq(BaseModel):
    """
    Request model for get_guild_list endpoint.
    (Based on OpenAPI spec, request body is empty)
    """
    pass
# endregion req



# region res
class GetGuildListRes(BaseModel):
    """
    Response model for get_guild_list endpoint.
    (Based on OpenAPI spec, response body is an empty object)
    """
    pass
# endregion res

# region api
class GetGuildListAPI(BaseModel):
    """get_guild_list接口数据模型"""
    endpoint: str = "get_guild_list"
    method: str = "POST"
    Req: type[BaseModel] = GetGuildListReq
    Res: type[BaseModel] = GetGuildListRes
# endregion api




# endregion code
