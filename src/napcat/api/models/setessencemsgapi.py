# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/226658674e0
@llms.txt: https://napcat.apifox.cn/226658674e0.md
@last_update: 2025-04-25 23:00:49

@description: 

summary:设置群精华消息

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "set_essence_msg"
__id__ = "226658674e0"
__method__ = "POST"

# region METADATA/


# region code
from pydantic import BaseModel, Field
from typing import Any
import logging

logger = logging.getLogger(__name__)

# region component_models

class ResultData(BaseModel):
    """响应数据类型"""

    model_config = {
        "extra": "allow",
    }

class Result(BaseModel):
    """结果模型"""
    status: str = Field(default="ok", description="status字段")
    retcode: float = Field(default=0.0, description="retcode字段")
    data: ResultData = Field(default_factory=ResultData, description="data字段")
    message: str = Field(default="", description="message字段")
    wording: str = Field(default="", description="wording字段")
    echo: str | None = Field(default=None, description="echo字段")

    model_config = {
        "extra": "allow",
    }

# region component_models/

# region req
class SetEssenceMsgReq(BaseModel):
    """设置群精华消息请求模型"""
    message_id: str | int = Field(description="标识ID (可以是字符串或数字)")

    model_config = {
        "extra": "allow",
    }

# region req/


# region res
class SetEssenceMsgRes(BaseModel):
    """设置群精华消息响应模型"""
    status: str = Field(default="ok", description="status字段")
    retcode: float = Field(default=0, description="retcode字段")
    data: dict[str, Any] = Field(default_factory=dict, description="data字段")
    message: str = Field(default="", description="message字段")
    wording: str = Field(default="", description="wording字段")
    echo: str | None = Field(default=None, description="echo字段")

    model_config = {
        "extra": "allow",
    }

# region res/

# region api
class SetEssenceMsgAPI(BaseModel):
    """set_essence_msg接口数据模型"""
    endpoint: str = Field(default="set_essence_msg", description="API端点")
    method: str = Field(default="POST", description="HTTP方法")
    Req: type[BaseModel] = Field(default=SetEssenceMsgReq, description="请求模型")
    Res: type[BaseModel] = Field(default=SetEssenceMsgRes, description="响应模型")

    model_config = {
        "arbitrary_types_allowed": True
    }

    logger: logging.Logger = Field(default_factory=lambda: logging.getLogger(__name__), description="日志记录器")

    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self.logger.debug("初始化 SetEssenceMsgAPI")

    def __call__(self, req: SetEssenceMsgReq) -> SetEssenceMsgRes:
        """
        调用API的方法（仅作为接口定义，不包含实际请求逻辑）
        
        Args:
            req: 请求参数对象
            
        Returns:
            响应对象
        """
        # 调试日志
        self.logger.debug(f