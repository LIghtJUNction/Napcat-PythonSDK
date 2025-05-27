# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/228534361e0
@llms.txt: https://napcat.apifox.cn/228534361e0.md
@last_update: 2025-05-28 01:34:11

@description: 

summary:检查链接安全性

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.43"
__endpoint__ = "check_url_safely"
__id__ = "228534361e0"
__method__ = "POST"

# endregion METADATA


# region code
from pydantic import BaseModel, Field
from typing import Literal
import logging

logger = logging.getLogger(__name__)

# region req
class CheckUrlSafelyReq(BaseModel):
    """检查链接安全性"""
    # No request parameters based on OpenAPI spec and original code

    model_config = {
        "extra": "allow",
    }
# region req/


# region res
class CheckUrlSafelyRes(BaseModel):
    """检查链接安全性"""
    class Data(BaseModel):
        """响应数据类型"""
        yes: bool = Field(default=True, description="是否可用")
        reason: str | None = Field(default=None, description="原因")

        model_config = {
            "extra": "allow",
        }

    status: Literal["ok"] = Field(default="ok", description="状态，如 'ok'")
    retcode: float = Field(default=0.0, description="返回码，0表示成功")
    data: Data = Field(default_factory=Data, description="响应数据")
    message: str = Field(default="", description="消息")
    wording: str = Field(default="", description="文字描述")
    echo: str | None = Field(default=None, description="回显内容")

    model_config = {
        "extra": "allow",
    }
# region res/

# region api
class CheckUrlSafelyAPI(BaseModel):
    """check_url_safely接口数据模型"""
    endpoint: str = "check_url_safely"
    method: str = "POST"
    Req: type[BaseModel] = CheckUrlSafelyReq
    Res: type[BaseModel] = CheckUrlSafelyRes

# region api/
# endregion code
