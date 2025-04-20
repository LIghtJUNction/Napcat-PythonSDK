"""
设置头像 API
用于设置当前登录QQ账号的头像
接口地址: https://napcat.apifox.cn/226658980e0.md

参数：
- file: 图片文件路径或图片的二进制数据
- cache: 是否使用缓存(可选)

返回：
- 设置头像的结果信息，包含是否设置成功的状态

# NapCat 开发中
"""

from typing import TypedDict, BinaryIO
from pathlib import Path
from napcat.api.base.models import BaseHttpResponse

class SetQQAvatarReq(TypedDict):
    """
    设置头像 API 请求参数
    """
    file: str | Path | bytes | BinaryIO  # 图片文件路径或二进制数据
    cache: bool | None                    # 是否使用缓存(可选)

class AvatarResult(TypedDict):
    """
    设置头像的结果信息
    """
    success: bool                            # 是否设置成功
    message: str                             # 结果消息

class SetQQAvatarRes(BaseHttpResponse[AvatarResult]):
    """
    设置头像 API 响应参数
    """
    pass