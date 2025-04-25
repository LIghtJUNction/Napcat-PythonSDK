# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/283136375e0
@llms.txt: https://napcat.apifox.cn/283136375e0.md
@last_update: 2025-04-25 23:00:50

@description: 

summary:重命名群文件

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "rename_group_file"
__id__ = "283136375e0"
__method__ = "POST"

# region METADATA/


# region code
from pydantic import BaseModel, Field
import logging

logger = logging.getLogger(__name__)

# region component_models
class GroupId(BaseModel):
    """群组ID模型"""
    id: str | int = Field(description="标识ID")
    name: str | None = Field(None, description="名称")

    model_config = {
        "extra": "allow",
    }


# region component_models/

# region req
class RenameGroupFileReq(BaseModel):
    """重命名群文件请求模型"""
    group_id: GroupId = Field(description="群组ID")
    file_id: str = Field(description="文件ID")
    current_parent_directory: str = Field(description="当前父目录")
    new_name: str = Field(description="新文件名")

    model_config = {
        "extra": "allow",
    }


# region req/


# region res
class RenameGroupFileRes(BaseModel):
    """重命名群文件响应模型"""

    class ResponseData(BaseModel):
        """响应数据类型"""
        ok: bool = Field(description="ok字段")

        model_config = {
            "extra": "allow",
        }

    status: str = Field(default="ok", description="status字段")
    retcode: float = Field(default=0, description="retcode字段")
data: ResponseData = Field(description="data字段")
    message: str = Field(default="", description="message字段")
    wording: str = Field(default="", description="wording字段")
    echo: str | None = Field(default=None, description="echo字段")

    model_config = {
        "extra": "allow",
    }


# region res/

# region api
class RenameGroupFileAPI(BaseModel):
    """rename_group_file接口数据模型"""
    endpoint: str = "rename_group_file"
    method: str = "POST"
    Req: type[BaseModel] = RenameGroupFileReq
    Res: type[BaseModel] = RenameGroupFileRes
    logger = logging.getLogger(__name__)

    def __init__(self) -> None:
        super().__init__()
        self.logger.debug("初始化 RenameGroupFileAPI")

    def __call__(self, req: RenameGroupFileReq) -> RenameGroupFileRes:
        """
        调用API的方法（仅作为接口定义，不包含实际请求逻辑）

        Args:
            req: 请求参数对象

        Returns:
            响应对象
        """
        # 调试日志
        self.logger.debug(f"调用 RenameGroupFileAPI API")
        self.logger.debug(f"请求参数: {req.model_dump_json()}")

        # 注意：这里不应该包含实际的请求逻辑
        # 这个方法只是定义了接口，实际的请求应由适配器或客户端实现
        raise NotImplementedError("此方法需要由实际的API客户端实现")


# region api/
# region code/