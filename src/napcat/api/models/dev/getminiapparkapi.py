# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: ['账号相关']
@homepage: https://napcat.apifox.cn/227738594e0
@llms.txt: https://napcat.apifox.cn/227738594e0.md
@last_update: 2025-04-27 00:53:41

@description: 

summary:获取小程序卡片

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.43"
__endpoint__ = "get_mini_app_ark"
__id__ = "227738594e0"
__method__ = "POST"

# endregion METADATA


# region code
import logging
from pydantic import BaseModel, Field
from typing import Literal

logger = logging.getLogger(__name__)

# region req
class GetMiniAppArkReq(BaseModel):
    """
    获取小程序卡片请求参数
    """

    type: Literal["bili", "weibo"] | None = Field(None, description="只填入必须参数的话该值必须填")
    title: str = Field(..., description="标题")
    desc: str = Field(..., description="内容")
    picUrl: str = Field(..., description="图片链接")
    jumpUrl: str = Field(..., description="跳转链接")
    iconUrl: str | None = Field(None, description="")
    sdkId: str | None = Field(None, description="")
    appId: str | None = Field(None, description="")
    scene: int | str | None = Field(None, description="")
    templateType: int | str | None = Field(None, description="")
    businessType: int | str | None = Field(None, description="")
    verType: int | str | None = Field(None, description="")
    shareType: int | str | None = Field(None, description="")
    versionId: str | None = Field(None, description="")
    withShareTicket: int | str | None = Field(None, description="")
    rawArkData: bool | str | None = Field(None, description="")

# endregion req



# region res
class GetMiniAppArkRes(BaseModel):
    """
    获取小程序卡片响应参数
    Note: The API spec indicates an empty response body schema (properties: {}). 
    Assuming a standard Napcat response wrapper structure.
    """
    retcode: int = Field(..., description="响应码")
    status: Literal["ok", "failed"] = Field(..., description="响应状态")
    data: dict | None = Field(None, description="响应数据")
    # The OpenAPI spec shows an empty object for properties,
    # so the data field contains no specific defined structure.
    # If there were properties defined under the response schema,
    # a nested Data class would be defined here.

# endregion res

# region api
class GetMiniAppArkAPI(BaseModel):
    """get_mini_app_ark接口数据模型"""
    endpoint: str = "get_mini_app_ark"
    method: str = "POST"
    Req: type[BaseModel] = GetMiniAppArkReq
    Res: type[BaseModel] = GetMiniAppArkRes
# endregion api




# endregion code
