# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: 账号相关
@homepage: https://napcat.apifox.cn/227233981e0
@llms.txt: https://napcat.apifox.cn/227233981e0.md
@last_update: 2025-04-27 00:53:41

@description: 

summary:_获取在线机型

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.43"
__endpoint__ = "_get_model_show"
__id__ = "227233981e0"
__method__ = "POST"

# endregion METADATA


# region code
from pydantic import BaseModel, Field
from typing import Literal


# region req
class GetModelShowReq(BaseModel):
    """
    _get_model_show请求数据模型
    """

    model: str = Field(
        "napcat", description="机型名称，默认为 napcat"
    )

# endregion req



# region res
class GetModelShowRes(BaseModel):
    """
    _get_model_show响应数据模型
    """

    class Variants(BaseModel):
        """_get_model_show Variants 嵌套数据模型"""
        model_show: str = Field(..., description="在线机型显示名称")
        need_pay: bool = Field(..., description="是否需要付费")

    class ModelItem(BaseModel):
        """_get_model_show Data Item 嵌套数据模型"""
        variants: Variants = Field(..., description="机型变体信息")

    status: Literal["ok"] = Field(..., description="状态码，固定为 'ok'")
    retcode: int = Field(..., description="返回码")
    data: list[ModelItem] = Field(..., description="在线机型列表")
    message: str = Field(..., description="状态消息")
    wording: str = Field(..., description="状态提示")
    echo: str | None = Field(None, description="echo字段，可能为null")

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
