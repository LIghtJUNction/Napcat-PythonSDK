# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: 群聊相关
@homepage: https://napcat.apifox.cn/226656979e0
@llms.txt: https://napcat.apifox.cn/226656979e0.md
@last_update: 2025-04-26 01:17:44

@description: 

summary:获取群信息

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "get_group_info"
__id__ = "226656979e0"
__method__ = "POST"

# endregion METADATA


# region code
import logging
from pydantic import BaseModel, Field

logger = logging.getLogger(__name__)

# region req
class GetGroupInfoReq(BaseModel): # type: ignore
    """
    获取群信息请求模型
    """

    group_id: int | str = Field(..., description="群号")
# endregion req



# region res
class GetGroupInfoRes(BaseModel): # type: ignore
    """
    获取群信息响应模型
    """
    status: str = Field(..., description="状态")
    retcode: int = Field(..., description="返回码")
    data: dict = Field(..., description="响应数据") # Data is an empty object {} in the spec
    message: str = Field(..., description="消息")
    wording: str = Field(..., description="提示")
    echo: str | None = Field(None, description="Echo") # Nullable field

# endregion res

# region api
class GetGroupInfoAPI(BaseModel):
    """get_group_info接口数据模型"""
    endpoint: str = "get_group_info"
    method: str = "POST"
    Req: type[BaseModel] = GetGroupInfoReq
    Res: type[BaseModel] = GetGroupInfoRes
# endregion api




# endregion code
