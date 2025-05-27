# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/226658985e0
@llms.txt: https://napcat.apifox.cn/226658985e0.md
@last_update: 2025-05-28 01:34:09

@description: 

summary:获取文件信息

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.43"
__endpoint__ = "get_file"
__id__ = "226658985e0"
__method__ = "POST"

# endregion METADATA


# region code
from pydantic import BaseModel, Field
from typing import Any
import logging

logger = logging.getLogger(__name__)

# region component_models
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
class GetFileReq(BaseModel):
    """获取文件信息"""
    file_id: str | None = Field(None, description="二选一")
    file: str | None = Field(None, description="二选一")

    model_config = {
        "extra": "allow",
    }
# region req/


# region res
class GetFileRes(BaseModel):
    """获取文件信息"""
    class Data(BaseModel):
        """响应数据类型"""
        file: str = Field(default=None, description="路径或链接")
        url: str = Field(default=None, description="路径或链接")
        file_size: str = Field(default=None, description="文件大小")
        file_name: str = Field(default=None, description="文件名")
        base64: str = Field(default=None, description="base64字段")

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
class GetFileAPI(BaseModel):
    """get_file接口数据模型"""
    endpoint: str = "get_file"
    method: str = "POST"
    Req: type[BaseModel] = GetFileReq
    Res: type[BaseModel] = GetFileRes

# region api/
# endregion code

