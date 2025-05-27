# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/226657080e0
@llms.txt: https://napcat.apifox.cn/226657080e0.md
@last_update: 2025-05-28 01:34:09

@description: 

summary:检查是否可以发送语音

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.43"
__endpoint__ = "can_send_record"
__id__ = "226657080e0"
__method__ = "POST"

# endregion METADATA


# region code
from pydantic import BaseModel, Field
from typing import Literal, Any

# region component_models
class result(BaseModel):
    status: Literal["ok"] = Field("ok", description="status字段")
    retcode: float = Field(0.0, description="retcode字段")
    data: dict[str, Any] = Field({}, description="data字段")
    message: str = Field("", description="message字段")
    wording: str = Field("", description="wording字段")
    echo: str | None = Field(None, description="echo字段")

    model_config = {
        "extra": "allow",
    }
# region component_models/

# region req
class CanSendRecordReq(BaseModel):
    """检查是否可以发送语音"""
    pass  # 没有请求参数

    model_config = {
        "extra": "allow",
    }
# region req/


# region res
class CanSendRecordRes(BaseModel):
    """检查是否可以发送语音"""
    class Data(BaseModel):
        """响应数据类型"""
        yes: bool = Field(False, description="yes字段")

        model_config = {
            "extra": "allow",
        }

    status: Literal["ok"] = Field("ok", description="status字段")
    retcode: float = Field(0.0, description="retcode字段")
    data: Data = Field(default_factory=Data, description="data字段")
    message: str = Field("", description="message字段")
    wording: str = Field("", description="wording字段")
    echo: str | None = Field(None, description="echo字段")

    model_config = {
        "extra": "allow",
    }
# region res/

# region api
class CanSendRecordAPI(BaseModel):
    """can_send_record接口数据模型"""
    endpoint: str = "can_send_record"
    method: str = "POST"
    Req: type[BaseModel] = CanSendRecordReq
    Res: type[BaseModel] = CanSendRecordRes

# region api/
# endregion code
