# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/226659167e0
@llms.txt: https://napcat.apifox.cn/226659167e0.md
@last_update: 2025-04-25 23:00:49

@description: 

summary:设置群聊已读

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "mark_group_msg_as_read"
__id__ = "226659167e0"
__method__ = "POST"

# region METADATA/


# region code
from pydantic import BaseModel, Field
import logging

logger = logging.getLogger(__name__)

# region component_models
class GroupId(BaseModel):
    group_id: str | int = Field(description="群组ID")

    model_config = {
        "extra": "allow",
    }


class Result(BaseModel):
    status: str = Field(default="ok", description="status字段")
    retcode: float = Field(description="retcode字段")
    data: dict[str, any] | None = Field(default=None, description="data字段")
    message: str = Field(description="message字段")
    wording: str = Field(description="wording字段")
    echo: str | None = Field(default=None, description="echo字段")

    model_config = {
        "extra": "allow",
    }

# region component_models/

# region req
class MarkGroupMsgAsReadReq(BaseModel):
    """设置群聊已读"""
    group_id: GroupId = Field(description="群组ID")

    model_config = {
        "extra": "allow",
    }

# region req/


# region res
class MarkGroupMsgAsReadRes(BaseModel):
    """设置群聊已读"""
    status: str = Field(default="ok", description="status字段")
    retcode: float = Field(default=0, description="retcode字段")
    data: dict[str, any] | None = Field(default=None, description="data字段")
    message: str = Field(default="", description="message字段")
    wording: str = Field(default="", description="wording字段")
    echo: str | None = Field(default=None, description="echo字段")

    model_config = {
        "extra": "allow",
    }

# region res/

# region api
class MarkGroupMsgAsReadAPI(BaseModel):
    """mark_group_msg_as_read接口数据模型"""
    endpoint: str = Field(default="mark_group_msg_as_read", description="API端点")
    method: str = Field(default="POST", description="HTTP方法")
    Req: type[BaseModel] = Field(default=MarkGroupMsgAsReadReq, description="请求模型")
    Res: type[BaseModel] = Field(default=MarkGroupMsgAsReadRes, description="响应模型")
    logger: logging.Logger = Field(default_factory=lambda: logging.getLogger(__name__), description="日志记录器")

# region api/
# region code/