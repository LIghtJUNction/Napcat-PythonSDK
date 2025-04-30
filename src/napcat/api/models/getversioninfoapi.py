# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: 系统操作
@homepage: https://napcat.apifox.cn/226657087e0
@llms.txt: https://napcat.apifox.cn/226657087e0.md
@last_update: 2025-04-27 00:53:40

@description:

summary:获取版本信息

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.43"
__endpoint__ = "get_version_info"
__id__ = "226657087e0"
__method__ = "POST"

# endregion METADATA


# region code
from pydantic import BaseModel, Field
from typing import Literal

# region req
class GetVersionInfoReq(BaseModel):
    """
    请求模型：获取版本信息
    """
    pass # Request body is empty
# endregion req



# region res
class GetVersionInfoRes(BaseModel):
    """
    响应模型：获取版本信息
    """
    status: Literal["ok"] = Field("ok", description="状态码，固定为 'ok'")
    retcode: int = Field(..., description="返回码") # Assuming retcode is an integer based on common practice
    message: str = Field(..., description="响应消息")
    wording: str = Field(..., description="响应提示")
    echo: str | None = Field(None, description="Echo") # Nullable string, default to None

    class Data(BaseModel):
        """
        响应模型嵌套数据：版本信息详情
        """
        app_name: str = Field(..., description="应用名称")
        protocol_version: str = Field(..., description="协议版本")
        app_version: str = Field(..., description="应用版本")

    data: Data = Field(..., description="版本信息详情")

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