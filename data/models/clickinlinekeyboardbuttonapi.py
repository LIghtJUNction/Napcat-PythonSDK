# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/266151864e0
@llms.txt: https://napcat.apifox.cn/266151864e0.md
@last_update: 2025-05-28 01:34:11

@description: 

summary:点击按钮

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.43"
__endpoint__ = "click_inline_keyboard_button"
__id__ = "266151864e0"
__method__ = "POST"

# endregion METADATA


# region code
from pydantic import BaseModel, Field
from typing import Any
import logging

logger = logging.getLogger(__name__)

# region component_models
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
class ClickInlineKeyboardButtonReq(BaseModel):
    """点击按钮"""
    group_id: group_id
    bot_appid: str
    button_id: str
    callback_data: str
    msg_seq: str

    model_config = {
        "extra": "allow",
    }
# region req/


# region res
class ClickInlineKeyboardButtonRes(BaseModel):
    """点击按钮"""
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
class ClickInlineKeyboardButtonAPI(BaseModel):
    """click_inline_keyboard_button接口数据模型"""
    endpoint: str = "click_inline_keyboard_button"
    method: str = "POST"
    Req: type[BaseModel] = ClickInlineKeyboardButtonReq
    Res: type[BaseModel] = ClickInlineKeyboardButtonRes

# region api/
# endregion code

