# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/226656707e0
@llms.txt: https://napcat.apifox.cn/226656707e0.md
@last_update: 2025-04-25 23:00:48

@description: 

summary:获取消息详情

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "get_msg"
__id__ = "226656707e0"
__method__ = "POST"

# region METADATA/


# region code
from pydantic import BaseModel, Field
import logging

logger = logging.getLogger(__name__)

# region component_models
class MessageId(BaseModel):
    """标识ID类型，可以是字符串或数字"""
    id: str | int = Field(description="标识ID")
    name: str | None = Field(default=None, description="名称")

    model_config = {
        "extra": "allow",
    }

class Result(BaseModel):
    """通用结果返回类型"""
    status: str = Field(default="ok", description="status字段")
    retcode: float = Field(default=0.0, description="retcode字段")
    data: dict[str, any] = Field(default_factory=dict, description="data字段")
    message: str = Field(default="", description="message字段")
    wording: str = Field(default="", description="wording字段")
    echo: str | None = Field(default=None, description="echo字段")

    model_config = {
        "extra": "allow",
    }
# region component_models/

# region req
class GetMsgReq(BaseModel):
    """获取消息详情请求参数"""
    message_id: MessageId = Field(description="消息ID")

    model_config = {
        "extra": "allow",
    }
# region req/


# region res
class GetMsgRes(BaseModel):
    """获取消息详情响应结果"""
    status: str = Field(default="ok", description="status字段")
    retcode: float = Field(default=0.0, description="retcode字段")
    data: dict[str, any] = Field(default_factory=dict, description="data字段")
    message: str = Field(default="", description="message字段")
    wording: str = Field(default="", description="wording字段")
    echo: str | None = Field(default=None, description="echo字段")

    model_config = {
        "extra": "allow",
    }
# region res/

# region api
class GetMsgAPI:
    """get_msg接口数据模型"""
    endpoint: str = "get_msg"
    method: str = "POST"
    logger = logging.getLogger(__name__)

    def __init__(self) -> None:
        self.logger.debug("初始化 GetMsgAPI")

    def __call__(self, req: GetMsgReq) -> GetMsgRes:
        """
        调用API的方法（仅作为接口定义，不包含实际请求逻辑）
        
        Args:
            req: 请求参数对象
            
        Returns:
            响应对象
        """
        # 调试日志
        self.logger.debug(f"调用 GetMsgAPI API")
        self.logger.debug(f"请求参数: {req.model_dump_json()}")
        
        # 注意：这里不应该包含实际的请求逻辑
        # 这个方法只是定义了接口，实际的请求应由适配器或客户端实现
        raise NotImplementedError("此方法需要由实际的API客户端实现")

# region api/
# region code/
