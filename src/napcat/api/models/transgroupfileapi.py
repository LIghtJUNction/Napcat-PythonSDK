# -*- coding: utf-8 -*- 

"""
@tags: 文件相关
@homepage: https://napcat.apifox.cn/283136366e0
@llms.txt: https://napcat.apifox.cn/283136366e0.md
@last_update: 2025-04-25 23:00:50

@description: 

summary:转存为永久文件

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "trans_group_file"
__id__ = "283136366e0"
__method__ = "POST"

# region component_models
from pydantic import BaseModel, Field
from typing import Any


class ResultData(BaseModel):
    ok: bool = Field(..., description="是否成功")


class Result(BaseModel):
    status: str = Field("ok", const=True, description="状态")
    retcode: float = Field(..., description="返回码")
    data: ResultData = Field(..., description="数据")
    message: str = Field(..., description="消息")
    wording: str = Field(..., description="说明")
    echo: str | None = Field(None, description="回显")

    model_config = {
        "extra": "allow",
    }

# region component_models/

# region req
class TransGroupFileReq(BaseModel):
    """转存为永久文件请求体"""
    group_id: str | int = Field(..., description="标识ID")
    file_id: str = Field(..., description="文件ID")

    model_config = {
        "extra": "allow",
    }

# region req/


# region res

class TransGroupFileRes(BaseModel):
    """转存为永久文件响应体"""
    status: str = Field("ok", description="状态")
    retcode: float = Field(0, description="返回码")
    data: dict[str, Any] = Field(..., description="数据")
    message: str = Field("", description="消息")
    wording: str = Field("", description="说明")
    echo: str | None = Field(None, description="回显")

    model_config = {
        "extra": "allow",
    }


# region res/
