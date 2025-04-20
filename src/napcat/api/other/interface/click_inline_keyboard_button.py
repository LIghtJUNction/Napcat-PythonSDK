"""
点击行内键盘按钮 API
用于点击消息中的行内键盘按钮
接口地址: https://napcat.apifox.cn/227495408e0.md

参数：
- message_id: 消息ID
- button_id: 按钮ID

返回：
- 操作结果

# NapCat 开发中
"""

from napcat.api.base.types import BaseHttpResponse
from pydantic import BaseModel

class ClickInlineKeyboardButtonReq(BaseModel):
    """
    点击行内键盘按钮 API 请求参数
    """
    message_id: int  # 消息ID
    button_id: str   # 按钮ID

class ClickInlineKeyboardButtonRes(BaseHttpResponse[dict[str, bool]]):
    """
    点击行内键盘按钮 API 响应参数
    """
    pass