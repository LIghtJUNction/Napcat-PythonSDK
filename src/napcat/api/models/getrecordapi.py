# -*- coding: utf-8 -*- 

"""
@tags: ['消息相关']
@homepage: https://napcat.apifox.cn/226657058e0
@llms.txt: https://napcat.apifox.cn/226657058e0.md
@last_update: 2025-04-25 23:00:49

@description: 获取语音消息详情

summary: 获取语音消息详情

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "get_record"
__id__ = "226657058e0"
__method__ = "POST"

# region code
from pydantic import BaseModel, Field
import logging
from enum import Enum

logger = logging.getLogger(__name__)

# region req
class OutFormatEnum(str, Enum):
    MP3 = "mp3"
    AMR = "amr"
    WMA = "wma"
    M4A = "m4a"
    SPX = "spx"
    OGG = "ogg"
    WAV = "wav"
    FLAC = "flac"

class GetRecordReq(BaseModel):
    """获取语音消息详情的请求参数"""
    file: str = Field(..., description="文件标识符")
    out_format: OutFormatEnum = Field(..., description="输出格式")

    model_config = {
        "extra": "allow",
    }
# region req/


# region res
class GetRecordRes(BaseModel):
    """获取语音消息详情的响应"""
    class ResponseData(BaseModel):
        """响应数据类型"""
        file: str = Field(..., description="本地路径")
        url: str = Field(..., description="网络路径")
        file_size: str = Field(..., description="文件大小")
        file_name: str = Field(..., description="文件名")
        base64: str = Field(..., description="base64字段")

        model_config = {
            "extra": "allow",
        }

    status: str = Field(default="ok", description="状态")
    retcode: float = Field(default=0, description="返回码")
    data: ResponseData = Field(..., description="数据")
    message: str = Field(default="", description="消息")
    wording: str = Field(default="", description="说明")
    echo: str | None = Field(default=None, description="回显")

    model_config = {
        "extra": "allow",
    }
# region res/

# region component_models
class Result(BaseModel):
    status: str = Field(const="ok", description="status字段")
    retcode: float = Field(..., description="retcode字段")
    data: dict[str, any] = Field(..., description="data字段")
    message: str = Field(..., description="message字段")
    wording: str = Field(..., description="wording字段")
    echo: str | None = Field(description="echo字段")

    model_config = {
        "extra": "allow",
    }
# region component_models/

# region api
class GetRecordAPI(BaseModel):
    """get_record接口数据模型"""
    endpoint: str = "get_record"
    method: str = "POST"
    Req: type[BaseModel] = GetRecordReq
    Res: type[BaseModel] = GetRecordRes
    logger = logging.getLogger(__name__)

    def __init__(self) -> None:
        super().__init__()
        self.logger.debug("初始化 GetRecordAPI")

    def __call__(self, req: GetRecordReq) -> GetRecordRes:
        """
        调用API的方法（仅作为接口定义，不包含实际请求逻辑）
        
        Args:
            req: 请求参数对象
            
        Returns:
            响应对象
        """
        # 调试日志
        self.logger.debug(f"调用 GetRecordAPI API")
        self.logger.debug(f"请求参数: {req.model_dump_json()}")
        
        # 注意：这里不应该包含实际的请求逻辑
        # 这个方法只是定义了接口，实际的请求应由适配器或客户端实现
        raise NotImplementedError("此方法需要由实际的API客户端实现")

# region api/
# region code/