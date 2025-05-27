# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: 消息相关
@homepage: https://napcat.apifox.cn/226657058e0
@llms.txt: https://napcat.apifox.cn/226657058e0.md
@last_update: 2025-05-28 01:34:09

@description: 

summary:获取语音消息详情

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.43"
__endpoint__ = "get_record"
__id__ = "226657058e0"
__method__ = "POST"

# endregion METADATA


# region code
from pydantic import BaseModel, Field
from typing import Literal

# region component_models
# The generic 'result' component model is removed as GetRecordRes directly defines
# its specific 'Data' structure based on the OpenAPI response schema.
# endregion component_models/

# region req
class GetRecordReq(BaseModel):
    """获取语音消息详情"""
    file: str | None = Field(default=None, description="文件路径")
    file_id: str | None = Field(default=None, description="文件ID")
    out_format: Literal["mp3", "amr", "wma", "m4a", "spx", "ogg", "wav", "flac"] = Field(
        description="输出格式，可选值为：mp3, amr, wma, m4a, spx, ogg, wav, flac"
    )

    model_config = {
        "extra": "allow",
    }
# region req/


# region res
class GetRecordRes(BaseModel):
    """获取语音消息详情"""

    class Data(BaseModel):
        """响应数据类型"""
        file: str = Field(description="本地路径")
        url: str = Field(description="网络路径")
        file_size: str = Field(description="文件大小")
        file_name: str = Field(description="文件名")
        base64: str = Field(description="base64编码的语音数据")

        model_config = {
            "extra": "allow",
        }

    status: Literal["ok"] = Field(description="status字段，固定为'ok'")
    retcode: float = Field(description="retcode字段")
    data: Data = Field(default_factory=Data, description="data字段")
    message: str = Field(description="message字段")
    wording: str = Field(description="wording字段")
    echo: str | None = Field(default=None, description="echo字段")

    model_config = {
        "extra": "allow",
    }
# region res/

# region api
class GetRecordAPI(BaseModel):
    """get_record接口数据模型"""
    endpoint: str = "get_record"
    method: str = "POST"
    Req: type[BaseModel] = GetRecordReq
    Res: type[BaseModel] = GetRecordRes

# region api/
# endregion code