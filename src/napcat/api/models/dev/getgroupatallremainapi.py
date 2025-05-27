# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/227245941e0
@llms.txt: https://napcat.apifox.cn/227245941e0.md
@last_update: 2025-05-28 01:34:11

@description: 

summary:获取群 @全体成员 剩余次数

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.43"
__endpoint__ = "get_group_at_all_remain"
__id__ = "227245941e0"
__method__ = "POST"

# endregion METADATA


# region code
from pydantic import BaseModel, Field
from typing import Literal

# region component_models
# group_id component model is removed as per OpenAPI specification, it's a scalar type (str | int).
# result component model is removed as GetGroupAtAllRemainRes explicitly defines its response structure.
# endregion component_models/

# region req
class GetGroupAtAllRemainReq(BaseModel):
    """获取群 @全体成员 剩余次数"""
    group_id: str | int = Field(description="群号，可以是字符串或数字类型") # Type adjusted based on OpenAPI 'oneOf' for group_id

    model_config = {
        "extra": "allow",
    }
# endregion req/


# region res
class GetGroupAtAllRemainRes(BaseModel):
    """获取群 @全体成员 剩余次数"""
    class Data(BaseModel):
        """响应数据类型"""
        can_at_all: bool = Field(description="是否可以 @全体成员") # Required field, removed default=None
        remain_at_all_count_for_group: float = Field(description="群剩余 @全体成员 次数") # Required field, removed default=None
        remain_at_all_count_for_uin: float = Field(description="用户剩余 @全体成员 次数") # Required field, removed default=None

        model_config = {
            "extra": "allow",
        }

    status: Literal["ok"] = Field("ok", description="状态码，固定为 'ok'") # Changed to Literal["ok"]
    retcode: float = Field(0, description="返回码")
    data: Data = Field(default_factory=Data, description="响应数据") # Using default_factory for nested model
    message: str = Field("", description="消息")
    wording: str = Field("", description="提示信息")
    echo: str | None = Field(None, description="回显信息")

    model_config = {
        "extra": "allow",
    }
# endregion res/

# region api
class GetGroupAtAllRemainAPI(BaseModel):
    """get_group_at_all_remain接口数据模型"""
    endpoint: str = "get_group_at_all_remain"
    method: str = "POST"
    Req: type[BaseModel] = GetGroupAtAllRemainReq
    Res: type[BaseModel] = GetGroupAtAllRemainRes

# endregion api/
# endregion code
