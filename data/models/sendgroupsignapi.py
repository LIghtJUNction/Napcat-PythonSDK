# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/230897177e0
@llms.txt: https://napcat.apifox.cn/230897177e0.md
@last_update: 2025-05-28 01:34:11

@description: 

summary:群打卡

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.43"
__endpoint__ = "send_group_sign"
__id__ = "230897177e0"
__method__ = "POST"

# endregion METADATA


# region code
from pydantic import BaseModel, Field
from typing import Any
import logging

logger = logging.getLogger(__name__)

# region req
class SendGroupSignReq(BaseModel):
    """群打卡"""
    group_id: str

    model_config = {
        "extra": "allow",
    }
# region req/


# region res
class SendGroupSignRes(BaseModel):
    """群打卡"""
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
class SendGroupSignAPI(BaseModel):
    """send_group_sign接口数据模型"""
    endpoint: str = "send_group_sign"
    method: str = "POST"
    Req: type[BaseModel] = SendGroupSignReq
    Res: type[BaseModel] = SendGroupSignRes

# region api/
# endregion code

