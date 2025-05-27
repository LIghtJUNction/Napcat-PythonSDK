# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/226659074e0
@llms.txt: https://napcat.apifox.cn/226659074e0.md
@last_update: 2025-05-28 01:34:09

@description: 

summary:消息转发到群

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.43"
__endpoint__ = "forward_group_single_msg"
__id__ = "226659074e0"
__method__ = "POST"

# endregion METADATA


# region code
from pydantic import BaseModel, Field
from typing import Literal
import logging

logger = logging.getLogger(__name__)

# region component_models
# message_id and group_id component models were removed as per OpenAPI spec they are scalar types (str | int)
# result component model was removed as its definition was inconsistent with the specific response schema's data field
# endregion component_models/

# region req
class ForwardGroupSingleMsgReq(BaseModel):
    """消息转发到群"""
    group_id: str | int = Field(..., description="群组ID，可以是字符串或整数")
    message_id: str | int = Field(..., description="消息ID，可以是字符串或整数")

    model_config = {
        "extra": "allow",
    }
# endregion req/


# region res
class ForwardGroupSingleMsgRes(BaseModel):
    """消息转发到群"""
    status: Literal["ok"] = Field("ok", description="status字段，固定为'ok'")
    retcode: float = Field(0.0, description="retcode字段")
    data: None = Field(None, description="data字段，此API响应中固定为null")
    message: str = Field("", description="message字段")
    wording: str = Field("", description="wording字段")
    echo: str | None = Field(None, description="echo字段")

    model_config = {
        "extra": "allow",
    }
# endregion res/

# region api
class ForwardGroupSingleMsgAPI(BaseModel):
    """forward_group_single_msg接口数据模型"""
    endpoint: str = "forward_group_single_msg"
    method: str = "POST"
    Req: type[BaseModel] = ForwardGroupSingleMsgReq
    Res: type[BaseModel] = ForwardGroupSingleMsgRes

# endregion api/
# endregion code
