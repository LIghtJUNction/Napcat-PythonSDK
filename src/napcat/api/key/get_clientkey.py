"""
获取clientkey API
用于获取客户端密钥，此密钥用于身份验证和部分敏感操作
接口地址: https://napcat.apifox.cn/250286915e0.md

参数：
无需参数

返回：
- 包含clientkey的对象，用于后续API调用的身份验证

# NapCat 开发中
"""

from pydantic import BaseModel
from napcat.api.base.models import BaseHttpResponse

class GetClientkeyReq(BaseModel):
    """
    获取clientkey API 请求参数
    """
    pass  # 无请求参数

class ClientkeyData(BaseModel):
    """
    客户端密钥数据
    """
    client_key: str      # 客户端密钥字符串
    expires_in: int      # 密钥有效期(秒)
    created_at: int      # 创建时间戳

class GetClientkeyRes(BaseHttpResponse[ClientkeyData]):
    """
    获取clientkey API 响应参数
    """
    pass