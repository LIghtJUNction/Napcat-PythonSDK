"""
获取表情回应列表 API
用于获取某条消息的表情回应列表
接口地址: https://napcat.apifox.cn/227229046e0.md

参数：
- message_id: 消息ID

返回：
- 表情回应列表

# NapCat 开发中
"""

from pydantic import BaseModel
from napcat.api.base.models import BaseHttpResponse

class FetchEmojiLikeReq(BaseModel):
    """
    获取表情回应列表 API 请求参数
    """
    message_id: int  # 消息ID

class EmojiInfo(BaseModel):
    """
    表情信息
    """
    emoji_id: str  # 表情ID
    count: int     # 回应数量

class EmojiUserInfo(BaseModel):
    """
    表情回应用户信息
    """
    emoji_id: str  # 表情ID
    user_id: int   # 用户QQ号
    timestamp: int # 回应时间戳

class EmojiLikeData(BaseModel):
    """
    表情回应数据
    """
    message_id: int              # 消息ID
    emoji_stats: list[EmojiInfo] # 各表情回应统计
    reactions: list[EmojiUserInfo] # 具体回应用户列表

class FetchEmojiLikeRes(BaseHttpResponse[EmojiLikeData]):
    """
    获取表情回应列表 API 响应参数
    """
    pass