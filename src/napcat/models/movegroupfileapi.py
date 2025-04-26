# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/283136359e0
@llms.txt: https://napcat.apifox.cn/283136359e0.md
@last_update: 2025-04-27 00:53:41

@description: 

summary:移动群文件

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.43"
__endpoint__ = "move_group_file"
__id__ = "283136359e0"
__method__ = "POST"

# endregion METADATA


# region code
from pydantic import BaseModel, Field
from typing import Any
import logging

logger = logging.getLogger(__name__)

# region component_models
class group_id(BaseModel):
    id: str = Field(description="标识ID")
    name: str | None = Field(None, description="名称")

    model_config = {
        "extra": "allow",
    }

class result(BaseModel):
    status: str = Field(description="status字段")
    retcode: float = Field(description="retcode字段")
    data: dict[str, Any] = Field(description="data字段")
    message: str = Field(description="message字段")
    wording: str = Field(description="wording字段")
    echo: str | None = Field(description="echo字段")

    model_config = {
        "extra": "allow",
    }
# region component_models/

# region req
class MoveGroupFileReq(BaseModel):
    """移动群文件"""
    group_id: group_id
    file_id: str
    current_parent_directory: str = Field(description="根目录填  /")
    target_parent_directory: str

    model_config = {
        "extra": "allow",
    }
# region req/


# region res
class MoveGroupFileRes(BaseModel):
    """移动群文件"""
    class Data(BaseModel):
        """响应数据类型"""
        ok: bool = Field(default=None, description="ok字段")

        model_config = {
            "extra": "allow",
        }

    status: str = Field(default="ok", description="status字段")
    retcode: float = Field(default=0, description="retcode字段")
    data: Data = Field(default_factory=lambda: Data(), description="data字段")
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

# region api/
# endregion code

