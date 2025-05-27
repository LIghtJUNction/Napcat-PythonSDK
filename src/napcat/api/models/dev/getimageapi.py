# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/226657066e0
@llms.txt: https://napcat.apifox.cn/226657066e0.md
@last_update: 2025-05-28 01:34:09

@description:

summary:获取图片消息详情

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.43"
__endpoint__ = "get_image"
__id__ = "226657066e0"
__method__ = "POST"

# endregion METADATA


# region code
from pydantic import BaseModel, Field
from typing import Literal
import logging

logger = logging.getLogger(__name__)

# region req
class GetImageReq(BaseModel):
    """获取图片消息详情请求模型"""
    file_id: str = Field(description="图片文件ID")

    model_config = {
        "extra": "allow",
    }
# region req/


# region res
class GetImageRes(BaseModel):
    """获取图片消息详情响应模型"""
    class Data(BaseModel):
        """响应数据详情"""
        file: str = Field(description="本地路径")
        url: str = Field(description="网络路径")
        file_size: str = Field(description="文件大小")
        file_name: str = Field(description="文件名")
        base64: str = Field(description="base64编码的图片数据")

        model_config = {
            "extra": "allow",
        }

    status: Literal["ok"] = Field(description="状态码，固定为 'ok'")
    retcode: float = Field(description="返回码")
    data: Data = Field(description="响应数据详情")
    message: str = Field(description="消息")
    wording: str = Field(description="提示词")
    echo: str | None = Field(description="echo字段，可为空")

    model_config = {
        "extra": "allow",
    }
# region res/

# region api
class GetImageAPI(BaseModel):
    """get_image接口数据模型"""
    endpoint: str = "get_image"
    method: str = "POST"
    Req: type[BaseModel] = GetImageReq
    Res: type[BaseModel] = GetImageRes

# region api/
# endregion code
