"""
获取推荐好友卡片 API
用于获取系统推荐的好友卡片信息，展示给用户作为添加建议
接口地址: https://napcat.apifox.cn/226658965e0.md

参数：
- category_id: 推荐的类别ID

返回：
- 包含推荐好友卡片信息的列表

# NapCat 开发中
"""



from pydantic import BaseModel
from napcat.api.base.models import BaseHttpResponse

class ArkSharePeerReq(BaseModel):
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