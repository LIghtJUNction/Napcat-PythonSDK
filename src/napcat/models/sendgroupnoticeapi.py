# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/226658740e0
@llms.txt: https://napcat.apifox.cn/226658740e0.md
@last_update: 2025-04-27 00:53:40

@description: 

summary:_发送群公告

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.43"
__endpoint__ = "_send_group_notice"
__id__ = "226658740e0"
__method__ = "POST"

# endregion METADATA


# region code
from pydantic import BaseModel, Field
from typing import Any
import logging

logger = logging.getLogger(__name__)

# region component_models
class number | string(BaseModel):
    id: str = Field(description="标识ID")
    name: str | None = Field(None, description="名称")

    model_config = {
        "extra": "allow",
    }

class group_id(BaseModel):
    id: str = Field(description="标识ID")
    name: str | None = Field(None, description="名称")

    model_config = {
        "extra": "allow",
    }

class result(BaseModel):
    status: str = Field(description="status字段")
    retcode: float = Field(description="retcode字段")
    data: dict[str, Any] = Field(description="data字段")
    message: str = Field(description="message字段")
    wording: str = Field(description="wording字段")
    echo: str | None = Field(description="echo字段")

    model_config = {
        "extra": "allow",
    }
# region component_models/

# region req
class SendGroupNoticeReq(BaseModel):
    """_发送群公告"""
    group_id: group_id
    content: str = Field(description="内容")
    image: str | None = Field(None, description="图片路径")
    pinned: number | None = Field(None)
    type: number | None = Field(None)
    confirm_required: number | None = Field(None)
    is_show_edit_card: number | None = Field(None)
    tip_window_type: number | None = Field(None)

    model_config = {
        "extra": "allow",
    }
# region req/


# region res
class SendGroupNoticeRes(BaseModel):
    """_发送群公告"""
    class Data(BaseModel):
        """响应数据类型"""
        yes: bool = Field(default=True, description="是否可用")
        reason: str | None = Field(default=None, description="原因")

        model_config = {
            "extra": "allow",
        }

    status: str = Field(default="ok", description="status字段")
    retcode: float = Field(default=0, description="retcode字段")
    data: Data = Field(default_factory=lambda: Data(), description="data字段")
    message: str = Field(default="", description="message字段")
    wording: str = Field(default="", description="wording字段")
    echo: str | None = Field(default=None, description="echo字段")

    model_config = {
        "extra": "allow",
    }
# region res/

# region api
class SendGroupNoticeAPI(BaseModel):
    """_send_group_notice接口数据模型"""
    endpoint: str = "_send_group_notice"
    method: str = "POST"
    Req: type[BaseModel] = SendGroupNoticeReq
    Res: type[BaseModel] = SendGroupNoticeRes

# region api/
# endregion code

