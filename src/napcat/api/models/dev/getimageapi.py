# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: ['消息相关']
@homepage: https://napcat.apifox.cn/226657066e0
@llms.txt: https://napcat.apifox.cn/226657066e0.md
@last_update: 2025-04-27 00:53:40

@description: 获取图片消息详情

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
from typing import Literal # Using Literal for status 'ok'

# region req
class GetImageReq(BaseModel):
    """
    请求模型
    """
    file_id: str = Field(..., description="文件ID，例如：226723D7B1EE3BF02E9CFD8236EE468B.jpg")

# endregion req



# region res
class GetImageRes(BaseModel):
    """
    响应模型
    """

    class Data(BaseModel):
        """
        响应数据详情
        """
        file: str = Field(..., description="本地路径")
        url: str = Field(..., description="网络路径")
        file_size: str = Field(..., description="文件大小") # OpenAPI spec says string, keeping string
        file_name: str = Field(..., description="文件名")
        base64: str = Field(..., description="Base64编码的图片数据")

    status: Literal["ok"] = Field(..., description="API执行状态")
    retcode: int = Field(..., description="返回码")
    data: Data = Field(..., description="响应数据详情")
    message: str = Field(..., description="消息")
    wording: str = Field(..., description="描述信息")
    echo: str | None = Field(None, description="echo") # Nullable field, use | None

# endregion res

# region api
class GetImageAPI(BaseModel):
    """get_image接口数据模型"""
    endpoint: str = "get_image"
    method: str = "POST"
    Req: type[BaseModel] = GetImageReq
    Res: type[BaseModel] = GetImageRes
# endregion api




# endregion code
