# -*- coding: utf-8 -*- 
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/244510838e0
@llms.txt: https://napcat.apifox.cn/244510838e0.md
@last_update: 2025-04-25 23:00:50

@description: 发送群消息

summary:发送私聊文件

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "send_private_msg"
__id__ = "244510838e0"
__method__ = "POST"

# region METADATA/


# region code
from pydantic import BaseModel, Field
import logging

logger = logging.getLogger(__name__)

# region component_models
class 文件消息Data(BaseModel):
    file: str = Field(..., description="文件路径")
    name: str | None = Field(None, description="文件名称")

    model_config = {
        "extra": "allow",
    }

class 文件消息(BaseModel):
    type: str = Field("file", const=True, description="type字段")
    data: 文件消息Data = Field(..., description="data字段")

    model_config = {
        "extra": "allow",
    }

class resultData(BaseModel):
    message_id: float = Field(..., description="消息ID")

    model_config = {
        "extra": "allow",
    }


# region component_models/

# region req
class SendPrivateMsgReq(BaseModel):
    """发送私聊文件"""
    user_id: str | int = Field(..., description="标识ID")
    message: list[文件消息] = Field(..., description="消息列表")

    model_config = {
        "extra": "allow",
    }

# region req/


# region res
class SendPrivateMsgRes(BaseModel):
    """发送私聊文件"""

    status: str = Field("ok", const=True, description="status字段")
    retcode: float = Field(0, description="retcode字段")
    data: resultData | None = Field(None, description="data字段")
    message: str = Field("", description="message字段")
    wording: str = Field("", description="wording字段")
    echo: str | None = Field(None, description="echo字段")

    model_config = {
        "extra": "allow",
    }

# region res/

# region api
class SendPrivateMsgAPI(BaseModel):
    """send_private_msg接口数据模型"""
    endpoint: str = Field("send_private_msg", description="API endpoint")
    method: str = Field("POST", description="HTTP method")
    Req: type[BaseModel] = Field(SendPrivateMsgReq, description="Request model")
    Res: type[BaseModel] = Field(SendPrivateMsgRes, description="Response model")
    logger: logging.Logger = Field(default_factory=lambda: logging.getLogger(__name__), description="Logger instance")

    def __init__(self) -> None:
        super().__init__()
        self.logger.debug("初始化 SendPrivateMsgAPI")

    def __call__(self, req: SendPrivateMsgReq) -> SendPrivateMsgRes:
        """
        调用API的方法（仅作为接口定义，不包含实际请求逻辑）

        Args:
            req: 请求参数对象

        Returns:
            响应对象
        """
        # 调试日志
        self.logger.debug(f"调用 SendPrivateMsgAPI API")
        self.logger.debug(f"请求参数: {req.model_dump_json()}")

        # 注意：这里不应该包含实际的请求逻辑
        # 这个方法只是定义了接口，实际的请求应由适配器或客户端实现
        raise NotImplementedError("此方法需要由实际的API客户端实现")

# region api/
# region code/