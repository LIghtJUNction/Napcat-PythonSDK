"""
获取用户个性签名点赞数 API
用于获取用户个人资料中的点赞数
接口地址: https://napcat.apifox.cn/227495305e0.md

参数：
- user_id: 用户QQ号

返回：
- 用户个性签名点赞信息

# NapCat 开发中
"""

from pydantic import BaseModel
from napcat.api.base.models import BaseHttpResponse

class FetchUserProfileLikeReq(BaseModel):
    """
    获取用户个性签名点赞数 API 请求参数
    """
    user_id: int  # 用户QQ号

class ProfileLikeInfo(BaseModel):
    """
    个性签名点赞信息
    """
    user_id: int     # 用户QQ号
    like_count: int  # 点赞数量
    is_liked: bool   # 当前账号是否已点赞

class FetchUserProfileLikeRes(BaseHttpResponse[ProfileLikeInfo]):
    """
    获取用户个性签名点赞数 API 响应参数
    """
    pass