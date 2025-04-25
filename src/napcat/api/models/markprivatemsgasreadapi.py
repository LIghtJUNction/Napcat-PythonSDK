# -*- coding: utf-8 -*- 
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/226659165e0
@llms.txt: https://napcat.apifox.cn/226659165e0.md
@last_update: 2025-04-25 23:00:49

@description: 

summary:设置私聊已读

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "mark_private_msg_as_read"
__id__ = "226659165e0"
__method__ = "POST"

# region METADATA/


# region code
from pydantic import BaseModel, Field
import logging

logger = logging.getLogger(__name__)

# region component_models
class ResultData(BaseModel):
    """Result Data Model"""
    pass


class Result(BaseModel):
    """Result Model"""
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
class MarkPrivateMsgAsReadReq(BaseModel):
    """设置私聊已读 请求体"""
    user_id: str | int = Field(description="标识ID")

    model_config = {
        "extra": "allow",
    }

# region req/


# region res
class MarkPrivateMsgAsReadRes(BaseModel):
    """设置私聊已读 响应体"""

    status: str = Field(default="ok", description="status字段")
    retcode: float = Field(default=0.0, description="retcode字段")
    data: None = Field(default=None, description="data字段")
    message: str = Field(default="", description="message字段")
    wording: str = Field(default="", description="wording字段")
    echo: str | None = Field(default=None, description="echo字段")

    model_config = {
        "extra": "allow",
    }

# region res/

# region api
class MarkPrivateMsgAsReadAPI(BaseModel):
    """mark_private_msg_as_read接口数据模型"""
    endpoint: str = Field(default="mark_private_msg_as_read")
    method: str = Field(default="POST")
    Req: type[BaseModel] = Field(default=MarkPrivateMsgAsReadReq)
    Res: type[BaseModel] = Field(default=MarkPrivateMsgAsReadRes)

# region api/
# region code/