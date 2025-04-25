# -*- coding: utf-8 -*- 
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/226659234e0
@llms.txt: https://napcat.apifox.cn/226659234e0.md
@last_update: 2025-04-25 23:00:50

@description: 获取被过滤的加群请求

summary:获取被过滤的加群请求

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "get_group_ignore_add_request"
__id__ = "226659234e0"
__method__ = "POST"

# region METADATA/


# region code
from pydantic import BaseModel, Field


# region component_models
class result(BaseModel):
    status: str = Field(default="ok", description="status字段")
    retcode: float = Field(default=0.0, description="retcode字段")
    data: list[dict[str, any]] = Field(default_factory=list, description="data字段")
    message: str = Field(default="", description="message字段")
    wording: str = Field(default="", description="wording字段")
    echo: str | None = Field(default=None, description="echo字段")

    model_config = {
        "extra": "allow",
    }
# region component_models/

# region req
class GetGroupIgnoreAddRequestReq(BaseModel):
    """获取被过滤的加群请求"""
    pass  # 没有请求参数

    model_config = {
        "extra": "allow",
    }
# region req/


# region res
class GetGroupIgnoreAddRequestRes(BaseModel):
    """获取被过滤的加群请求"""
    class ResponseData(BaseModel):
        """响应数据类型"""
        yes: bool = Field(default=True, description="是否可用")
        reason: str | None = Field(default=None, description="原因")

        model_config = {
            "extra": "allow",
        }

    status: str = Field(default="ok", description="status字段")
    retcode: float = Field(default=0, description="retcode字段")
    data: ResponseData = Field(default_factory=lambda: ResponseData, description="data字段")
    message: str = Field(default="", description="message字段")
    wording: str = Field(default="", description="wording字段")
    echo: str | None = Field(default=None, description="echo字段")

    model_config = {
        "extra": "allow",
    }
# region res/

# region api
import logging

class GetGroupIgnoreAddRequestAPI(BaseModel):
    """get_group_ignore_add_request接口数据模型"""
    endpoint: str = Field(default="get_group_ignore_add_request", description="接口endpoint")
    method: str = Field(default="POST", description="接口请求方法")
    Req: type[BaseModel] = Field(default=GetGroupIgnoreAddRequestReq, description="请求模型")
    Res: type[BaseModel] = Field(default=GetGroupIgnoreAddRequestRes, description="响应模型")
    logger: logging.Logger = Field(default_factory=lambda: logging.getLogger(__name__), description="日志记录器")

    def __call__(self, req: GetGroupIgnoreAddRequestReq) -> GetGroupIgnoreAddRequestRes:
        """
        调用API的方法（仅作为接口定义，不包含实际请求逻辑）
        
        Args:
            req: 请求参数对象
            
        Returns:
            响应对象
        """
        # 调试日志
        self.logger.debug(f"调用 GetGroupIgnoreAddRequestAPI API")
        self.logger.debug(f"请求参数: {req.model_dump_json()}")
        
        # 注意：这里不应该包含实际的请求逻辑
        # 这个方法只是定义了接口，实际的请求应由适配器或客户端实现
        raise NotImplementedError("此方法需要由实际的API客户端实现")

# region api/
# region code/