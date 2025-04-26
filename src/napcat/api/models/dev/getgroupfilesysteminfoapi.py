# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: 文件相关
@homepage: https://napcat.apifox.cn/226658789e0
@llms.txt: https://napcat.apifox.cn/226658789e0.md
@last_update: 2025-04-27 00:53:40

@description: 获取群文件系统信息

summary:获取群文件系统信息

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.43"
__endpoint__ = "get_group_file_system_info"
__id__ = "226658789e0"
__method__ = "POST"

# endregion METADATA


# region code
import logging
from pydantic import BaseModel, Field
from typing import Literal

logger = logging.getLogger(__name__)

# region req
class GetGroupFileSystemInfoReq(BaseModel):
    """
    获取群文件系统信息请求模型
    """

    group_id: int | str = Field(..., description="群号")

# endregion req



# region res
class GetGroupFileSystemInfoRes(BaseModel):
    """
    获取群文件系统信息响应模型
    """

    class Data(BaseModel):
        """
        响应数据详情
        """
        file_count: float = Field(..., description="文件总数")
        limit_count: float = Field(..., description="文件上限")
        used_space: float = Field(..., description="已使用空间")
        total_space: float = Field(..., description="空间上限")

    status: Literal["ok"] = Field(..., description="状态")
    retcode: int = Field(..., description="返回码")
    data: Data = Field(..., description="响应数据")
    message: str = Field(..., description="消息")
    wording: str = Field(..., description="wording")
    echo: str | None = Field(None, description="回声")

# endregion res

# region api
class GetGroupFileSystemInfoAPI(BaseModel):
    """get_group_file_system_info接口数据模型"""
    endpoint: str = "get_group_file_system_info"
    method: str = "POST"
    Req: type[BaseModel] = GetGroupFileSystemInfoReq
    Res: type[BaseModel] = GetGroupFileSystemInfoRes
# endregion api




# endregion code
