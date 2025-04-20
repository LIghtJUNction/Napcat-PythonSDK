"""
设置自定义在线状态 API
用于设置QQ账号的自定义在线状态，支持设置自定义状态文本和表情
接口地址: https://napcat.apifox.cn/266151905e0.md

参数：
- face_id: 状态表情ID，用于显示特定表情图标
- status_text: 自定义状态文本内容
- duration: 状态持续时间(单位:秒)，设置为0表示永久生效

返回：
- 设置自定义在线状态的结果信息

# NapCat 开发中
"""

from pydantic import BaseModel
from napcat.api.base.models import BaseHttpResponse

class SetDiyOnlineStatusReq(BaseModel):
    """
    设置自定义在线状态 API 请求参数
    """
    face_id: int          # 状态表情ID
    status_text: str      # 自定义状态文本内容
    duration: int         # 状态持续时间(单位:秒)，0表示永久生效

class DiyStatusResult(BaseModel):
    """
    设置自定义在线状态的结果信息
    """
    success: bool         # 是否设置成功
    message: str          # 结果消息

class SetDiyOnlineStatusRes(BaseHttpResponse[DiyStatusResult]):
    """
    设置自定义在线状态 API 响应参数
    """
    pass