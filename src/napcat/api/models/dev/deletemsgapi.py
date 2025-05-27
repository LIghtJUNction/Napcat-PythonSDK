# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: 消息相关
@homepage: https://napcat.apifox.cn/226919954e0
@llms.txt: https://napcat.apifox.cn/226919954e0.md
@last_update: 2025-05-28 01:34:10

@description:

summary:撤回消息

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.43"
__endpoint__ = "delete_msg"
__id__ = "226919954e0"
__method__ = "POST"

# endregion METADATA


# region code
from pydantic import BaseModel, Field
from typing import Literal

# region component_models
# The original message_id and result classes are removed based on OpenAPI spec interpretation.
# message_id is a union type in req, result structure is directly in res.
# endregion component_models/

# region req
class DeleteMsgReq(BaseModel):
    """撤回消息请求模型"""
    # OpenAPI spec: message_id can be number or string
    message_id: str | int = Field(description="标识ID")

    model_config = {
        "extra": "allow",
    }
# endregion req/


# region res
class DeleteMsgRes(BaseModel):
    """撤回消息响应模型"""
    status: Literal["ok"] = Field("ok", description="状态字段")
    retcode: float = Field(description="返回码")
    data: None = Field(None, description="数据字段，此接口返回null")
    message: str = Field(description="消息")
    wording: str = Field(description="提示词")
    echo: str | None = Field(None, description="回显")

    model_config = {
        "extra": "allow",
    }
# endregion res/

# region api
class DeleteMsgAPI(BaseModel):
    """delete_msg接口数据模型"""
    endpoint: str = "delete_msg"
    method: str = "POST"
    Req: type[BaseModel] = DeleteMsgReq
    Res: type[BaseModel] = DeleteMsgRes

# endregion api/
# endregion code
