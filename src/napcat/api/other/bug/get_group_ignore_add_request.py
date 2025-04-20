"""
获取被过滤的加群请求 API
用于获取被系统自动过滤的加群请求列表
接口地址: https://napcat.apifox.cn/226659234e0.md

参数：
无需参数

返回：
- 包含被过滤的加群请求列表，包括请求者信息、群信息、过滤原因等

注意：
- 此API目前标记为bug状态，可能存在稳定性或功能问题
- 仅群主和管理员可以查看被过滤的加群请求
- 过滤的请求可能已经过期，无法再进行操作

# NapCat 开发中
"""

"""
获取群邀请自动处理状态 API
用于获取群邀请的自动处理状态
接口地址: https://napcat.apifox.cn/227495352e0.md

参数：
无需参数

返回：
- 群邀请自动处理状态

# NapCat 开发中
"""

from pydantic import BaseModel
from napcat.api.base.models import BaseHttpResponse

class GetGroupIgnoreAddRequestReq(BaseModel):
    """
    获取群邀请自动处理状态 API 请求参数
    """
    pass  # 无需参数

class IgnoreStatus(BaseModel):
    """
    群邀请自动处理状态
    """
    status: bool  # 是否启用自动忽略
    list: list[int]  # 自动忽略的群号列表

class GetGroupIgnoreAddRequestRes(BaseHttpResponse[IgnoreStatus]):
    """
    获取群邀请自动处理状态 API 响应参数
    """
    pass