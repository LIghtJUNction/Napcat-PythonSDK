"""
获取自定义表情 API
用于获取用户上传的自定义表情列表
接口地址: https://napcat.apifox.cn/227233981e0.md

参数：
- type: 表情类型 (all/image/face)
- page: 分页页码

返回：
- 表情列表及元数据
"""

from pydantic import BaseModel
from napcat.api.base.models import BaseHttpResponse

class FetchCustomFaceReq(BaseModel):
    """
    获取自定义表情 API 请求参数
    """
    type: str  # 表情类型
    page: int  # 分页页码

class CustomFaceItem(BaseModel):
    """
    自定义表情项
    """
    id: str         # 表情ID
    name: str       # 表情名称
    url: str        # 表情URL
    width: int      # 表情宽度
    height: int     # 表情高度

class FetchCustomFaceRes(BaseHttpResponse[list[CustomFaceItem]]):
    """
    获取自定义表情 API 响应参数
    """
    total: int      # 总数量
    page_size: int  # 每页数量
