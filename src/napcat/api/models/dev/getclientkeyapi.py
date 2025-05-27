# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/250286915e0
@llms.txt: https://napcat.apifox.cn/250286915e0.md
@last_update: 2025-05-28 01:34:11

@description: 

summary:获取clientkey

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.43"
__endpoint__ = "get_clientkey"
__id__ = "250286915e0"
__method__ = "POST"

# endregion METADATA


# region code
from pydantic import BaseModel, Field
from typing import Literal, Any
import logging

logger = logging.getLogger(__name__)

# region component_models
class Result(BaseModel):
    """通用响应结果结构 (来自 OpenAPI components/schemas/result)"""
    status: Literal["ok"] = Field(description="状态码，固定为 'ok'")
    retcode: float = Field(description="返回码")
    data: dict[str, Any] = Field(description="通用数据字段，可以是任意对象")
    message: str = Field(description="消息")
    wording: str = Field(description="提示语")
    echo: str | None = Field(description="Echo字段，可选")

    model_config = {
        "extra": "allow",
    }
# endregion component_models

# region req
class GetClientkeyReq(BaseModel):
    """获取clientkey请求模型"""
    pass

    model_config = {
        "extra": "allow",
    }
# endregion req


# region res
class GetClientkeyRes(Result):
    """获取clientkey响应模型"""
    class Data(BaseModel):
        """响应数据详情"""
        clientkey: str = Field(description="clientkey字段") # Required, so no default

        model_config = {
            "extra": "allow",
        }
    
    # Override the 'data' field from the base Result class
    data: Data = Field(description="获取clientkey特有的响应数据")

    model_config = {
        "extra": "allow",
    }
# endregion res

# region api
class GetClientkeyAPI(BaseModel):
    """get_clientkey接口数据模型"""
    endpoint: str = "get_clientkey"
    method: str = "POST"
    Req: type[BaseModel] = GetClientkeyReq
    Res: type[BaseModel] = GetClientkeyRes

# endregion api
# endregion code
