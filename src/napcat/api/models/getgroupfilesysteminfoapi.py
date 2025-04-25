# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: 文件相关
@homepage: https://napcat.apifox.cn/226658789e0
@llms.txt: https://napcat.apifox.cn/226658789e0.md
@last_update: 2025-04-25 23:00:49

@description: 

summary:获取群文件系统信息

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "get_group_file_system_info"
__id__ = "226658789e0"
__method__ = "POST"

# region METADATA/


# region code
from pydantic import BaseModel, Field
from typing import Any
import logging

logger = logging.getLogger(__name__)

# region component_models
class GroupId(BaseModel):
    group_id: str | int = Field(description="群ID，可以是字符串或数字")

    model_config = {
        "extra": "allow",
    }


class ResultData(BaseModel):
    file_count: float = Field(description="文件总数")
    limit_count: float = Field(description="文件上限")
    used_space: float = Field(description="已使用空间")
    total_space: float = Field(description="空间上限")

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
class GetGroupFileSystemInfoReq(BaseModel):
    """获取群文件系统信息请求模型"""
    group_id: GroupId = Field(description="群ID信息")

    model_config = {
        "extra": "allow",
    }


# region req/


# region res
class GetGroupFileSystemInfoRes(BaseModel):
    """获取群文件系统信息响应模型"""
    status: str = Field(default="ok", description="status字段")
    retcode: float = Field(default=0.0, description="retcode字段")
    data: ResultData = Field(description="data字段")
    message: str = Field(default="", description="message字段")
    wording: str = Field(default="", description="wording字段")
    echo: str | None = Field(default=None, description="echo字段")

    model_config = {
        "extra": "allow",
    }


# region res/

# region api
class GetGroupFileSystemInfoAPI(BaseModel):
    """get_group_file_system_info接口数据模型"""
    endpoint: str = Field(default="get_group_file_system_info", description="Endpoint")
    method: str = Field(default="POST", description="HTTP方法")
    Req: type[BaseModel] = Field(default=GetGroupFileSystemInfoReq, description="请求模型")
    Res: type[BaseModel] = Field(default=GetGroupFileSystemInfoRes, description="响应模型")

    logger: logging.Logger = Field(default_factory=lambda: logging.getLogger(__name__), description="日志记录器")

    def __call__(self, req: GetGroupFileSystemInfoReq) -> GetGroupFileSystemInfoRes:
        """
        调用API的方法（仅作为接口定义，不包含实际请求逻辑）

        Args:
            req: 请求参数对象

        Returns:
            响应对象
        """
        # 调试日志
        self.logger.debug(f"调用 GetGroupFileSystemInfoAPI API")
        self.logger.debug(f"请求参数: {req.model_dump_json()}")

        # 注意：这里不应该包含实际的请求逻辑
        # 这个方法只是定义了接口，实际的请求应由适配器或客户端实现
        raise NotImplementedError("此方法需要由实际的API客户端实现")

# region api/
# region code/