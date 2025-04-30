# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: 其他/接口
@homepage: https://napcat.apifox.cn/226659317e0
@llms.txt: https://napcat.apifox.cn/226659317e0.md
@last_update: 2025-04-27 00:53:40

@description:
summary:get_guild_service_profile

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.43"
__endpoint__ = "get_guild_service_profile"
__id__ = "226659317e0"
__method__ = "POST"

# endregion METADATA


# region code
from pydantic import BaseModel, Field

# region req
class GetGuildServiceProfileReq(BaseModel):
    """
    请求参数模型
    """
    # 根据openapi文档，该接口没有请求参数
    pass
# endregion req


# region res
class GetGuildServiceProfileRes(BaseModel):
    """
    响应参数模型
    """
    # 根据openapi文档，响应体是一个空对象
    pass
# endregion res

# region api
class GetGuildServiceProfileAPI(BaseModel):
    """get_guild_service_profile接口数据模型"""
    endpoint: str = Field("get_guild_service_profile", description="API端点")
    method: str = Field("POST", description="HTTP方法")
    Req: type[BaseModel] = Field(GetGuildServiceProfileReq, description="请求模型")
    Res: type[BaseModel] = Field(GetGuildServiceProfileRes, description="响应模型")
# endregion api

# endregion code