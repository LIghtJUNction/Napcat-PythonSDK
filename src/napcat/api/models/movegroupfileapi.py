# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: 文件相关
@homepage: https://napcat.apifox.cn/283136359e0
@llms.txt: https://napcat.apifox.cn/283136359e0.md
@last_update: 2025-04-25 23:00:50

@description: 移动群文件

summary:移动群文件

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "move_group_file"
__id__ = "283136359e0"
__method__ = "POST"

# region METADATA/


# region code
from pydantic import BaseModel, Field
from typing import Any
import logging

logger = logging.getLogger(__name__)

# region component_models
class GroupId(BaseModel):
    """群组ID，可以是数字或字符串"""
    group_id: int | str = Field(description="标识ID")

    model_config = {
        "extra": "allow",
    }


class Result(BaseModel):
    """通用结果返回模型"""
    status: str = Field(default="ok", const=True, description="状态，固定为ok")
    retcode: float = Field(default=0, description="返回码")
    data: dict[str, Any] = Field(default_factory=dict, description="数据")
    message: str = Field(default="", description="消息")
    wording: str = Field(default="", description="提示语")
    echo: str | None = Field(default=None, description="回显数据")

    model_config = {
        "extra": "allow",
    }


# region component_models/

# region req
class MoveGroupFileReq(BaseModel):
    """移动群文件请求参数"""
    group_id: GroupId = Field(description="群组ID")
    file_id: str = Field(description="文件ID")
    current_parent_directory: str = Field(description="当前父目录")
    target_parent_directory: str = Field(description="目标父目录")

    model_config = {
        "extra": "allow",
    }


# region req/


# region res
class MoveGroupFileRes(BaseModel):
    """移动群文件响应结果"""

    class ResponseData(BaseModel):
        """响应数据类型"""
        ok: bool = Field(description="操作是否成功")

        model_config = {
            "extra": "allow",
        }

    status: str = Field(default="ok", description="status字段")
    retcode: float = Field(default=0, description="retcode字段")
    data: ResponseData = Field(default_factory=ResponseData, description="data字段")
    message: str = Field(default="", description="message字段")
    wording: str = Field(default="", description="wording字段")
    echo: str | None = Field(default=None, description="echo字段")

    model_config = {
        "extra": "allow",
    }


# region res/

# region api
class MoveGroupFileAPI(BaseModel):
    """move_group_file接口数据模型"""
    endpoint: str = "move_group_file"
    method: str = "POST"
    Req: type[BaseModel] = MoveGroupFileReq
    Res: type[BaseModel] = MoveGroupFileRes
    logger: logging.Logger = Field(default_factory=lambda: logging.getLogger(__name__))

    def __init__(self) -> None:
        super().__init__()
        self.logger.debug("初始化 MoveGroupFileAPI")

    def __call__(self, req: MoveGroupFileReq) -> MoveGroupFileRes:
        """
        调用API的方法（仅作为接口定义，不包含实际请求逻辑）

        Args:
            req: 请求参数对象

        Returns:
            响应对象
        """
        # 调试日志
        self.logger.debug(f"调用 MoveGroupFileAPI API")
        self.logger.debug(f"请求参数: {req.model_dump_json()}")

        # 注意：这里不应该包含实际的请求逻辑
        # 这个方法只是定义了接口，实际的请求应由适配器或客户端实现
        raise NotImplementedError("此方法需要由实际的API客户端实现")


# region api/
# region code/
