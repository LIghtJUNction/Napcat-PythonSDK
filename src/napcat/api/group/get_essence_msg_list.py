"""
获取精华消息列表 API
用于获取群精华消息列表
接口地址: https://napcat.apifox.cn/227425361e0.md

参数：
- group_id: 群号

返回：
- 精华消息列表信息

# NapCat 开发中
"""

from typing import TypedDict
from napcat.api.base.models import BaseHttpResponse
# region TypedDicts
class GetEssenceMsgListReq(TypedDict):
    """
    获取精华消息列表 API 请求参数
    """
    group_id: int  # 群号

class EssenceMessage(TypedDict):
    """
    精华消息信息
    """
    sender_id: int     # 发送者QQ号
    sender_nick: str   # 发送者昵称
    sender_time: int   # 发送时间
    operator_id: int   # 操作者QQ号
    operator_nick: str # 操作者昵称
    operator_time: int # 精华设置时间
    message_id: int    # 消息ID
    content: str       # 消息内容

class GetEssenceMsgListRes(BaseHttpResponse[list[EssenceMessage]]):
    """
    获取精华消息列表 API 响应参数
    """
    pass