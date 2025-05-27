# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/226659178e0
@llms.txt: https://napcat.apifox.cn/226659178e0.md
@last_update: 2025-05-28 01:34:10

@description: 

summary:创建收藏

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.43"
__endpoint__ = "create_collection"
__id__ = "226659178e0"
__method__ = "POST"

# endregion METADATA


# region code
from pydantic import BaseModel, Field
from typing import Any, Literal
import logging

logger = logging.getLogger(__name__)

# region component_models
class result(BaseModel):
    status: Literal["ok"] = Field(description="status字段")
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
class CreateCollectionReq(BaseModel):
    """创建收藏"""
    rawData: str = Field(description="内容")
    brief: str = Field(description="标题")

    model_config = {
        "extra": "allow",
    }
# region req/


# region res
class CreateCollectionRes(BaseModel):
    """创建收藏"""
    class Data(BaseModel):
        """响应数据类型"""
        result: float = Field(description="result字段")
        errMsg: str = Field(description="errMsg字段")

        model_config = {
            "extra": "allow",
        }

    status: Literal["ok"] = Field(description="status字段")
    retcode: float = Field(description="retcode字段")
    data: Data = Field(description="data字段")
    message: str = Field(description="message字段")
    wording: str = Field(description="wording字段")
    echo: str | None = Field(default=None, description="echo字段")

    model_config = {
        "extra": "allow",
    }
# region res/

# region api
class CreateCollectionAPI(BaseModel):
    """create_collection接口数据模型"""
    endpoint: str = "create_collection"
    method: str = "POST"
    Req: type[BaseModel] = CreateCollectionReq
    Res: type[BaseModel] = CreateCollectionRes

# region api/
# endregion code
