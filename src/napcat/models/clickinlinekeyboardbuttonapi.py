# -*- coding: utf-8 -*-
# region METADATA
"""
@author: LIghtJUNction

@api_id: 266151864e0
@endpoint: click_inline_keyboard_button
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/266151864e0
@llms.txt: https://napcat.apifox.cn/266151864e0.md
@version: 4.7.17
@last_update: 2025-04-23 20:09:55

@description: 

summary:点击按钮

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "click_inline_keyboard_button"
__method__ = "POST"

# region METADATA/


# region code
from typing import Any , Literal

from pydantic import BaseModel, Field

# region req
class ClickInlineKeyboardButtonReq(BaseModel): # type: ignore
    """
    {{DESC_EndPointReq}}
    """

    pass
# region req/



# region res
class ClickInlineKeyboardButtonRes(BaseModel): # type: ignore
    # 定义响应参数
    # 例如：
    # param1: str = Field(..., description="参数1的描述")
    # param2: int = Field(..., description="参数2的描述")
    
    pass
# region res/

# region api
class ClickInlineKeyboardButtonAPI(BaseModel):
    
    Request : type[ClickInlineKeyboardButtonReq] = ClickInlineKeyboardButtonReq
    Response  : type[ClickInlineKeyboardButtonRes] = ClickInlineKeyboardButtonRes


# region api/




# region code/

