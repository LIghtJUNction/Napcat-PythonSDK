"""
设置消息表情回应 API
用于对消息设置表情回应
接口地址: https://napcat.apifox.cn/227229079e0.md

参数：
- message_id: 消息ID
- emoji_id: 表情ID
- action: 动作，add为添加，delete为删除

返回：
- 操作结果

# NapCat 开发中
"""

from typing import Literal
from pydantic import BaseModel
from napcat.api.base.models import BaseHttpResponse

class SetMsgEmojiLikeReq(BaseModel):
    """
    设置消息表情回应 API 请求参数
    """
    message_id: int  # 消息ID
    emoji_id: str    # 表情ID
    action: Literal["add", "delete"]  # 动作，add为添加，delete为删除

class SetMsgEmojiLikeRes(BaseHttpResponse[dict[str, bool]]):
    """
    设置消息表情回应 API 响应参数
    """
    pass