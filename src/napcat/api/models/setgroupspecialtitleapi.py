# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: 群聊相关
@homepage: https://napcat.apifox.cn/226656931e0
@llms.txt: https://napcat.apifox.cn/226656931e0.md
@last_update: 2025-04-25 23:00:49

@description: 

summary:设置群头衔

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "set_group_special_title"
__id__ = "226656931e0"
__method__ = "POST"

# region METADATA/


# region code
from pydantic import BaseModel, Field
from typing import Any
import logging

logger = logging.getLogger(__name__)

# region component_models
class UserId(BaseModel):
    id: str = Field(..., description="标识ID")
    name: str | None = Field(None, description="名称")

    model_config = {
        "extra": "allow",
    }


class GroupId(BaseModel):
    id: str = Field(..., description="标识ID")
    name: str | None = Field(None, description="名称")

    model_config = {
        "extra": "allow",
    }


# region component_models/

# region req
class SetGroupSpecialTitleReq(BaseModel):
    """设置群头衔"""
    group_id: GroupId = Field(..., description="群ID")
    user_id: UserId = Field(..., description="用户ID")
    special_title: str = Field(..., description="特殊头衔")

    model_config = {
        "extra": "allow",
    }


# region req/


# region res
class SetGroupSpecialTitleRes(BaseModel):
    """设置群头衔"""

    class ResponseData(BaseModel):
        """响应数据类型"""
        yes: bool = Field(default=True, description="是否可用")
        reason: str | None = Field(default=None, description="原因")

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
class SetGroupSpecialTitleAPI(BaseModel):
    """set_group_special_title接口数据模型"""

    endpoint: str = Field(default="set_group_special_title", description="API端点")
    method: str = Field(default="POST", description="HTTP方法")
    Req: type[BaseModel] = Field(default=SetGroupSpecialTitleReq, description="请求模型")
    Res: type[BaseModel] = Field(default=SetGroupSpecialTitleRes, description="响应模型")
    logger: logging.Logger = Field(default_factory=lambda: logging.getLogger(__name__), description="日志记录器")

    def __init__(self) -> None:
        super().__init__()
        self.logger.debug("初始化 SetGroupSpecialTitleAPI")

    def __call__(self, req: SetGroupSpecialTitleReq) -> SetGroupSpecialTitleRes:
        """
        调用API的方法（仅作为接口定义，不包含实际请求逻辑）

        Args:
            req: 请求参数对象

        Returns:
            响应对象
        """
        # 调试日志
        self.logger.debug(f"调用 SetGroupSpecialTitleAPI API")
        self.logger.debug(f"请求参数: {req.model_dump_json()}")

        # 注意：这里不应该包含实际的请求逻辑
        # 这个方法只是定义了接口，实际的请求应由适配器或客户端实现
        raise NotImplementedError("此方法需要由实际的API客户端实现")

# region api/
# region code/
