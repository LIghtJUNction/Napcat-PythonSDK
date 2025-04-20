"""
获取图片 API
用于获取图片文件
接口地址: https://napcat.apifox.cn/227229095e0.md

参数：
- file: 图片缓存文件名

返回：
- 图片文件信息

# NapCat 开发中
"""

from pydantic import BaseModel
from napcat.api.base.models import BaseHttpResponse

class GetImageReq(BaseModel):
    """
    获取图片 API 请求参数
    """
    file: str  # 图片缓存文件名

class ImageInfo(BaseModel):
    """
    图片信息
    """
    file: str   # 图片缓存文件名
    size: int   # 图片大小
    filename: str  # 图片文件名
    url: str    # 图片下载链接

class GetImageRes(BaseHttpResponse[ImageInfo]):
    """
    获取图片 API 响应参数
    """
    pass