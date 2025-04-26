# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/266151849e0
@llms.txt: https://napcat.apifox.cn/266151849e0.md
@last_update: 2025-04-27 00:53:41

@description: 

summary:获取私聊文件链接

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.43"
__endpoint__ = "get_private_file_url"
__id__ = "266151849e0"
__method__ = "POST"

# endregion METADATA


# region code
import logging
from typing import Any
from pydantic import BaseModel, Field

logger = logging.getLogger(__name__)

# region req
class GetPrivateFileUrlReq(BaseModel): # type: ignore
    """
    {{DESC_EndPointReq}}
    """

    pass
# endregion req



# region res
class GetPrivateFileUrlRes(BaseModel): # type: ignore
    # 定义响应参数
    # 例如：
    # param1: str = Field(..., description="参数1的描述")
    # param2: int = Field(..., description="参数2的描述")
    
    pass
# endregion res

# region api
class GetPrivateFileUrlAPI(BaseModel):
    """get_private_file_url接口数据模型"""
    endpoint: str = "get_private_file_url"
    method: str = "POST"
    Req: type[BaseModel] = GetPrivateFileUrlReq
    Res: type[BaseModel] = GetPrivateFileUrlRes
# endregion api




# endregion code

