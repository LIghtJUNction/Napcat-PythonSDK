# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/228534361e0
@llms.txt: https://napcat.apifox.cn/228534361e0.md
@last_update: 2025-04-25 23:00:50

@description: 

summary:检查链接安全性

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "check_url_safely"
__id__ = "228534361e0"
__method__ = "POST"

# region METADATA/


# region code
from pydantic import BaseModel, Field
import logging

logger = logging.getLogger(__name__)

# region req
class CheckUrlSafelyReq(BaseModel):
    """检查链接安全性"""
    url: str = Field(default="", description="需要检查的URL")

    model_config = {
        "extra": "allow",
    }
# region req/


# region res
class CheckUrlSafelyRes(BaseModel):
    """检查链接安全性"""
    class ResponseData(BaseModel):
        """响应数据类型"""
        yes: bool = Field(default=True, description="是否可用")
        reason: str | None = Field(default=None, description="原因")

        model_config = {
            "extra": "allow",
        }

    status: str = Field(default="ok", description="状态，如 'ok'")
    retcode: int = Field(default=0, description="返回码，0表示成功")
    data: ResponseData = Field(default_factory=lambda: CheckUrlSafelyRes.ResponseData(), description="响应数据")
    message: str = Field(default="", description="消息")
    wording: str = Field(default="", description="文字描述")
    echo: str | None = Field(default=None, description="回显内容")

    model_config = {
        "extra": "allow",
    }
# region res/

# region api
class CheckUrlSafelyAPI(BaseModel):
    """check_url_safely接口数据模型"""
    endpoint: str = Field(default="check_url_safely", description="API endpoint")
    method: str = Field(default="POST", description="HTTP method")
    Req: type[BaseModel] = Field(default=CheckUrlSafelyReq, description="Request model")
    Res: type[BaseModel] = Field(default=CheckUrlSafelyRes, description="Response model")
    logger: logging.Logger = Field(default_factory=lambda: logging.getLogger(__name__), description="Logger instance")

    def __init__(self) -> None:
        super().__init__()
        self.logger.debug("初始化 CheckUrlSafelyAPI")

    def __call__(self, req: CheckUrlSafelyReq) -> CheckUrlSafelyRes:
        """
        调用API的方法（仅作为接口定义，不包含实际请求逻辑）
        
        Args:
            req: 请求参数对象
            
        Returns:
            响应对象
        """
        # 调试日志
        self.logger.debug(f"调用 CheckUrlSafelyAPI API")
        self.logger.debug(f"请求参数: {req.model_dump_json()}")
        
        # 注意：这里不应该包含实际的请求逻辑
        # 这个方法只是定义了接口，实际的请求应由适配器或客户端实现
        raise NotImplementedError("此方法需要由实际的API客户端实现")

# region api/
# region code/