# -*- coding: utf-8 -*-
from __future__ import annotations

# region METADATA
"""
@tags: 其他
@homepage: https://napcat.apifox.cn/289565516e0
@llms.txt: https://napcat.apifox.cn/289565516e0.md
@last_update: 2025-04-27 00:53:41

@description: 
功能：获取可疑的好友添加请求
获取可能需要处理的好友添加请求列表
"""
__author__ = "LIghtJUNction"
__version__ = "4.7.43"
__endpoint__ = "get_doubt_friends_add_request"
__id__ = "289565516e0"
__method__ = "GET"

# endregion METADATA


# region code
import logging
from typing import Literal
from pydantic import BaseModel, Field

logger = logging.getLogger(__name__)
logger.debug("加载 GetDoubtFriendsAddRequestAPI 模型")

# region req
class GetDoubtFriendsAddRequestReq(BaseModel):
    """获取可疑的好友添加请求模型"""
    # 根据OpenAPI规范，此请求不需要任何参数
    pass
# endregion req


# region res
class GetDoubtFriendsAddRequestRes(BaseModel):
    """获取可疑的好友添加请求响应模型"""
    class Data(BaseModel):
        """响应数据模型，当前为空对象"""
        pass
    
    status: Literal["ok"] = Field("ok", description="状态码，固定为 'ok'")
    retcode: int = Field(0, description="返回码")
    data: Data = Field(default_factory=Data, description="响应数据，当前为空对象")
    message: str = Field("", description="消息")
    wording: str = Field("", description="提示文本")
    echo: str | None = Field(None, description="回显数据")
# endregion res

# region api
class GetDoubtFriendsAddRequestAPI(BaseModel):
    """get_doubt_friends_add_request接口数据模型"""
    endpoint: str = "get_doubt_friends_add_request"
    method: str = "GET"
    Req: type[BaseModel] = GetDoubtFriendsAddRequestReq
    Res: type[BaseModel] = GetDoubtFriendsAddRequestRes
# endregion api

# endregion code