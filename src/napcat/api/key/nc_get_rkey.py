"""
nc获取rkey API
用于通过NapCat服务获取rkey，该密钥用于特定的加密和验证操作
接口地址: https://napcat.apifox.cn/226659297e0.md

参数：
无需参数

返回：
- 包含rkey的对象，用于特定的加密和验证场景

# NapCat 开发中
"""

from pydantic import BaseModel
from napcat.api.base.types import BaseHttpResponse

class NcGetRkeyReq(BaseModel):
    """
    nc获取rkey API 请求参数
    """
    pass  # 无请求参数

class RkeyData(BaseModel):
    """
    Rkey数据
    """
    rkey: str           # R密钥字符串
    expires_in: int     # 密钥有效期(秒)
    created_at: int     # 创建时间戳

class NcGetRkeyRes(BaseHttpResponse[RkeyData]):
    """
    nc获取rkey API 响应参数
    """
    pass