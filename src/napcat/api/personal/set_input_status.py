"""
设置输入状态 API
用于设置当前用户的输入状态，例如正在输入等
接口地址: https://napcat.apifox.cn/243539842e0.md

参数：
- target_id: 目标ID，好友QQ号或群号
- target_type: 目标类型，"private"表示私聊，"group"表示群聊
- status_type: 状态类型，如"typing"表示正在输入
- duration: 状态持续时间(毫秒)，可选参数

返回：
- 设置结果，表明操作是否成功

注意：
- 输入状态是临时的，会在一定时间后自动取消
- 状态类型可能因目标类型不同而有所差异
- 部分状态可能需要特定的权限才能设置

# NapCat 开发中
"""

from typing import Literal
from pydantic import BaseModel, Field
from napcat.api.base.models import BaseHttpResponse

class SetInputStatusReq(BaseModel):
    """
    设置输入状态 API 请求参数
    """
    target_id: int                                # 目标ID，如好友QQ号或群号
    target_type: Literal["private", "group"]      # 目标类型，"private"表示私聊，"group"表示群聊
    status_type: Literal["typing", "recording", "sending_file", "custom"]  # 状态类型
    duration: int | None = None                                 # 状态持续时间(毫秒)，可选
    custom_status: str | None = Field(default=None)                            # 自定义状态文本，当status_type为"custom"时使用

class StatusResult(BaseModel):
    """
    状态设置结果
    """
    success: bool      # 是否设置成功
    message: str       # 结果消息
    expires_at: int    # 状态过期时间戳(毫秒)

class SetInputStatusRes(BaseHttpResponse[StatusResult]):
    """
    设置输入状态 API 响应参数
    """
    pass