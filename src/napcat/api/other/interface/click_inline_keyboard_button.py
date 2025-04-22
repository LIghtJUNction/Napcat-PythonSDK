# -*- coding: utf-8 -*-
"""
@author: LIghtJUNction
@builder: AI

@build_id: 214
@api_id: 266151864e0
@endpoint: click_inline_keyboard_button
@tags: 其他/接口
@homepage: https://napcat.apifox.cn/266151864e0
@llms.txt: https://napcat.apifox.cn/266151864e0.md
@version: 4.7.17
@last_update: 2025-04-23 04:39:51

@description: click_inline_keyboard_button API
@usage: 使用 `client.click_inline_keyboard_button()` 调用此API

"""
# region METADATA

__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "click_inline_keyboard_button"
__method__ = "POST"


# region code
from typing import Literal, Any

from pydantic import BaseModel, Field
from napcat.base.models import BaseHttpAPI, BaseHttpResponse, BaseHttpRequest



# region req
class ClickInlineKeyboardButtonReq(BaseHttpRequest):
    """
    click_inline_keyboard_button 请求参数
    """

    pass
# region req/

# region data
class ClickInlineKeyboardButtonData(BaseModel):
    """
    click_inline_keyboard_button 数据结构
    """
    # 定义可选数据字段
    # 例如：
    # param1: str = Field(..., description="参数1的描述")
    # param2: int = Field(..., description="参数2的描述")
    
    pass
# region data/

# region res
class ClickInlineKeyboardButtonRes(BaseHttpResponse[ClickInlineKeyboardButtonData]):
    """
    click_inline_keyboard_button 响应参数
    """
    # 定义响应参数
    # 例如：
    # param1: str = Field(..., description="参数1的描述")
    # param2: int = Field(..., description="参数2的描述")
    
    pass
# region res/

# region api
class ClickInlineKeyboardButtonAPI(BaseHttpAPI[ClickInlineKeyboardButtonReq, ClickInlineKeyboardButtonRes]):
    """
    点击按钮
    """
    api: str = "/click_inline_keyboard_button"
    method: Literal["POST", "GET"] = "POST"

    Request = ClickInlineKeyboardButtonReq
    Response = ClickInlineKeyboardButtonRes

    request: ClickInlineKeyboardButtonReq
    response: ClickInlineKeyboardButtonRes
# region api/


if __name__ == "__main__":

    from napcat.base.utils import test_model
    test_model(ClickInlineKeyboardButtonAPI)

# region code/

