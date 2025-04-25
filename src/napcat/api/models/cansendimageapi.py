# -*- coding: utf-8 -*- 
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/226657071e0
@llms.txt: https://napcat.apifox.cn/226657071e0.md
@last_update: 2025-04-25 23:00:49

@description: 

summary:检查是否可以发送图片

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "can_send_image"
__id__ = "226657071e0"
__method__ = "POST"

# region METADATA/


# region code
from pydantic import BaseModel, Field
from typing import Any
import logging

logger = logging.getLogger(__name__)

# region component_models
class result(BaseModel):
    """result模型"""
    status: str = Field(default="ok", description="status字段")
    retcode: float = Field(default=0.0, description="retcode字段")
    data: dict[str, Any] = Field(default_factory=dict, description="data字段")
    message: str = Field(default="", description="message字段")
    wording: str = Field(default="", description="wording字段")
    echo: str | None = Field(default=None, description="echo字段")

    model_config = {
        "extra": "allow",
    }
# region component_models/

# region req
class CanSendImageReq(BaseModel):
    """检查是否可以发送图片 请求参数模型"""
    model_config = {
        "extra": "allow",
    }
# region req/


# region res
class CanSendImageRes(BaseModel):
    """检查是否可以发送图片 响应参数模型"""
    class ResponseData(BaseModel):
        """响应数据类型"""
        yes: bool = Field(..., description="yes字段")

        model_config = {
            "extra": "allow",
        }

    status: str = Field(default="ok", description="status字段")
    retcode: float = Field(default=0.0, description="retcode字段")
    data: ResponseData = Field(..., description="data字段")
    message: str = Field(default="", description="message字段")
    wording: str = Field(default="", description="wording字段")
    echo: str | None = Field(default=None, description="echo字段")

    model_config = {
        "extra": "allow",
    }
# region res/

# region api
class CanSendImageAPI(BaseModel):
    """can_send_image接口数据模型"""
    endpoint: str = "can_send_image"
    method: str = "POST"
    Req: type[CanSendImageReq] = CanSendImageReq
    Res: type[CanSendImageRes] = CanSendImageRes
    logger = logging.getLogger(__name__)

    def __call__(self, req: CanSendImageReq) -> CanSendImageRes:
        """
        调用API的方法（仅作为接口定义，不包含实际请求逻辑）
        
        Args:
            req: 请求参数对象
            
        Returns:
            响应对象
        """
        # 调试日志
        self.logger.debug(f"调用 CanSendImageAPI API")
        self.logger.debug(f"请求参数: {req.model_dump_json()}")
        
        # 注意：这里不应该包含实际的请求逻辑
        # 这个方法只是定义了接口，实际的请求应由适配器或客户端实现
        return CanSendImageRes()

# region api/
# region code/