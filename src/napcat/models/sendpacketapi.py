# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/250286903e0
@llms.txt: https://napcat.apifox.cn/250286903e0.md
@last_update: 2025-04-27 00:53:41

@description: 

summary:发送自定义组包

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.43"
__endpoint__ = "send_packet"
__id__ = "250286903e0"
__method__ = "POST"

# endregion METADATA


# region code
from pydantic import BaseModel, Field
from typing import Any
import logging

logger = logging.getLogger(__name__)

# region req
class SendPacketReq(BaseModel):
    """发送自定义组包"""
    pass  # 没有请求参数

    model_config = {
        "extra": "allow",
    }
# region req/


# region res
class SendPacketRes(BaseModel):
    """发送自定义组包"""
    class Data(BaseModel):
        """响应数据类型"""
        yes: bool = Field(default=True, description="是否可用")
        reason: str | None = Field(default=None, description="原因")

        model_config = {
            "extra": "allow",
        }

    status: str = Field(default="ok", description="状态，如 'ok'")
    retcode: float = Field(default=0, description="返回码，0表示成功")
    data: Data = Field(default_factory=lambda: Data(), description="响应数据")
    message: str = Field(default="", description="消息")
    wording: str = Field(default="", description="文字描述")
    echo: str | None = Field(default=None, description="回显内容")

    model_config = {
        "extra": "allow",
    }
# region res/

# region api
class SendPacketAPI(BaseModel):
    """send_packet接口数据模型"""
    endpoint: str = "send_packet"
    method: str = "POST"
    Req: type[BaseModel] = SendPacketReq
    Res: type[BaseModel] = SendPacketRes

# region api/
# endregion code

