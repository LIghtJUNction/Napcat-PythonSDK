"""
设置群头像 API
用于设置群组的头像
接口地址: https://napcat.apifox.cn/226658669e0.md

参数:
- group_id: int - 群号
- file: str/bytes - 图片文件名或图片的二进制数据
- cache: int - 图片缓存时间，单位秒，默认为1

返回:
- 操作结果

# NapCat 开发中
"""

from typing import TypedDict
from napcat.api.base.models import BaseHttpResponse

class SetGroupPortraitReq(TypedDict, total=False):
    """
    设置群头像 API 请求参数
    """
    group_id: int           # 群号
    file: str | bytes # 图片文件名或图片的二进制数据
    cache: int              # 图片缓存时间，单位秒，默认为1

class SetGroupPortraitRes(BaseHttpResponse[dict[str, bool]]):
    """
    设置群头像 API 响应参数
    """
    pass