# -*- coding: utf-8 -*- 
# region METADATA
"""
@tags: ['群聊相关']
@homepage: https://napcat.apifox.cn/226656748e0
@llms.txt: https://napcat.apifox.cn/226656748e0.md
@last_update: 2025-04-25 23:00:49

@description: 

summary:群踢人

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "set_group_kick"
__id__ = "226656748e0"
__method__ = "POST"

# region METADATA/


# region code
from pydantic import BaseModel, Field
from typing import Any
import logging

logger = logging.getLogger(__name__)

# region component_models
class UserID(BaseModel):
    id: str | int = Field(description="标识ID")
    # name字段openapi里没有定义

    model_config = {
        "extra": "allow",
    }

class GroupID(BaseModel):
    id: str | int = Field(description="标识ID")
    # name字段openapi里没有定义

    model_config = {
        "extra": "allow",
    }

class ResultData(BaseModel):
    # data 字段的类型根据openapi是object，但是它的properties为空，所以这里设置为Any
    data: dict[str, Any] = Field(default_factory=dict, description="data字段")

    model_config = {
        "extra": "allow",
    }

class Result(BaseModel):
    status: str = Field(default="ok", description="status字段")
    retcode: float = Field(description="retcode字段")
    data: ResultData | None = Field(default=None, description="data字段")
    message: str = Field(description="message字段")
    wording: str = Field(description="wording字段")
    echo: str | None = Field(default=None, description="echo字段")

    model_config = {
        "extra": "allow",
    }
# region component_models/

# region req
class SetGroupKickReq(BaseModel):
    """群踢人"""
    group_id: GroupID = Field(description="群ID")
    user_id: UserID = Field(description="用户ID")
    reject_add_request: bool = Field(description="是否群拉黑")

    model_config = {
        "extra": "allow",
    }
# region req/


# region res
class SetGroupKickRes(BaseModel):
    """群踢人"""
    status: str = Field(default="ok", description="status字段")
    retcode: float = Field(default=0, description="retcode字段")
    data: None = Field(default=None, description="data字段")
    message: str = Field(default="", description="message字段")
    wording: str = Field(default="", description="wording字段")
    echo: str | None = Field(default=None, description="echo字段")

    model_config = {
        "extra": "allow",
    }
# region res/

# region api
class SetGroupKickAPI(BaseModel):
    """set_group_kick接口数据模型"""
    endpoint: str = "set_group_kick"
    method: str = "POST"
    Req: type[BaseModel] = SetGroupKickReq
    Res: type[BaseModel] = SetGroupKickRes
    logger = logging.getLogger(__name__)

    def __init__(self) -> None:
        super().__init__()
        self.logger.debug("初始化 SetGroupKickAPI")

    def __call__(self, req: SetGroupKickReq) -> SetGroupKickRes:
        """
        调用API的方法（仅作为接口定义，不包含实际请求逻辑）
        
        Args:
            req: 请求参数对象
            
        Returns:
            响应对象
        """
        # 调试日志
        self.logger.debug(f"调用 SetGroupKickAPI API")
        self.logger.debug(f"请求参数: {req.model_dump_json()}")
        
        # 注意：这里不应该包含实际的请求逻辑
        # 这个方法只是定义了接口，实际的请求应由适配器或客户端实现
        raise NotImplementedError(