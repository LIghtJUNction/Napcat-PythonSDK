# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/283136268e0
@llms.txt: https://napcat.apifox.cn/283136268e0.md
@last_update: 2025-05-28 01:34:11

@description: 

summary:设置群备注

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.43"
__endpoint__ = "set_group_remark"
__id__ = "283136268e0"
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
class SetGroupRemarkReq(BaseModel):
    """设置群备注"""
    group_id: str
    remark: str

    model_config = {
        "extra": "allow",
    }
# region req/


# region res
class SetGroupRemarkRes(BaseModel):
    """设置群备注"""
    class Data(BaseModel):
        """响应数据类型"""
        yes: bool = Field(default=True, description="是否可用")
        reason: str | None = Field(default=None, description="原因")

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
class SetGroupRemarkAPI(BaseModel):
    """set_group_remark接口数据模型"""
    endpoint: str = "set_group_remark"
    method: str = "POST"
    Req: type[BaseModel] = SetGroupRemarkReq
    Res: type[BaseModel] = SetGroupRemarkRes

# region api/
# endregion code

