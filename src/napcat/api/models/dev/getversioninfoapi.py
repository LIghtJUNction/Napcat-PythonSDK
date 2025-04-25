# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: 系统操作
@homepage: https://napcat.apifox.cn/226657087e0
@llms.txt: https://napcat.apifox.cn/226657087e0.md
@last_update: 2025-04-26 01:17:44

@description: 

summary:获取版本信息

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "get_version_info"
__id__ = "226657087e0"
__method__ = "POST"

# endregion METADATA


# region code
from pydantic import BaseModel, Field
from typing import Literal # Import Literal for const="ok"

# region req
class GetVersionInfoReq(BaseModel): # type: ignore
    """
    {{DESC_EndPointReq}}
    """
    # Request body is empty according to the OpenAPI spec
    pass
# endregion req



# region res
class GetVersionInfoRes(BaseModel):
    """
    {{DESC_EndPointRes}}
    """

    # Define the nested Data model as per the OpenAPI spec
    class Data(BaseModel):
        app_name: str = Field(..., description="应用名称")
        protocol_version: str = Field(..., description="协议版本")
        app_version: str = Field(..., description="应用版本")

    # Define the main response fields based on the OpenAPI spec
    status: Literal["ok"] = Field(
        ..., description="状态", const="ok"
    ) # Use Literal for the const value
    retcode: int = Field(..., description="返回码") # Assuming integer for retcode
    data: Data = Field(..., description="响应数据") # Use the nested Data model
    message: str = Field(..., description="消息")
    wording: str = Field(..., description="词语")
    echo: str | None = Field(..., description="回显") # Use | None for nullable

# endregion res

# region api
class GetVersionInfoAPI(BaseModel):
    """get_version_info接口数据模型"""
    endpoint: str = "get_version_info"
    method: str = "POST"
    Req: type[BaseModel] = GetVersionInfoReq
    Res: type[BaseModel] = GetVersionInfoRes
# endregion api




# endregion code
