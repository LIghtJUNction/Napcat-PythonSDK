"""
获取推荐群聊卡片 API
用于获取系统推荐的群聊卡片信息，可用于群聊推广和邀请加群
接口地址: https://napcat.apifox.cn/226658971e0.md

参数：
- group_id: 群号，要获取卡片信息的群ID

返回：
- 包含群聊卡片信息的数据，如群名称、群头像、群简介等

"""

"""
分享群聊小程序卡片 API
用于分享小程序卡片到指定群聊
接口地址: https://napcat.apifox.cn/250287107e0.md

参数：
- app_id: 小程序ID
- group_id: 目标群号
- title: 卡片标题
- content: 卡片内容
- image: 卡片图片URL
- url: 小程序跳转链接

返回：
- 分享结果信息

# NapCat 开发中
"""

from typing import TypedDict
from napcat.api.base.models import BaseHttpResponse
# region TypedDicts
class ArkShareGroupReq(TypedDict):
    """分享群聊小程序卡片的请求参数"""
    app_id: str
    group_id: int
    title: str
    content: str
    image: str
    url: str

class ArkShareGroupRes(BaseHttpResponse[None]):
    """分享群聊小程序卡片的响应结果"""
    pass
