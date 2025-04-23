# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/227738594e0
@llms.txt: https://napcat.apifox.cn/227738594e0.md
@last_update: 2025-04-23 20:23:18

@description: 

summary:获取小程序卡片

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "get_mini_app_ark"
__id__ = "227738594e0"
__method__ = "POST"

# region METADATA/


# region code
from typing import Any
from pydantic import BaseModel, Field
from typing import Union

# region req
class GetMiniAppArkReq(BaseModel):
    """
    请求参数
    """

    type: str | None = Field(None, description="只填入必须参数的话该值必须填")
    title: str = Field(..., description="标题")
    desc: str = Field(..., description="内容")
    picUrl: str = Field(..., description="图片链接")
    jumpUrl: str = Field(..., description="跳转链接")
    iconUrl: str | None = Field(None, description="")
    sdkId: str | None = Field(None, description="")
    appId: str | None = Field(None, description="")
    scene: float | str | None = Field(None, description="")
    templateType: float | str | None = Field(None, description="")
    businessType: float | str | None = Field(None, description="")
    verType: float | str | None = Field(None, description="")
    shareType: float | str | None = Field(None, description="")
    versionId: str | None = Field(None, description="")
    withShareTicket: float | str | None = Field(None, description="")
    rawArkData: bool | str | None = Field(None, description="")
# region req/


# region res
class GetMiniAppArkRes(BaseModel):
    """
    响应参数
    """

    pass
# region res/

# region api
class GetMiniAppArkAPI(BaseModel):
    
    Request : type[GetMiniAppArkReq] = GetMiniAppArkReq
    Response  : type[GetMiniAppArkRes] = GetMiniAppArkRes


# region api/
# region code/

