# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: 文件相关
@homepage: https://napcat.apifox.cn/266151849e0
@llms.txt: https://napcat.apifox.cn/266151849e0.md
@last_update: 2025-05-28 01:34:11

@description: 

summary:获取私聊文件链接

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.43"
__endpoint__ = "get_private_file_url"
__id__ = "266151849e0"
__method__ = "POST"

# endregion METADATA


# region code
from pydantic import BaseModel, Field
from typing import Literal, Any

# region component_models
class result(BaseModel):
    """通用API响应结构"""
    status: Literal["ok"] = Field(description="API处理状态，固定为'ok'")
    retcode: float = Field(description="API返回码，0表示成功，非0表示错误")
    data: dict[str, Any] = Field(description="响应数据体")
    message: str = Field(description="API处理消息，通常用于描述成功或错误信息")
    wording: str = Field(description="API提示信息，通常用于用户界面展示")
    echo: str | None = Field(description="回显字段，通常用于客户端请求的标识，可为空")

    model_config = {
        "extra": "allow",
    }
# region component_models/

# region req
class GetPrivateFileUrlReq(BaseModel):
    """获取私聊文件链接请求"""
    file_id: str = Field(description="文件ID")

    model_config = {
        "extra": "allow",
    }
# region req/


# region res
class GetPrivateFileUrlRes(BaseModel):
    """获取私聊文件链接响应"""
    class Data(BaseModel):
        """响应数据体"""
        url: str = Field(description="私聊文件的下载链接")

        model_config = {
            "extra": "allow",
        }

    status: Literal["ok"] = Field(default="ok", description="API处理状态，固定为'ok'")
    retcode: float = Field(default=0, description="API返回码，0表示成功")
    data: Data = Field(default_factory=Data, description="私聊文件链接的响应数据")
    message: str = Field(default="", description="API处理消息")
    wording: str = Field(default="", description="API提示信息")
    echo: str | None = Field(default=None, description="回显字段，可为空")

    model_config = {
        "extra": "allow",
    }
# region res/

# region api
class GetPrivateFileUrlAPI(BaseModel):
    """get_private_file_url接口数据模型"""
    endpoint: str = "get_private_file_url"
    method: str = "POST"
    Req: type[BaseModel] = GetPrivateFileUrlReq
    Res: type[BaseModel] = GetPrivateFileUrlRes

# region api/
# endregion code
