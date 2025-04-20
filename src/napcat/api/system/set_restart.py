"""
重启NapCat API
用于重启NapCat服务
接口地址: https://napcat.apifox.cn/227230510e0.md

参数：
无需参数

返回：
- 重启操作结果

# NapCat 开发中
"""

from typing import TypedDict
from napcat.api.base.types import BaseHttpResponse

class SetRestartReq(TypedDict):
    """
    重启NapCat API 请求参数
    """
    pass  # 无需参数

class SetRestartRes(BaseHttpResponse[dict[str, bool]]):
    """
    重启NapCat API 响应参数
    """
    pass