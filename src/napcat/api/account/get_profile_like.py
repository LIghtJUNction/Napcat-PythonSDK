"""
获取点赞列表 API
用于获取当天收到的点赞信息列表
接口地址: https://napcat.apifox.cn/226659197e0.md

参数：
无需参数

返回：
- 当天收到的点赞列表数据，包含点赞者QQ号、点赞时间和点赞次数等信息

# NapCat 开发中
"""

from pydantic import BaseModel
from napcat.api.base.models import BaseHttpResponse

class GetProfileLikeReq(BaseModel):
    """
    获取点赞列表 API 请求参数
    """
    pass  # 无需参数

class LikeInfo(BaseModel):
    """
    点赞信息结构
    """
    user_id: int    # 点赞者QQ号
    time: int       # 点赞时间戳
    count: int      # 点赞次数

class GetProfileLikeRes(BaseHttpResponse[list[LikeInfo]]):
    """
    获取点赞列表 API 响应参数
    """
    pass