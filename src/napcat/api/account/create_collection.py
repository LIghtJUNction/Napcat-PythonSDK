"""
创建收藏 API
用于在QQ收藏夹中创建新的收藏内容
接口地址: https://napcat.apifox.cn/226659190e0.md

参数：
- message_id: 要收藏的消息ID，收藏指定消息内容
- content: 收藏的自定义内容，与message_id二选一

返回：
- 创建收藏的结果信息

# NapCat 开发中
"""

from typing import TypedDict
from napcat.api.base.models import BaseHttpResponse
# region TypedDicts
class CreateCollectionReq(TypedDict, total=False):
    """创建收藏的请求参数，message_id和content二选一"""
    message_id: int  # 要收藏的消息ID
    content: str     # 收藏的自定义内容

class CollectionData(TypedDict):
    """收藏数据"""
    collection_id: str  # 创建的收藏ID

class CreateCollectionRes(BaseHttpResponse[CollectionData]):
    """创建收藏的响应结果"""
    pass