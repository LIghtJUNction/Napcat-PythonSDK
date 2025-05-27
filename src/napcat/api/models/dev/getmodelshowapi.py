# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/227233981e0
@llms.txt: https://napcat.apifox.cn/227233981e0.md
@last_update: 2025-05-28 01:34:10

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
import logging

logger = logging.getLogger(__name__)

# region component_models
class Result(BaseModel):
    """通用构建结果类"""
    status: Literal["ok"] = Field(default="ok", description="状态码，固定为'ok'")
    retcode: float = Field(description="返回码")
    data: dict[str, object] = Field(default_factory=dict, description="数据字段")
    message: str = Field(default="", description="消息")
    wording: str = Field(default="", description="提示语")
    echo: str | None = Field(default=None, description="回显信息")

    model_config = {
        "extra": "allow",
    }
# endregion component_models/

# region req
class GetModelShowReq(BaseModel):
    """_获取在线机型 请求模型"""
    model: str = Field(default="napcat", description="模型名称，默认为napcat")

    model_config = {
        "extra": "allow",
    }
# endregion req/


# region res
class GetModelShowRes(BaseModel):
    """_获取在线机型 响应模型"""

    class Variants(BaseModel):
        """Variants 详情"""
        model_show: str = Field(description="模型展示名称")
        need_pay: bool = Field(description="是否需要支付")

        model_config = {
            "extra": "allow",
        }

    class DataItem(BaseModel):
        """响应数据项"""
        variants: Variants = Field(description="变体信息")

        model_config = {
            "extra": "allow",
        }

    status: Literal["ok"] = Field(default="ok", description="状态码，固定为'ok'")
    retcode: float = Field(description="返回码")
    data: list[DataItem] = Field(default_factory=list, description="数据列表")
    message: str = Field(default="", description="消息")
    wording: str = Field(default="", description="提示语")
    echo: str | None = Field(default=None, description="回显信息")

    model_config = {
        "extra": "allow",
    }
# endregion res/

# region api
class GetModelShowAPI(BaseModel):
    """_get_model_show接口数据模型"""
    endpoint: str = Field(default="_get_model_show", description="接口端点")
    method: str = Field(default="POST", description="请求方法")
    Req: type[BaseModel] = Field(default=GetModelShowReq, description="请求模型类型")
    Res: type[BaseModel] = Field(default=GetModelShowRes, description="响应模型类型")

# endregion api/
# endregion code