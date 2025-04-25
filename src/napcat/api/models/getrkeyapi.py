# -*- coding: utf-8 -*- 
# region METADATA
"""
@tags: 密钥相关
@homepage: https://napcat.apifox.cn/283136230e0
@llms.txt: https://napcat.apifox.cn/283136230e0.md
@last_update: 2025-04-25 23:00:50

@description: 获取rkey

summary:获取rkey

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "get_rkey"
__id__ = "283136230e0"
__method__ = "POST"

# region METADATA/


# region code
from pydantic import BaseModel, Field
import logging

logger = logging.getLogger(__name__)

# region component_models
class ResultData(BaseModel):
    rkey: str = Field(..., description="RKey")
    ttl: str = Field(..., description="TTL")
    type: str = Field(..., description="Type")
    created_at: float = Field(..., description="创建时间")

class Result(BaseModel):
    status: str = Field(const="ok", description="Status")
    retcode: float = Field(..., description="Return Code")
    data: list[ResultData] = Field(..., description="Data")
    message: str = Field(..., description="Message")
    wording: str = Field(..., description="Wording")
    echo: str | None = Field(default=None, description="Echo")

# region component_models/

# region req
class GetRkeyReq(BaseModel):
    """获取rkey"""
    pass  # 没有请求参数

# region req/


# region res
class GetRkeyRes(BaseModel):
    """获取rkey"""
    status: str = Field(default="ok", description="Status")
    retcode: float = Field(default=0, description="Return Code")
    data: list[ResultData] = Field(default_factory=list, description="Data")
    message: str = Field(default="", description="Message")
    wording: str = Field(default="", description="Wording")
    echo: str | None = Field(default=None, description="Echo")

# region res/

# region api
class GetRkeyAPI:
    """get_rkey接口数据模型"""
    endpoint: str = "get_rkey"
    method: str = "POST"
    Req = GetRkeyReq
    Res = GetRkeyRes

    def __init__(self) -> None:
        self.logger = logging.getLogger(__name__)
        self.logger.debug("初始化 GetRkeyAPI")

    def __call__(self, req: GetRkeyReq) -> GetRkeyRes:
        """
        调用API的方法（仅作为接口定义，不包含实际请求逻辑）
        
        Args:
            req: 请求参数对象
            
        Returns:
            响应对象
        """
        # 调试日志
        self.logger.debug(f"调用 GetRkeyAPI API")
        self.logger.debug(f"请求参数: {req.model_dump_json()}")
        
        # 注意：这里不应该包含实际的请求逻辑
        # 这个方法只是定义了接口，实际的请求应由适配器或客户端实现
        raise NotImplementedError("此方法需要由实际的API客户端实现")

# region api/
# region code/