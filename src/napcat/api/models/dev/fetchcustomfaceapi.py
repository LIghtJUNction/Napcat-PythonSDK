# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/226659210e0
@llms.txt: https://napcat.apifox.cn/226659210e0.md
@last_update: 2025-05-28 01:34:10

@description: 

summary:获取收藏表情

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.43"
__endpoint__ = "fetch_custom_face"
__id__ = "226659210e0"
__method__ = "POST"

# endregion METADATA


# region code
from pydantic import BaseModel, Field
from typing import Any, Literal

# region component_models
class result(BaseModel):
    status: Literal["ok"] = Field(default="ok", description="状态码，固定为ok")
    retcode: float = Field(description="返回码")
    data: dict[str, Any] = Field(default_factory=dict, description="数据字段")
    message: str = Field(description="消息")
    wording: str = Field(description="说明")
    echo: str | None = Field(default=None, description="echo字段")

    model_config = {
        "extra": "allow",
    }
# region component_models/

# region req
class FetchCustomFaceReq(BaseModel):
    """获取收藏表情请求"""
    count: float = Field(default=48, description="获取表情的数量，默认48")

    model_config = {
        "extra": "allow",
    }
# region req/


# region res
class FetchCustomFaceRes(BaseModel):
    """获取收藏表情响应"""
    status: Literal["ok"] = Field(default="ok", description="状态码，固定为ok")
    retcode: float = Field(default=0, description="返回码")
    data: list[str] = Field(default_factory=list, description="收藏表情列表")
    message: str = Field(default="", description="消息")
    wording: str = Field(default="", description="说明")
    echo: str | None = Field(default=None, description="echo字段")

    model_config = {
        "extra": "allow",
    }
# region res/

# region api
class FetchCustomFaceAPI(BaseModel):
    """fetch_custom_face接口数据模型"""
    endpoint: str = "fetch_custom_face"
    method: str = "POST"
    Req: type[BaseModel] = FetchCustomFaceReq
    Res: type[BaseModel] = FetchCustomFaceRes

# region api/
# endregion code