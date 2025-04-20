"""
设置群备注 API
用于设置群组的备注信息
接口地址: https://napcat.apifox.cn/283136268e0.md

参数:
- group_id: int - 群号
- remark: str - 备注信息

返回:
- 设置群备注的结果

# NapCat 开发中
"""

from typing import TypedDict
from napcat.api.base.models import BaseHttpResponse

class SetGroupRemarkReq(TypedDict):
    """
    设置群备注 API 请求参数
    """
    group_id: int  # 群号
    remark: str    # 备注信息

class SetGroupRemarkRes(BaseHttpResponse[dict[str, bool]]):
    """
    设置群备注 API 响应参数
    """
    pass