# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/226658669e0
@llms.txt: https://napcat.apifox.cn/226658669e0.md
@last_update: 2025-04-25 23:00:49

@description: 

summary:设置群头像

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "set_group_portrait"
__id__ = "226658669e0"
__method__ = "POST"

# region METADATA/


# region code
from pydantic import BaseModel, Field
from typing import Any


# region component_models
class GroupId(BaseModel):
    group_id: str | int = Field(description="标识ID")

    model_config = {
        "extra": "allow",
    }


class ResultData(BaseModel):
    result: str = Field(..., description="Result字段")
    errMsg: str = Field(..., description="ErrMsg字段")

    model_config = {
        "extra": "allow",
    }


class Result(BaseModel):
    status: str = Field("ok", const=True, description="Status字段")
    retcode: float = Field(0, description="Retcode字段")
    data: ResultData = Field(..., description="Data字段")
    message: str = Field("", description="Message字段")
    wording: str = Field("", description="Wording字段")
    echo: str | None = Field(None, description="Echo字段")

    model_config = {
        "extra": "allow",
    }


# region component_models/

# region req
class SetGroupPortraitReq(BaseModel):
    """设置群头像"""
    group_id: GroupId
    file: str = Field(description="文件路径")

    model_config = {
        "extra": "allow",
    }


# region req/


# region res
class SetGroupPortraitRes(BaseModel):
    """设置群头像"""
    status: str = Field("ok", description="Status字段")
    retcode: float = Field(0, description="Retcode字段")
    data: ResultData = Field(description="Data字段")
    message: str = Field("", description="Message字段")
    wording: str = Field("", description="Wording字段")
    echo: str | None = Field(None, description="Echo字段")

    model_config = {
        "extra": "allow",
    }


# region res/

# region api
# class SetGroupPortraitAPI(BaseModel):
#     """set_group_portrait接口数据模型"""
#     endpoint: str = "set_group_portrait"
#     method: str = "POST"
#     Req: type[BaseModel] = SetGroupPortraitReq
#     Res: type[BaseModel] = SetGroupPortraitRes
#     logger = logging.getLogger(__name__)
#
#     def __init__(self) -> None:
#         super().__init__()
#         self.logger.debug("初始化 SetGroupPortraitAPI")
#
#     def __call__(self, req: SetGroupPortraitReq) -> SetGroupPortraitRes:
#         """
#         调用API的方法（仅作为接口定义，不包含实际请求逻辑）
#
#         Args:
#             req: 请求参数对象
#
#         Returns:
#             响应对象
#         """
#         # 调试日志
#         self.logger.debug(f"调用 SetGroupPortraitAPI API")
#         self.logger.debug(f"请求参数: {req.model_dump_json()}")
#
#         # 注意：这里不应该包含实际的请求逻辑
#         # 这个方法只是定义了接口，实际的请求应由适配器或客户端实现
#         raise NotImplementedError("此方法需要由实际的API客户端实现")

# region api/
# region code/