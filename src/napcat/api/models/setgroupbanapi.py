# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/226656791e0
@llms.txt: https://napcat.apifox.cn/226656791e0.md
@last_update: 2025-04-25 23:00:49

@description: 

summary:群禁言

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "set_group_ban"
__id__ = "226656791e0"
__method__ = "POST"

# region METADATA/


# region code
from pydantic import BaseModel, Field
import logging

logger = logging.getLogger(__name__)


# region component_models
class UserID(BaseModel):
    """用户ID模型"""

    user_id: str = Field(description="用户ID")

    model_config = {
        "extra": "allow",
    }


class GroupID(BaseModel):
    """群组ID模型"""

    group_id: str = Field(description="群组ID")

    model_config = {
        "extra": "allow",
    }


class ResultData(BaseModel):
    """结果数据模型"""

    model_config = {
        "extra": "allow",
    }


class Result(BaseModel):
    """结果模型"""

    status: str = Field(default="ok", description="状态")
    retcode: float = Field(default=0, description="返回码")
    data: dict = Field(default={}, description="数据")
    message: str = Field(default="", description="消息")
    wording: str = Field(default="", description="措辞")
    echo: str | None = Field(default=None, description="回显")

    model_config = {
        "extra": "allow",
    }


# region component_models/


# region req
class SetGroupBanReq(BaseModel):
    """群禁言请求模型"""

    group_id: GroupID = Field(description="群组ID")
    user_id: UserID = Field(description="用户ID")
    duration: float = Field(description="禁言时长")

    model_config = {
        "extra": "allow",
    }


# region req/


# region res
class SetGroupBanRes(BaseModel):
    """群禁言响应模型"""

    status: str = Field(default="ok", description="状态")
    retcode: float = Field(default=0, description="返回码")
    data: dict | None = Field(default=None, description="数据")
    message: str = Field(default="", description="消息")
    wording: str = Field(default="", description="措辞")
    echo: str | None = Field(default=None, description="回显")

    model_config = {
        "extra": "allow",
    }


# region res/


# region api
class SetGroupBanAPI:
    """set_group_ban接口数据模型"""

    endpoint: str = "set_group_ban"
    method: str = "POST"
    Req = SetGroupBanReq
    Res = SetGroupBanRes
    logger = logging.getLogger(__name__)

    def __call__(self, req: SetGroupBanReq) -> SetGroupBanRes:
        """
        调用API的方法（仅作为接口定义，不包含实际请求逻辑）

        Args:
            req: 请求参数对象

        Returns:
            响应对象
        """
        # 调试日志
        self.logger.debug("调用 SetGroupBanAPI API")
        self.logger.debug(f"请求参数: {req.model_dump_json()}")

        # 注意：这里不应该包含实际的请求逻辑
        # 这个方法只是定义了接口，实际的请求应由适配器或客户端实现
        raise NotImplementedError("此方法需要由实际的API客户端实现")


# region api/
# region code/