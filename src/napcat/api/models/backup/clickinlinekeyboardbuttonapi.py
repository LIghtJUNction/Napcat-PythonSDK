# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: 其他/接口
@homepage: https://napcat.apifox.cn/266151864e0
@llms.txt: https://napcat.apifox.cn/266151864e0.md
@last_update: 2025-04-26 01:17:45

@description: 

summary:点击按钮

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "click_inline_keyboard_button"
__id__ = "266151864e0"
__method__ = "POST"

# endregion METADATA


# region code
import logging
from pydantic import BaseModel, Field
from typing import Literal

logger = logging.getLogger(__name__)

# region req
class ClickInlineKeyboardButtonReq(BaseModel):
    """
    点击按钮请求模型
    """
    group_id: int | str = Field(..., description="群ID")
    bot_appid: str = Field(..., description="机器人appid")
    button_id: str = Field(..., description="按钮id")
    callback_data: str = Field(..., description="按钮回调数据")
    msg_seq: str = Field(..., description="消息序列号")
# endregion req



# region res
class ClickInlineKeyboardButtonRes(BaseModel):
    """
    点击按钮响应模型
    """
    status: Literal['ok'] = Field(..., description="状态，固定为 'ok'")
    retcode: int = Field(..., description="返回码")
    data: dict = Field(..., description="响应数据体 (空对象)") # OpenAPI specified an empty object
    message: str = Field(..., description="消息")
    wording: str = Field(..., description="描述")
    echo: str | None = Field(..., description="echo，可能为null")
# endregion res

# region api
class ClickInlineKeyboardButtonAPI(BaseModel):
    """click_inline_keyboard_button接口数据模型"""
    endpoint: str = "click_inline_keyboard_button"
    method: str = "POST"
    Req: type[BaseModel] = ClickInlineKeyboardButtonReq
    Res: type[BaseModel] = ClickInlineKeyboardButtonRes
# endregion api




# endregion code
