# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: 文件相关
@homepage: https://napcat.apifox.cn/226658985e0
@llms.txt: https://napcat.apifox.cn/226658985e0.md
@last_update: 2025-04-26 01:17:44

@description: 

summary:获取文件信息

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "get_file"
__id__ = "226658985e0"
__method__ = "POST"

# endregion METADATA


# region code
import logging
from pydantic import BaseModel, Field, constr

logger = logging.getLogger(__name__)

# region req
class GetFileReq(BaseModel):
    """
    获取文件信息请求模型
    """

    file_id: str = Field(..., description="文件ID")

# endregion req



# region res
class GetFileRes(BaseModel):
    """
    获取文件信息响应模型
    """

    class Data(BaseModel):
        """
        文件信息数据
        """
        file: str = Field(..., description="路径或链接")
        url: str = Field(..., description="路径或链接")
        file_size: str = Field(..., description="文件大小")
        file_name: str = Field(..., description="文件名")
        base64: str = Field(..., description="Base64编码的文件内容")

    status: constr(const='ok') = Field(..., description="响应状态，固定为'ok'")
    retcode: int = Field(..., description="响应码")
    data: Data = Field(..., description="文件信息数据")
    message: str = Field(..., description="响应消息")
    wording: str = Field(..., description="响应提示")
    echo: str | None = Field(None, description="Echo字段，可能为null")

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
