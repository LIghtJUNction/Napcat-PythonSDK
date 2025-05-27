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
from typing import Literal

# region component_models
class ResultData(BaseModel):
    """
    响应数据，根据OpenAPI定义，此为一个空对象。
    """
    model_config = {
        "extra": "allow",
    }

class Result(BaseModel):
    """
    API标准响应结果模型，对应OpenAPI `components/schemas/result`。
    """
    status: Literal["ok"] = Field(description="状态，固定为 'ok'")
    retcode: float = Field(description="返回码，0表示成功")
    data: ResultData = Field(description="响应数据对象")
    message: str = Field(description="消息")
    wording: str = Field(description="文字描述")
    echo: str | None = Field(description="回显内容，可能为空")

    model_config = {
        "extra": "allow",
    }
# region component_models/

# region req
class ClickInlineKeyboardButtonReq(BaseModel):
    """点击按钮请求体"""
    # 根据OpenAPI components/schemas/group_id 定义，group_id 可以是数字或字符串。
    group_id: str | int = Field(description="群组或频道ID，可以是数字或字符串")
    bot_appid: str = Field(description="机器人App ID")
    button_id: str = Field(description="按钮ID")
    callback_data: str = Field(description="回调数据")
    msg_seq: str = Field(description="消息序列号")

    model_config = {
        "extra": "allow",
    }
# region req/


# region res
class ClickInlineKeyboardButtonRes(Result):
    """
    点击按钮响应体。
    继承自Result模型，符合OpenAPI `responses.200` 定义。
    """
    pass
# region res/

# region api
class ClickInlineKeyboardButtonAPI(BaseModel):
    """click_inline_keyboard_button接口数据模型"""
    endpoint: Literal["click_inline_keyboard_button"] = Field(default="click_inline_keyboard_button", description="接口端点")
    method: Literal["POST"] = Field(default="POST", description="HTTP 方法")
    Req: type[BaseModel] = Field(default=ClickInlineKeyboardButtonReq, description="请求数据模型")
    Res: type[BaseModel] = Field(default=ClickInlineKeyboardButtonRes, description="响应数据模型")

# region api/
# endregion code
