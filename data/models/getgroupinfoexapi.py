# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/226659229e0
@llms.txt: https://napcat.apifox.cn/226659229e0.md
@last_update: 2025-05-28 01:34:10

@description: 

summary:获取群信息ex

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.43"
__endpoint__ = "get_group_info_ex"
__id__ = "226659229e0"
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
# region component_models/

# region req
class GetGroupInfoExReq(BaseModel):
    """获取群信息ex"""
    group_id: group_id

    model_config = {
        "extra": "allow",
    }
# region req/


# region res
class GetGroupInfoExRes(BaseModel):
    """获取群信息ex"""
    class Data(BaseModel):
        """响应数据类型"""
        groupCode: str = Field(default=None, description="groupCode字段")
        resultCode: float = Field(default=None, description="resultCode字段")
        extInfo: Extinfo = Field(default=None, description="extInfo字段")

        model_config = {
            "extra": "allow",
        }

    status: str = Field(default="ok", description="status字段")
    retcode: float = Field(default=0, description="retcode字段")
    data: Data = Field(default_factory=lambda: Data(), description="data字段")
    message: str = Field(default="", description="message字段")
    wording: str = Field(default="", description="wording字段")
    echo: None | None = Field(default=None, description="echo字段")

    model_config = {
        "extra": "allow",
    }
# region res/

# region api
class GetGroupInfoExAPI(BaseModel):
    """get_group_info_ex接口数据模型"""
    endpoint: str = "get_group_info_ex"
    method: str = "POST"
    Req: type[BaseModel] = GetGroupInfoExReq
    Res: type[BaseModel] = GetGroupInfoExRes

# region api/
# endregion code

