# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: 文件相关
@homepage: https://napcat.apifox.cn/226658867e0
@llms.txt: https://napcat.apifox.cn/226658867e0.md
@last_update: 2025-04-26 01:17:44

@description: 

summary:获取群文件链接

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "get_group_file_url"
__id__ = "226658867e0"
__method__ = "POST"

# endregion METADATA


# region code
import logging
from pydantic import BaseModel, Field

logger = logging.getLogger(__name__)

# region req
class GetGroupFileUrlReq(BaseModel):
    """
    获取群文件链接请求模型
    """

    group_id: str | int = Field(..., description="群号") # OpenAPI specifies oneOf string or number
    file_id: str = Field(..., description="文件ID")

# endregion req



# region res
class GetGroupFileUrlRes(BaseModel):
    """
    获取群文件链接响应模型
    """

    class Data(BaseModel):
        """
        响应数据模型
        """
        url: str = Field(..., description="文件下载链接")

    status: str = Field(..., description="响应状态", pattern="^ok$")
    retcode: int = Field(..., description="响应码")
    data: Data = Field(..., description="响应数据")
    message: str = Field(..., description="响应消息")
    wording: str = Field(..., description="响应词")
    echo: str | None = Field(None, description="echo") # OpenAPI specifies nullable: true

# endregion res

# region api
class GetGroupFileUrlAPI(BaseModel):
    """get_group_file_url接口数据模型"""
    endpoint: str = "get_group_file_url"
    method: str = "POST"
    Req: type[BaseModel] = GetGroupFileUrlReq
    Res: type[BaseModel] = GetGroupFileUrlRes
# endregion api




# endregion code
