# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: 文件相关
@homepage: https://napcat.apifox.cn/226658867e0
@llms.txt: https://napcat.apifox.cn/226658867e0.md
@last_update: 2025-04-27 00:53:40

@description: 

summary:获取群文件链接

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.43"
__endpoint__ = "get_group_file_url"
__id__ = "226658867e0"
__method__ = "POST"

# endregion METADATA


# region code
import logging
from typing import Literal
from pydantic import BaseModel, Field

logger = logging.getLogger(__name__)

# region req
class GetGroupFileUrlReq(BaseModel): # type: ignore
    """
    获取群文件链接请求模型
    """

    group_id: int | str = Field(..., description="群号")
    file_id: str = Field(..., description="文件ID")
# endregion req



# region res
class GetGroupFileUrlRes(BaseModel): # type: ignore
    """
    获取群文件链接响应模型
    """

    class Data(BaseModel):
        """
        响应数据体
        """
        url: str = Field(..., description="群文件链接")

    status: Literal["ok"] = Field(..., description="响应状态")
    retcode: int = Field(..., description="状态码")
    data: Data = Field(..., description="响应数据体")
    message: str = Field(..., description="错误信息")
    wording: str = Field(..., description="错误描述")
    echo: str | None = Field(None, description="用户自定义字段")
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
