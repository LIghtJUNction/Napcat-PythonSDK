# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/226659240e0
@llms.txt: https://napcat.apifox.cn/226659240e0.md
@last_update: 2025-04-25 23:00:50

@description: 

summary:_删除群公告

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "_del_group_notice"
__id__ = "226659240e0"
__method__ = "POST"

# region METADATA/


# region code
from pydantic import BaseModel, Field
import logging
from typing import Any

logger = logging.getLogger(__name__)

# region component_models
class GroupId(BaseModel):
    id: str = Field(description="标识ID")
    name: str | None = Field(default=None, description="名称")

    model_config = {
        "extra": "allow",
    }


class Result(BaseModel):
    status: str = Field(default="ok", const="ok", description="status字段")
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
class DelGroupNoticeReq(BaseModel):
    """_删除群公告"""
    group_id: str | int = Field(description="群ID")
    notice_id: str = Field(description="公告ID")

    model_config = {
        "extra": "allow",
    }


# region req/


# region res
class DelGroupNoticeRes(BaseModel):
    """_删除群公告"""

    class ResponseData(BaseModel):
        """响应数据类型"""

        result: float = Field(description="result字段")
        errMsg: str = Field(description="errMsg字段")

        model_config = {
            "extra": "allow",
        }

    status: str = Field(default="ok", const="ok", description="status字段")
    retcode: float = Field(default=0.0, description="retcode字段")
    data: ResponseData = Field(default_factory=lambda: ResponseData(), description="data字段")
    message: str = Field(default="", description="message字段")
    wording: str = Field(default="", description="wording字段")
    echo: str | None = Field(default=None, description="echo字段")

    model_config = {
        "extra": "allow",
    }


# region res/

# region api
class DelGroupNoticeAPI(BaseModel):
    """_del_group_notice接口数据模型"""

    endpoint: str = Field(default="_del_group_notice", description="Endpoint")
    method: str = Field(default="POST", description="请求方法")
    Req: type[BaseModel] = Field(default=DelGroupNoticeReq, description="请求模型")
    Res: type[BaseModel] = Field(default=DelGroupNoticeRes, description="响应模型")
    logger: logging.Logger = Field(default_factory=lambda: logging.getLogger(__name__), description="Logger")

    def __call__(self, req: DelGroupNoticeReq) -> DelGroupNoticeRes:
        """
        调用API的方法（仅作为接口定义，不包含实际请求逻辑）

        Args:
            req: 请求参数对象

        Returns:
            响应对象
        """
        # 调试日志
        self.logger.debug("调用 DelGroupNoticeAPI API")
        self.logger.debug(f"请求参数: {req.model_dump_json()}")

        # 注意：这里不应该包含实际的请求逻辑
        # 这个方法只是定义了接口，实际的请求应由适配器或客户端实现
        raise NotImplementedError("此方法需要由实际的API客户端实现")


# region api/
# region code/