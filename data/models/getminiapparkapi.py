# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/227738594e0
@llms.txt: https://napcat.apifox.cn/227738594e0.md
@last_update: 2025-05-28 01:34:11

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
from pydantic import BaseModel, Field
from typing import Any
import logging

logger = logging.getLogger(__name__)

# region req
class GetMiniAppArkReq(BaseModel):
    """获取小程序卡片"""
    type: str | None = Field(None, description="只填入必须参数的话该值必须填")
    title: str = Field(description="标题")
    desc: str = Field(description="内容")
    picUrl: str = Field(description="图片链接")
    jumpUrl: str = Field(description="跳转链接")
    iconUrl: str | None = Field(None)
    sdkId: str | None = Field(None)
    appId: str | None = Field(None)
    scene: float | str | None = Field(None)
    templateType: float | str | None = Field(None)
    businessType: float | str | None = Field(None)
    verType: float | str | None = Field(None)
    shareType: float | str | None = Field(None)
    versionId: str | None = Field(None)
    withShareTicket: float | str | None = Field(None)
    rawArkData: bool | str | None = Field(None)

    model_config = {
        "extra": "allow",
    }
# region req/


# region res
class GetMiniAppArkRes(BaseModel):
    """获取小程序卡片"""
    class Data(BaseModel):
        """响应数据类型"""
        yes: bool = Field(default=True, description="是否可用")
        reason: str | None = Field(default=None, description="原因")

        model_config = {
            "extra": "allow",
        }

    status: str = Field(default="ok", description="状态，如 'ok'")
    retcode: float = Field(default=0, description="返回码，0表示成功")
    data: Data = Field(default_factory=lambda: Data(), description="响应数据")
    message: str = Field(default="", description="消息")
    wording: str = Field(default="", description="文字描述")
    echo: str | None = Field(default=None, description="回显内容")

    model_config = {
        "extra": "allow",
    }
# region res/

# region api
class GetMiniAppArkAPI(BaseModel):
    """get_mini_app_ark接口数据模型"""
    endpoint: str = "get_mini_app_ark"
    method: str = "POST"
    Req: type[BaseModel] = GetMiniAppArkReq
    Res: type[BaseModel] = GetMiniAppArkRes

# region api/
# endregion code

