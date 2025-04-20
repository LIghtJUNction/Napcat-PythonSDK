"""
获取小程序卡片 API
用于获取可分享的QQ小程序卡片信息
接口地址: https://napcat.apifox.cn/227738594e0.md

参数：
- app_id: 小程序的应用ID
- title: 卡片标题
- content: 卡片内容描述
- url: 小程序链接地址
- icon: 小程序图标URL(可选)
- mini_app_path: 小程序路径(可选)

返回：
- 小程序卡片的数据结构，可用于发送消息

# NapCat 开发中
"""

from pydantic import BaseModel
from napcat.api.base.models import BaseHttpResponse

class GetMiniAppArkReq(BaseModel):
    """
    获取小程序卡片 API 请求参数
    """
    app_id: str                  # 小程序的应用ID
    title: str                   # 卡片标题
    content: str                 # 卡片内容描述
    url: str                     # 小程序链接地址
    icon: str | None = None          # 小程序图标URL(可选)
    mini_app_path: str | None = None # 小程序路径(可选)

class MiniAppArkData(BaseModel):
    """
    小程序卡片数据
    """
    app_info: str                # 小程序信息
    ark_json: str                # 卡片JSON数据
    view_id: str                 # 视图ID

class GetMiniAppArkRes(BaseHttpResponse[MiniAppArkData]):
    """
    获取小程序卡片 API 响应参数
    """
    pass