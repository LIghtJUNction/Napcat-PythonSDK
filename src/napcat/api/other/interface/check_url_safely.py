"""
检查URL安全性 API
用于检查一个URL是否安全
接口地址: https://napcat.apifox.cn/227495392e0.md

参数：
- url: 需要检查的URL

返回：
- URL安全检查结果

# NapCat 开发中
"""

from napcat.api.base.models import BaseHttpResponse
from pydantic import BaseModel

class CheckUrlSafelyReq(BaseModel):
    """
    检查URL安全性 API 请求参数
    """
    url: str  # 需要检查的URL

class SafetyCheckResult(BaseModel):
    """
    安全检查结果
    """
    url: str       # 检查的URL
    is_safe: bool  # 是否安全
    risk_level: int  # 风险等级，0-5，数字越大风险越高
    risk_type: str   # 风险类型，如"phishing"、"malware"等

class CheckUrlSafelyRes(BaseHttpResponse[SafetyCheckResult]):
    """
    检查URL安全性 API 响应参数
    """
    pass