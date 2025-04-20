"""
发送戳一戳 API
用于向指定好友或群成员发送戳一戳(窗口抖动)消息
接口地址: https://napcat.apifox.cn/250286923e0.md

参数：
- user_id: 接收戳一戳的用户QQ号
- group_id: 群号(可选，如果在群内戳一戳则需要提供)
- poke_type: 戳一戳类型ID
- poke_id: 具体戳一戳表情的ID
- strength: 戳一戳强度(可选)

返回：
- 发送戳一戳的结果状态信息

# NapCat 开发中
"""

from pydantic import BaseModel
from napcat.api.base.models import BaseHttpResponse

class SendPokeReq(BaseModel):
    """
    发送戳一戳 API 请求参数
    """
    user_id: int                # 接收戳一戳的用户QQ号
    poke_type: int              # 戳一戳类型ID
    poke_id: int                # 具体戳一戳表情的ID
    group_id: int | None = None     # 群号(可选)
    strength: int | None = None     # 戳一戳强度(可选)

class PokeResult(BaseModel):
    """
    发送戳一戳的结果状态信息
    """
    success: bool               # 是否发送成功
    message: str                # 结果消息

class SendPokeRes(BaseHttpResponse[PokeResult]):
    """
    发送戳一戳 API 响应参数
    """
    pass