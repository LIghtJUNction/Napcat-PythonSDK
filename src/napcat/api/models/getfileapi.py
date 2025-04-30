# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: ['文件相关']
@homepage: https://napcat.apifox.cn/226658985e0
@llms.txt: https://napcat.apifox.cn/226658985e0.md
@last_update: 2025-04-27 00:53:40

@description: 

summary:获取文件信息

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.43"
__endpoint__ = "get_file"
__id__ = "226658985e0"
__method__ = "POST"

# endregion METADATA


# region code
from pydantic import BaseModel, Field
from typing import Literal

# region req
class GetFileReq(BaseModel):
    """
    获取文件信息请求模型
    """
    file_id: str | None = Field(None, description="二选一，文件ID")
    file: str | None = Field(None, description="二选一，文件路径")

# endregion req



# region res
class GetFileRes(BaseModel):
    """
    获取文件信息响应模型
    """
    class Data(BaseModel):
        """
        响应数据详情
        """
        file: str = Field(..., description="路径或链接")
        url: str = Field(..., description="路径或链接")
        file_size: str = Field(..., description="文件大小")
        file_name: str = Field(..., description="文件名")
        base64: str = Field(..., description="Base64编码")

    status: Literal["ok"] = Field("ok", description="状态码，固定为 'ok'")
    retcode: int = Field(..., description="返回码")
    data: Data = Field(..., description="响应数据")
    message: str = Field(..., description="消息")
    wording: str = Field(..., description="描述")
    echo: str | None = Field(None, description="Echo")

# endregion res

# region api
class GetFileAPI(BaseModel):
    """get_file接口数据模型"""
    endpoint: str = "get_file"
    method: str = "POST"
    Req: type[BaseModel] = GetFileReq
    Res: type[BaseModel] = GetFileRes
# endregion api




# endregion code