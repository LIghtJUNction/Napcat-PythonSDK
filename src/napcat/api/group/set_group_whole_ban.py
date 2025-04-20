"""
群组全员禁言 API
用于设置群组全员禁言状态
接口地址: https://napcat.apifox.cn/227425666e0.md

参数：
- group_id: 群号
- enable: 是否开启全员禁言

返回：
- 操作结果

# NapCat 开发中
"""

from typing import TypedDict
from napcat.api.base.models import BaseHttpResponse
# region TypedDicts
class SetGroupWholeBanReq(TypedDict):
    """
    群组全员禁言 API 请求参数
    """
    group_id: int  # 群号
    enable: bool   # 是否开启全员禁言

class SetGroupWholeBanRes(BaseHttpResponse[dict[str, bool]]):
    """
    群组全员禁言 API 响应参数
    """
    pass