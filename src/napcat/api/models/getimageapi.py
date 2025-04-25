# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/226657066e0
@llms.txt: https://napcat.apifox.cn/226657066e0.md
@last_update: 2025-04-25 23:00:49

@description: 

summary:获取图片消息详情

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "get_image"
__id__ = "226657066e0"
__method__ = "POST"

# region METADATA/


# region code
from pydantic import BaseModel, Field

import logging

logger = logging.getLogger(__name__)

# region component_models
class Result(BaseModel):
    status: str = Field(default="ok", description="status字段")
    retcode: float = Field(default=0.0, description="retcode字段")

    class Data(BaseModel):
        file: str = Field(default="", description="本地路径")
        url: str = Field(default="", description="网络路径")
        file_size: str = Field(default="", description="文件大小")
        file_name: str = Field(default="", description="文件名")
        base64: str = Field(default="", description="base64字段")

        model_config = {
            "extra": "allow",
        }

    data: Data = Field(default_factory=Data, description="data字段")
    message: str = Field(default="", description="message字段")
    wording: str = Field(default="", description="wording字段")
    echo: str | None = Field(default=None, description="echo字段")

    model_config = {
        "extra": "allow",
    }
# region component_models/

# region req
class GetImageReq(BaseModel):
    """获取图片消息详情"""
    file_id: str = Field(..., description="file_id")

    model_config = {
        "extra": "allow",
    }
# region req/


# region res
class GetImageRes(BaseModel):
    """获取图片消息详情"""
    class ResponseData(BaseModel):
        """响应数据类型"""
        file: str = Field(default="", description="本地路径")
        url: str = Field(default="", description="网络路径")
        file_size: str = Field(default="", description="文件大小")
        file_name: str = Field(default="", description="文件名")
        base64: str = Field(default="", description="base64字段")

        model_config = {
            "extra": "allow",
        }

    status: str = Field(default="ok", description="status字段")
    retcode: float = Field(default=0.0, description="retcode字段")
    data: ResponseData = Field(default_factory=ResponseData, description="data字段")
    message: str = Field(default="", description="message字段")
    wording: str = Field(default="", description="wording字段")
    echo: str | None = Field(default=None, description="echo字段")

    model_config = {
        "extra": "allow",
    }
# region res/

# region api
class GetImageAPI(BaseModel):
    """get_image接口数据模型"""
    endpoint: str = Field(default="get_image", description="endpoint")
    method: str = Field(default="POST", description="method")
    Req: type[BaseModel] = Field(default=GetImageReq, description="Req")
    Res: type[BaseModel] = Field(default=GetImageRes, description="Res")
    logger = logging.getLogger(__name__)

    def __init__(self) -> None:
        super().__init__()
        self.logger.debug("初始化 GetImageAPI")

    def __call__(self, req: GetImageReq) -> GetImageRes:
        """
        调用API的方法（仅作为接口定义，不包含实际请求逻辑）
        
        Args:
            req: 请求参数对象
            
        Returns:
            响应对象
        """
        # 调试日志
        self.logger.debug(f"调用 GetImageAPI API")
        self.logger.debug(f"请求参数: {req.model_dump_json()}")
        
        # 注意：这里不应该包含实际的请求逻辑
        # 这个方法只是定义了接口，实际的请求应由适配器或客户端实现
        raise NotImplementedError("此方法需要由实际的API客户端实现")

# region api/
# region code/