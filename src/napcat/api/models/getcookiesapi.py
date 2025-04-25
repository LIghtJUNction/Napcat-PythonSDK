# -*- coding: utf-8 -*- 
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/226657041e0
@llms.txt: https://napcat.apifox.cn/226657041e0.md
@last_update: 2025-04-25 23:00:49

@description: 获取cookies

summary:获取cookies

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "get_cookies"
__id__ = "226657041e0"
__method__ = "POST"

# region METADATA/


# region code
from pydantic import BaseModel, Field
import logging

logger = logging.getLogger(__name__)


# region req
class GetCookiesReq(BaseModel):
    """获取cookies"""
    domain: str = Field(..., description="域名")

    model_config = {
        "extra": "allow",
    }
# region req/


# region res
class GetCookiesRes(BaseModel):
    """获取cookies"""
    class ResponseData(BaseModel):
        """响应数据类型"""
        cookies: str = Field(default="", description="cookies字段")
        bkn: str = Field(default="", description="bkn字段")

        model_config = {
            "extra": "allow",
        }

    status: str = Field(default="ok", description="status字段")
    retcode: float = Field(default=0, description="retcode字段")
    data: ResponseData = Field(default_factory=ResponseData, description="data字段")
    message: str = Field(default="", description="message字段")
    wording: str = Field(default="", description="wording字段")
    echo: str | None = Field(default=None, description="echo字段")

    model_config = {
        "extra": "allow",
    }
# region res/

# region api
class GetCookiesAPI:
    """get_cookies接口数据模型"""
    endpoint: str = "get_cookies"
    method: str = "POST"
    Req = GetCookiesReq
    Res = GetCookiesRes

    @classmethod
    def __call__(cls, req: GetCookiesReq) -> GetCookiesRes:
        """
        调用API的方法（仅作为接口定义，不包含实际请求逻辑）
        
        Args:
            req: 请求参数对象
            
        Returns:
            响应对象
        """
        logger.debug(f"调用 GetCookiesAPI API")
        logger.debug(f"请求参数: {req.model_dump_json()}")
        
        # 注意：这里不应该包含实际的请求逻辑
        # 这个方法只是定义了接口，实际的请求应由适配器或客户端实现
        raise NotImplementedError("此方法需要由实际的API客户端实现")

# region api/
# region code/