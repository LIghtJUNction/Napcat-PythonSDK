# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/226658660e0
@llms.txt: https://napcat.apifox.cn/226658660e0.md
@last_update: 2025-04-25 23:00:49

@description: 

summary:获取群系统消息

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "get_group_system_msg"
__id__ = "226658660e0"
__method__ = "POST"

# region METADATA/


# region code
from pydantic import BaseModel, Field
from typing import Any
import logging

logger = logging.getLogger(__name__)

# region component_models
class group_id(BaseModel):
    id: str = Field(description="标识ID")
    name: str | None = Field(None, description="名称")

    model_config = {
        "extra": "allow",
    }

class result(BaseModel):
    status: str = Field(description="status字段")
    retcode: float = Field(description="retcode字段")
    data: dict[str, Any] = Field(description="data字段")
    message: str = Field(description="message字段")
    wording: str = Field(description="wording字段")
    echo: str | None = Field(description="echo字段")

    model_config = {
        "extra": "allow",
    }
# region component_models/

# region req
class GetGroupSystemMsgReq(BaseModel):
    """获取群系统消息"""
    group_id: group_id

    model_config = {
        "extra": "allow",
    }
# region req/


# region res
class GetGroupSystemMsgRes(BaseModel):
    """获取群系统消息"""
    class ResponseData(BaseModel):
        """响应数据类型"""
        InvitedRequest: list[InvitedrequestItem] = Field(default=None, description="InvitedRequest字段")
        join_requests: list[JoinRequestsItem] = Field(default=None, description="join_requests字段")

        model_config = {
            "extra": "allow",
        }

    status: str = Field(default="ok", description="status字段")
    retcode: float = Field(default=0, description="retcode字段")
    data: ResponseData = Field(default_factory=lambda: ResponseData(), description="data字段")
    message: str = Field(default="", description="message字段")
    wording: str = Field(default="", description="wording字段")
    echo: str | None = Field(default=None, description="echo字段")

    model_config = {
        "extra": "allow",
    }
# region res/

# region api
class GetGroupSystemMsgAPI(BaseModel):
    """get_group_system_msg接口数据模型"""
    endpoint: str = "get_group_system_msg"
    method: str = "POST"
    Req: type[BaseModel] = GetGroupSystemMsgReq
    Res: type[BaseModel] = GetGroupSystemMsgRes
    logger = logging.getLogger(__name__)

    def __init__(self) -> None:
        super().__init__()
        self.logger.debug("初始化 GetGroupSystemMsgAPI")

    def __call__(self, req: GetGroupSystemMsgReq) -> GetGroupSystemMsgRes:
        """
        调用API的方法（仅作为接口定义，不包含实际请求逻辑）
        
        Args:
            req: 请求参数对象
            
        Returns:
            响应对象
        """
        # 调试日志
        self.logger.debug(f"调用 GetGroupSystemMsgAPI API")
        self.logger.debug(f"请求参数: {req.model_dump_json()}")
        
        # 注意：这里不应该包含实际的请求逻辑
        # 这个方法只是定义了接口，实际的请求应由适配器或客户端实现
        raise NotImplementedError("此方法需要由实际的API客户端实现")

# region api/
# region code/

