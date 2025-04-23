# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/266151864e0
@llms.txt: https://napcat.apifox.cn/266151864e0.md
@last_update: 2025-04-23 20:23:18

@description: 

summary:点击按钮

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "click_inline_keyboard_button"
__id__ = "266151864e0"
__method__ = "POST"

# region METADATA/


# region code
from typing import Any
from pydantic import BaseModel, Field
from typing import Union

# region req
class ClickInlineKeyboardButtonReq(BaseModel):
    """
    请求参数
    """

    group_id: float | str = Field(..., description="")
    bot_appid: str = Field(..., description="")
    button_id: str = Field(..., description="")
    callback_data: str = Field(..., description="")
    msg_seq: str = Field(..., description="")
# region req/


# region res
class ClickInlineKeyboardButtonRes(BaseModel):
    """
    响应参数
    """

    pass
# region res/

# region api
class ClickInlineKeyboardButtonAPI(BaseModel):
    
    Request : type[ClickInlineKeyboardButtonReq] = ClickInlineKeyboardButtonReq
    Response  : type[ClickInlineKeyboardButtonRes] = ClickInlineKeyboardButtonRes


# region api/
# region code/

