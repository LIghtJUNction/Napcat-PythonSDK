# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/226658789e0
@llms.txt: https://napcat.apifox.cn/226658789e0.md
@last_update: 2025-05-28 01:34:09

@description:

summary:获取群文件系统信息

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.43"
__endpoint__ = "get_group_file_system_info"
__id__ = "226658789e0"
__method__ = "POST"

# endregion METADATA


# region code
from pydantic import BaseModel, Field
from typing import Literal

# region component_models
# 根据OpenAPI规范，group_id在请求体中是一个简单的number或string类型，而非复杂对象。
# `result`组件模型是通用响应模板，此API的响应已自定义，故移除。
# region component_models/

# region req
class GetGroupFileSystemInfoReq(BaseModel):
    """获取群文件系统信息请求"""
    # OpenAPI spec: components/schemas/group_id: oneOf: - type: number - type: string
    group_id: int | str = Field(description="群ID")

    model_config = {
        "extra": "allow",
    }
# region req/


# region res
class GetGroupFileSystemInfoRes(BaseModel):
    """获取群文件系统信息响应"""
    class Data(BaseModel):
        """响应数据类型"""
        # OpenAPI spec: data下的字段是required且类型为number
        file_count: float = Field(description="文件总数")
        limit_count: float = Field(description="文件上限")
        used_space: float = Field(description="已使用空间")
        total_space: float = Field(description="空间上限")

        model_config = {
            "extra": "allow",
        }

    # OpenAPI spec: status字段为const: ok -> Literal["ok"]
    status: Literal["ok"] = Field("ok", description="状态码，固定为 'ok'")
    retcode: float = Field(0.0, description="操作返回码")
    data: Data = Field(default_factory=Data, description="响应数据")
    message: str = Field("", description="错误消息")
    wording: str = Field("", description="错误消息的详细描述")
    echo: str | None = Field(None, description="回显字段")

    model_config = {
        "extra": "allow",
    }
# region res/

# region api
class GetGroupFileSystemInfoAPI(BaseModel):
    """get_group_file_system_info接口数据模型"""
    endpoint: str = "get_group_file_system_info"
    method: str = "POST"
    Req: type[BaseModel] = GetGroupFileSystemInfoReq
    Res: type[BaseModel] = GetGroupFileSystemInfoRes

# region api/
# endregion code