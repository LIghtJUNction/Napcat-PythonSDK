# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: 其他/接口
@homepage: https://napcat.apifox.cn/266151864e0
@llms.txt: https://napcat.apifox.cn/266151864e0.md
@last_update: 2025-04-27 00:53:41

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
from typing import Literal # Import Literal for status="ok"



# region req
class ClickInlineKeyboardButtonReq(BaseModel):
    """
    请求模型
    """

    group_id: str | int = Field(..., description="群号")
    bot_appid: str = Field(..., description="机器人appid")
    button_id: str = Field(..., description="按钮id")
    callback_data: str = Field(..., description="按钮回调数据")
    msg_seq: str = Field(..., description="消息序列号")

# endregion req



# region res
class ClickInlineKeyboardButtonRes(BaseModel):
    """
    响应模型
    """

    class Data(BaseModel):
        """
        响应数据
        """
        # API spec shows an empty object for data
        pass

    status: Literal["ok"] = Field(..., description="状态")
    retcode: int = Field(..., description="返回码")
    data: Data = Field(..., description="响应数据")
    message: str = Field(..., description="消息")
    wording: str = Field(..., description="提示")
    echo: str | None = Field(..., description="Echo数据")

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
