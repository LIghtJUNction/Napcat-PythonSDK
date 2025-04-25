# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/266151864e0
@llms.txt: https://napcat.apifox.cn/266151864e0.md
@last_update: 2025-04-25 23:00:50

@description: 点击按钮

summary:点击按钮

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "click_inline_keyboard_button"
__id__ = "266151864e0"
__method__ = "POST"

# region METADATA/

from pydantic import BaseModel, Field
from typing import Any
import logging

logger = logging.getLogger(__name__)

# region component_models
class GroupId(BaseModel):
    group_id: int | str = Field(description="标识ID")

    model_config = {
        "extra": "allow",
    }


class Result(BaseModel):
    status: str = Field(default="ok", description="状态，如 'ok'")
    retcode: float = Field(default=0.0, description="返回码，0表示成功")
    data: dict[str, Any] = Field(default={}, description="数据")
    message: str = Field(default="", description="消息")
    wording: str = Field(default="", description="文字描述")
    echo: str | None = Field(default=None, description="回显内容")

    model_config = {
        "extra": "allow",
    }


# region component_models/

# region req
class ClickInlineKeyboardButtonReq(BaseModel):
    """点击按钮请求参数"""
    group_id: GroupId = Field(description="群组ID")
    bot_appid: str = Field(description="机器人APPID")
    button_id: str = Field(description="按钮ID")
    callback_data: str = Field(description="回调数据")
    msg_seq: str = Field(description="消息序列号")

    model_config = {
        "extra": "allow",
    }


# region req/

# region res
# class ClickInlineKeyboardButtonRes(BaseModel):
#     """点击按钮响应"""
#     class ResponseData(BaseModel):
#         """响应数据类型"""
#         yes: bool = Field(default=True, description="是否可用")
#         reason: str | None = Field(default=None, description="原因")
#
#         model_config = {
#             "extra": "allow",
#         }
#
#     status: str = Field(default="ok", description="状态，如 'ok'")
#     retcode: float = Field(default=0, description="返回码，0表示成功")
#     data: ResponseData = Field(default_factory=lambda: ResponseData(), description="响应数据")
#     message: str = Field(default="", description="消息")
#     wording: str = Field(default="", description="文字描述")
#     echo: str | None = Field(default=None, description="回显内容")
#
#     model_config = {
#         "extra": "allow",
#     }
# region res/

# region api
# class ClickInlineKeyboardButtonAPI(BaseModel):
#     """click_inline_keyboard_button接口数据模型"""
#     endpoint: str = "click_inline_keyboard_button"
#     method: str = "POST"
#     Req: type[BaseModel] = ClickInlineKeyboardButtonReq
#     Res: type[BaseModel] = ClickInlineKeyboardButtonRes
#     logger = logging.getLogger(__name__)
#
#     def __init__(self) -> None:
#         super().__init__()
#         self.logger.debug("初始化 ClickInlineKeyboardButtonAPI")
#
#     def __call__(self, req: ClickInlineKeyboardButtonReq) -> ClickInlineKeyboardButtonRes:
#         """
#         调用API的方法（仅作为接口定义，不包含实际请求逻辑）
#
#         Args:
#             req: 请求参数对象
#
#         Returns:
#             响应对象
#         """
#         # 调试日志
#         self.logger.debug(f"调用 ClickInlineKeyboardButtonAPI API")
#         self.logger.debug(f"请求参数: {req.model_dump_json()}")
#
#         # 注意：这里不应该包含实际的请求逻辑
#         # 这个方法只是定义了接口，实际的请求应由适配器或客户端实现
#         raise NotImplementedError("此方法需要由实际的API客户端实现")

# region api/
# region code/