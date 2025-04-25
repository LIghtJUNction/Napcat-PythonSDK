# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: 账号相关
@homepage: https://napcat.apifox.cn/226658971e0
@llms.txt: https://napcat.apifox.cn/226658971e0.md
@last_update: 2025-04-26 01:17:44

@description: 

summary:获取推荐群聊卡片

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "ArkShareGroup"
__id__ = "226658971e0"
__method__ = "POST"

# endregion METADATA


# region code
import logging
from pydantic import BaseModel, Field

logger = logging.getLogger(__name__)

# region req
class ArksharegroupReq(BaseModel):
    """
    获取推荐群聊卡片请求参数
    """

    group_id: str = Field(..., description="群号")
# endregion req



# region res
class ArksharegroupRes(BaseModel):
    """
    获取推荐群聊卡片响应参数
    """

    status: str = Field("ok", description="状态")
    retcode: int = Field(..., description="返回码")
    data: str = Field(..., description="卡片json")
    message: str = Field(..., description="消息")
    wording: str = Field(..., description="附加消息")
    echo: str | None = Field(None, description="回显")

# endregion res

# region api
class ArksharegroupAPI(BaseModel):
    """ArkShareGroup接口数据模型"""
    endpoint: str = "ArkShareGroup"
    method: str = "POST"
    Req: type[BaseModel] = ArksharegroupReq
    Res: type[BaseModel] = ArksharegroupRes
# endregion api




# endregion code