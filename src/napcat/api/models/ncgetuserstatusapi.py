# -*- coding: utf-8 -*- 
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/226659292e0
@llms.txt: https://napcat.apifox.cn/226659292e0.md
@last_update: 2025-04-25 23:00:50

@description: 

summary:获取用户状态

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "nc_get_user_status"
__id__ = "226659292e0"
__method__ = "POST"

# region METADATA/


# region code
from pydantic import BaseModel, Field
from typing import Any
import logging

logger = logging.getLogger(__name__)

# region component_models
class UserId(BaseModel):
    id: str = Field(default="", description="标识ID")
    name: str | None = Field(default=None, description="名称")

    model_config = {
        "extra": "allow",
    }


class Result(BaseModel):
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
class NcGetUserStatusReq(BaseModel):
    """获取用户状态"""
    user_id: str | int = Field(description="用户ID，可以是字符串或数字")

    model_config = {
        "extra": "allow",
    }


# region req/


# region res
class NcGetUserStatusRes(BaseModel):
    """获取用户状态"""

    class ResponseData(BaseModel):
        """响应数据类型"""
        status: float = Field(default=0.0, description="status字段")
        ext_status: float = Field(default=0.0, description="ext_status字段")

        model_config = {
            "extra": "allow",
        }

    status: str = Field(default="ok", description="status字段")
    retcode: float = Field(default=0.0, description="retcode字段")
    data: ResponseData = Field(default_factory=ResponseData, description="data字段")
    message: str = Field(default="", description="message字段")
    wording: str = Field(default="", description="wording字段")
    echo: str | None = Field(default=None, description="echo字段")

    model_config = {
        "extra": "allow",
    }


# region res/

# region api
class NcGetUserStatusAPI(BaseModel):
    """nc_get_user_status接口数据模型"""
    endpoint: str = Field(default="nc_get_user_status", description="Endpoint名称")
    method: str = Field(default="POST", description="请求方法")
    Req: type[BaseModel] = Field(default=NcGetUserStatusReq, description="请求模型")
    Res: type[BaseModel] = Field(default=NcGetUserStatusRes, description="响应模型")
    logger: logging.Logger = Field(default_factory=lambda: logging.getLogger(__name__), description="Logger")

    def __init__(self) -> None:
        super().__init__()
        self.logger.debug("初始化 NcGetUserStatusAPI")

    def __call__(self, req: NcGetUserStatusReq) -> NcGetUserStatusRes:
        """
        调用API的方法（仅作为接口定义，不包含实际请求逻辑）

        Args:
            req: 请求参数对象

        Returns:
            响应对象
        """
        # 调试日志
        self.logger.debug(f"调用 NcGetUserStatusAPI API")
        self.logger.debug(f"请求参数: {req.model_dump_json()}")

        # 注意：这里不应该包含实际的请求逻辑
        # 这个方法只是定义了接口，实际的请求应由适配器或客户端实现
        raise NotImplementedError("此方法需要由实际的API客户端实现")


# region api/
# region code/