"""
获取推荐好友/群聊卡片 API
用于获取系统推荐的好友和群聊卡片信息，展示给用户作为添加建议
接口地址: https://napcat.apifox.cn/226658965e0.md

参数：
- category_id: 推荐的类别ID

返回：
- 包含推荐好友和群聊卡片信息的列表

# NapCat 开发中
"""

"""
分享私聊小程序卡片 API
用于分享小程序卡片到指定私聊
接口地址: https://napcat.apifox.cn/250287112e0.md

参数：
- app_id: 小程序ID
- user_id: 目标用户QQ号
- title: 卡片标题
- content: 卡片内容
- image: 卡片图片URL
- url: 小程序跳转链接

返回：
- 分享结果信息

# NapCat 开发中
"""

from typing import TypedDict
from python_napcat.api.base.types import BaseHttpResponse

class ArkSharePeerReq(TypedDict):
    """分享私聊小程序卡片的请求参数"""
    app_id: str
    user_id: int
    title: str
    content: str
    image: str
    url: str

class ArkSharePeerRes(BaseHttpResponse[None]):
    """分享私聊小程序卡片的响应结果"""
    pass