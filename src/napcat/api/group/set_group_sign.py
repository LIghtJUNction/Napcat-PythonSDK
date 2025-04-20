"""
群打卡 API
用于在群组中进行打卡操作
接口地址: https://napcat.apifox.cn/226659329e0.md 和 https://napcat.apifox.cn/230897177e0.md

参数:
- group_id: int - 群号

返回:
- 操作结果

# NapCat 开发中
"""

from typing import TypedDict
from napcat.api.base.models import BaseHttpResponse

class SetGroupSignReq(TypedDict):
    """
    群打卡 API 请求参数
    """
    group_id: int  # 群号

class SetGroupSignRes(BaseHttpResponse[dict[str, bool]]):
    """
    群打卡 API 响应参数
    """
    pass