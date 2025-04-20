"""
获取收藏表情列表 API
用于获取用户收藏的表情列表
接口地址: https://napcat.apifox.cn/227495324e0.md

参数：
无需参数

返回：
- 收藏表情列表

# NapCat 开发中
"""

from pydantic import BaseModel
from napcat.api.base.models import BaseHttpResponse

class GetCollectionListReq(BaseModel):
    """
    获取收藏表情列表 API 请求参数
    """
    pass  # 无需参数

class CollectionItem(BaseModel):
    """
    收藏表情项
    """
    collection_id: str  # 收藏ID
    emoji_id: str       # 表情ID
    emoji_url: str      # 表情图片URL
    emoji_type: int     # 表情类型
    add_time: int       # 收藏时间

class GetCollectionListRes(BaseHttpResponse[list[CollectionItem]]):
    """
    获取收藏表情列表 API 响应参数
    """
    pass