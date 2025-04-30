# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: ['
  
        
          群聊相关
        
      ']
@homepage: https://napcat.apifox.cn/226656919e0
@llms.txt: https://napcat.apifox.cn/226656919e0.md
@last_update: 2025-04-27 00:53:40

@description: 

summary:设置群名

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.43"
__endpoint__ = "set_group_name"
__id__ = "226656919e0"
__method__ = "POST"

# endregion METADATA


# region code
import logging
from typing import Literal
from pydantic import BaseModel, Field

logger = logging.getLogger(__name__)

# region req
class SetGroupNameReq(BaseModel):
    """
    设置群名请求模型
    """

    group_id: int | str = Field(
        ..., description="群号"
    )
    group_name: str = Field(
        ..., description="群名"
    )
# endregion req



# region res
class SetGroupNameRes(BaseModel):
    """
    设置群名响应模型
    """

    status: Literal["ok"] = Field(
        "ok", description="状态码，固定为 'ok'"
    )
    retcode: int = Field(
        ..., description="返回码"
    )
    data: None = Field(
        None, description="响应数据 (总是为null)"
    )
    message: str = Field(
        ..., description="信息"
    )
    wording: str = Field(
        ..., description="提示"
    )
    echo: str | None = Field(
        None, description="echo"
    )
# endregion res

# region api
class SetGroupNameAPI(BaseModel):
    """set_group_name接口数据模型"""
    endpoint: str = "set_group_name"
    method: str = "POST"
    Req: type[BaseModel] = SetGroupNameReq
    Res: type[BaseModel] = SetGroupNameRes
# endregion api




# endregion code