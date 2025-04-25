# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: 账号相关
@homepage: https://napcat.apifox.cn/227233981e0
@llms.txt: https://napcat.apifox.cn/227233981e0.md
@last_update: 2025-04-26 01:17:45

@description: _获取在线机型

summary:_获取在线机型

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "_get_model_show"
__id__ = "227233981e0"
__method__ = "POST"

# endregion METADATA


# region code
import logging
from typing import Literal
from pydantic import BaseModel, Field

logger = logging.getLogger(__name__)

# region req
class GetModelShowReq(BaseModel):
    """
    _获取在线机型 请求数据模型
    """

    model: str = Field(..., description="模型名称")

# endregion req



# region res
class GetModelShowRes(BaseModel):
    """
    _获取在线机型 响应数据模型
    """



    class DataItem(BaseModel):
        """
        数据项
        """
        class Variants(BaseModel):
            """
            变体信息
            """
            model_show: str = Field(..., description="模型展示名称")
            need_pay: bool = Field(..., description="是否需要付费")

        variants: Variants = Field(..., description="变体信息")

    status: Literal["ok"] = Field("ok", description="状态")
    retcode: int = Field(..., description="返回码")
    data: list[DataItem] = Field(..., description="数据")
    message: str = Field(..., description="消息")
    wording: str = Field(..., description="文案")
    echo: str | None = Field(None, description="回显信息")

# endregion res

# region api
class GetModelShowAPI(BaseModel):
    """_get_model_show接口数据模型"""
    endpoint: str = "_get_model_show"
    method: str = "POST"
    Req: type[BaseModel] = GetModelShowReq
    Res: type[BaseModel] = GetModelShowRes
# endregion api




# endregion code
