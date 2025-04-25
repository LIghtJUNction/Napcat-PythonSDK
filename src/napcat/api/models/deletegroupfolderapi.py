# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/226658779e0
@llms.txt: https://napcat.apifox.cn/226658779e0.md
@last_update: 2025-04-25 23:00:49

@description: 

summary:删除群文件夹

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "delete_group_folder"
__id__ = "226658779e0"
__method__ = "POST"

# region METADATA/


# region code
from pydantic import BaseModel, Field
from typing import Any
import logging

logger = logging.getLogger(__name__)

# region component_models
class GroupId(BaseModel):
    id: str = Field(description="标识ID")
    name: str | None = Field(default=None, description="名称")

    model_config = {
        "extra": "allow",
    }


class ResultData(BaseModel):
    retCode: float = Field(description="retCode字段")
    retMsg: str = Field(description="retMsg字段")
    clientWording: str = Field(description="clientWording字段")

    model_config = {
        "extra": "allow",
    }


class Result(BaseModel):
    status: str = Field(default="ok", const=True, description="status字段, 总是 'ok'")
    retcode: float = Field(default=0, description="retcode字段")
    data: ResultData = Field(description="data字段")
    message: str = Field(default="", description="message字段")
    wording: str = Field(default="", description="wording字段")
    echo: str | None = Field(default=None, description="echo字段")

    model_config = {
        "extra": "allow",
    }


# region component_models/

# region req
class DeleteGroupFolderReq(BaseModel):
    """删除群文件夹"""
    group_id: str | int = Field(description="群组ID，可以是字符串或整数")
    folder_id: str = Field(description="文件夹ID")

    model_config = {
        "extra": "allow",
    }


# region req/


# region res
class DeleteGroupFolderRes(Result):
    """删除群文件夹 响应结果"""

    model_config = {
        "extra": "allow",
    }


# region res/

# region api
class DeleteGroupFolderAPI(BaseModel):
    """delete_group_folder接口数据模型"""
    endpoint: str = Field(default="delete_group_folder", description="API端点")
    method: str = Field(default="POST", description="HTTP方法")
    Req: type[BaseModel] = Field(default=DeleteGroupFolderReq, description="请求模型")
    Res: type[BaseModel] = Field(default=DeleteGroupFolderRes, description="响应模型")
    logger: logging.Logger = Field(default_factory=lambda: logging.getLogger(__name__), description="日志记录器")

    def __init__(self) -> None:
        super().__init__()
        self.logger.debug("初始化 DeleteGroupFolderAPI")

    def __call__(self, req: DeleteGroupFolderReq) -> DeleteGroupFolderRes:
        """
        调用API的方法（仅作为接口定义，不包含实际请求逻辑）

        Args:
            req: 请求参数对象

        Returns:
            响应对象
        """
        # 调试日志
        self.logger.debug(f"调用 DeleteGroupFolderAPI API")
        self.logger.debug(f"请求参数: {req.model_dump_json()}")

        # 注意：这里不应该包含实际的请求逻辑
        # 这个方法只是定义了接口，实际的请求应由适配器或客户端实现
        raise NotImplementedError("此方法需要由实际的API客户端实现")


# region api/
# region code/