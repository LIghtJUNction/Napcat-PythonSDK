"""
获取rkey API
用于获取rkey密钥，此密钥在多种QQ安全验证场景中使用
接口地址: https://napcat.apifox.cn/283136230e0.md

参数：
无需参数

返回：
- 包含rkey的对象，用于QQ各类API的安全验证

# NapCat 开发中
"""

from pydantic import BaseModel
from napcat.api.base.types import BaseHttpResponse

class GetRkeyReq(BaseModel):
    """
    获取rkey API 请求参数
    """
    pass  # 无请求参数

class RkeyResult(BaseModel):
    """
    Rkey结果数据
    """
    rkey: str           # R密钥字符串
    expires_in: int     # 密钥有效期(秒)
    create_time: int    # 创建时间戳

class GetRkeyRes(BaseHttpResponse[RkeyResult]):
    """
    获取rkey API 响应参数
    """
    pass