# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/226658965e0
@llms.txt: https://napcat.apifox.cn/226658965e0.md
@last_update: 2025-04-25 23:00:49

@description: 

summary:获取推荐好友/群聊卡片

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "ArkSharePeer"
__id__ = "226658965e0"
__method__ = "POST"

# region METADATA/


# region code
from pydantic import BaseModel, Field
import logging

logger = logging.getLogger(__name__)

# region component_models
class UserId(BaseModel):
    id: str = Field(description="标识ID")
    name: str | None = Field(default=None, description="名称")

    model_config = {
        "extra": "allow",
    }


class GroupId(BaseModel):
    id: str = Field(description="标识ID")
    name: str | None = Field(default=None, description="名称")

    model_config = {
        "extra": "allow",
    }


class ResultData(BaseModel):
    errCode: float = Field(description="errCode字段")
    errMsg: str = Field(description="errMsg字段")
    arkJson: str = Field(description="卡片json")

    model_config = {
        "extra": "allow",
    }


class Result(BaseModel):
    status: str = Field(default="ok", description="status字段")
    retcode: float = Field(description="retcode字段")
    data: ResultData = Field(description="data字段")
    message: str = Field(description="message字段")
    wording: str = Field(description="wording字段")
    echo: str | None = Field(default=None, description="echo字段")

    model_config = {
        "extra": "allow",
    }

# region component_models/

# region req
class ArksharepeerReq(BaseModel):
    """获取推荐好友/群聊卡片"""
    group_id: GroupId | None = Field(default=None, description="和user_id二选一")
    user_id: UserId | None = Field(default=None, description="和group_id二选一")
    phoneNumber: str | None = Field(default=None, description="对方手机号")

    model_config = {
        "extra": "allow",
    }

# region req/


# region res
class ArksharepeerRes(BaseModel):
    """获取推荐好友/群聊卡片"""

    status: str = Field(default="ok", description="status字段")
    retcode: float = Field(default=0, description="retcode字段")
    data: ResultData = Field(description="data字段")
    message: str = Field(default="", description="message字段")
    wording: str = Field(default="", description="wording字段")
    echo: str | None = Field(default=None, description="echo字段")

    model_config = {
        "extra": "allow",
    }

# region res/

# region api
class ArksharepeerAPI(BaseModel):
    """ArkSharePeer接口数据模型"""
    endpoint: str = Field(default="ArkSharePeer", description="endpoint")
    method: str = Field(default="POST", description="method")
    Req: type[BaseModel] = Field(default=ArksharepeerReq, description="请求模型")
    Res: type[BaseModel] = Field(default=ArksharepeerRes, description="响应模型")
    logger = logger

    def __call__(self, req: ArksharepeerReq) -> ArksharepeerRes:
        """
        调用API的方法（仅作为接口定义，不包含实际请求逻辑）

        Args:
            req: 请求参数对象

        Returns:
            响应对象
        """
        # 调试日志
        self.logger.debug(f"调用 ArksharepeerAPI API")
        self.logger.debug(f"请求参数: {req.model_dump_json()}")

        # 注意：这里不应该包含实际的请求逻辑
        # 这个方法只是定义了接口，实际的请求应由适配器或客户端实现
        raise NotImplementedError("此方法需要由实际的API客户端实现")

# region api/
# region code/