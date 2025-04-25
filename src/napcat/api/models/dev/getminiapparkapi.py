# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: 账号相关
@homepage: https://napcat.apifox.cn/227738594e0
@llms.txt: https://napcat.apifox.cn/227738594e0.md
@last_update: 2025-04-26 01:17:45

@description: 

summary:获取小程序卡片

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "get_mini_app_ark"
__id__ = "227738594e0"
__method__ = "POST"

# endregion METADATA


# region code
from pydantic import BaseModel, Field
from enum import Enum

# region req
class MiniAppArkType(str, Enum):
    """小程序卡片类型"""
    BILI = "bili"
    WEIBO = "weibo"

class GetMiniAppArkReq(BaseModel):
    """
    获取小程序卡片请求参数
    """
    type: MiniAppArkType = Field(..., description="只填入必须参数的话该值必须填")
    title: str = Field(..., description="标题")
    desc: str = Field(..., description="内容")
    picUrl: str = Field(..., description="图片链接")
    jumpUrl: str = Field(..., description="跳转链接")
    iconUrl: str | None = Field(None, description="")
    sdkId: str | None = Field(None, description="")
    appId: str | None = Field(None, description="")
    scene: str | int | None = Field(None, description="")
    templateType: str | int | None = Field(None, description="")
    businessType: str | int | None = Field(None, description="")
    verType: str | int | None = Field(None, description="")
    shareType: str | int | None = Field(None, description="")
    versionId: str | None = Field(None, description="")
    withShareTicket: str | int | None = Field(None, description="")
    rawArkData: str | bool | None = Field(None, description="")
# endregion req



# region res
class GetMiniAppArkRes(BaseModel):
    """
    获取小程序卡片响应参数
    """
    pass # Response is an empty object {}
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
