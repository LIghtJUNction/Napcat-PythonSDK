# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/226658678e0
@llms.txt: https://napcat.apifox.cn/226658678e0.md
@last_update: 2025-04-25 23:00:49

@description: 

summary:删除群精华消息

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "delete_essence_msg"
__id__ = "226658678e0"
__method__ = "POST"

# region METADATA/


# region code
from pydantic import BaseModel, Field
import logging
from typing import Any

logger = logging.getLogger(__name__)

# region component_models
class MessageId(BaseModel):
    """标识ID"""
    id: str | int = Field(description="标识ID")
    name: str | None = Field(default=None, description="名称")

    model_config = {
        "extra": "allow",
    }

class Result(BaseModel):
    """返回结果"""
    status: str = Field(default="ok", description="状态，如 'ok'")
    retcode: float = Field(default=0, description="返回码，0表示成功")
    data: dict[str, Any] = Field(default_factory=dict, description="数据")
    message: str = Field(default="", description="消息")
    wording: str = Field(default="", description="文字描述")
    echo: str | None = Field(default=None, description="回显内容")

    model_config = {
        "extra": "allow",
    }

# region component_models/

# region req
class DeleteEssenceMsgReq(BaseModel):
    """删除群精华消息请求参数"""
    message_id: str | int = Field(description="标识ID")

    model_config = {
        "extra": "allow",
    }

# region req/


# region res

# region res/

# region api
class DeleteEssenceMsgAPI(BaseModel):
    """delete_essence_msg接口数据模型"""
    endpoint: str = "delete_essence_msg"
    method: str = "POST"
    logger = logging.getLogger(__name__)

    def __init__(self) -> None:
        super().__init__()
        self.logger.debug("初始化 DeleteEssenceMsgAPI")

    def __call__(self, req: DeleteEssenceMsgReq) -> Result:
        """
        调用API的方法（仅作为接口定义，不包含实际请求逻辑）
        
        Args:
            req: 请求参数对象
            
        Returns:
            响应对象
        """
        # 调试日志
        self.logger.debug(f"调用 DeleteEssenceMsgAPI API")
        self.logger.debug(f"请求参数: {req.model_dump_json()}")
        
        # 注意：这里不应该包含实际的请求逻辑
        # 这个方法只是定义了接口，实际的请求应由适配器或客户端实现
        raise NotImplementedError(