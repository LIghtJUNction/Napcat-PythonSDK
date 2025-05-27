# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/226659254e0
@llms.txt: https://napcat.apifox.cn/226659254e0.md
@last_update: 2025-05-28 01:34:10

@description: 

summary:fetch_user_profile_like

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.43"
__endpoint__ = "fetch_user_profile_like"
__id__ = "226659254e0"
__method__ = "POST"

# endregion METADATA


# region code
from pydantic import BaseModel, Field
from typing import Any, Literal

# region component_models
# user_id 和 result 组件模型已根据 OpenAPI 规范合并到对应的请求/响应模型中
# region component_models/

# region req
class FetchUserProfileLikeReq(BaseModel):
    """fetch_user_profile_like 请求模型"""
    user_id: int | str = Field(..., description="用户ID，可以是数字或字符串")

    model_config = {
        "extra": "allow",
    }
# region req/


# region res
class FetchUserProfileLikeRes(BaseModel):
    """fetch_user_profile_like 响应模型"""
    status: Literal["ok"] = Field("ok", description="状态，固定为 'ok'")
    retcode: float = Field(0.0, description="返回码，0表示成功")
    data: dict[str, Any] = Field(default_factory=dict, description="响应数据，一个空对象")
    message: str = Field("", description="消息")
    wording: str = Field("", description="文字描述")
    echo: str | None = Field(None, description="回显内容，可能为空")

    model_config = {
        "extra": "allow",
    }
# region res/

# region api
class FetchUserProfileLikeAPI(BaseModel):
    """fetch_user_profile_like接口数据模型"""
    endpoint: str = "fetch_user_profile_like"
    method: str = "POST"
    Req: type[BaseModel] = FetchUserProfileLikeReq
    Res: type[BaseModel] = FetchUserProfileLikeRes

# region api/
# endregion code
