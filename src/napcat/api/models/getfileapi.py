# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/226658985e0
@llms.txt: https://napcat.apifox.cn/226658985e0.md
@last_update: 2025-04-25 23:00:49

@description: 

summary:获取文件信息

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "get_file"
__id__ = "226658985e0"
__method__ = "POST"

# region METADATA/


# region code
from pydantic import BaseModel, Field
import logging

logger = logging.getLogger(__name__)

# region component_models
class Result(BaseModel):
    """result model"""
    status: str = Field(default="ok", description="status字段")
    retcode: float = Field(default=0.0, description="retcode字段")
    data: dict[str, any] = Field(default_factory=dict, description="data字段")
    message: str = Field(default="", description="message字段")
    wording: str = Field(default="", description="wording字段")
    echo: str | None = Field(default=None, description="echo字段")

    model_config = {
        "extra": "allow",
    }
# region component_models/

# region req
class GetFileReq(BaseModel):
    """获取文件信息"""
    file_id: str = Field(..., description="文件ID")

    model_config = {
        "extra": "allow",
    }
# region req/


# region res
class GetFileRes(BaseModel):
    """获取文件信息"""

    class ResponseData(BaseModel):
        """响应数据类型"""
        file: str = Field(default="", description="路径或链接")
        url: str = Field(default="", description="路径或链接")
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
class GetFileAPI(BaseModel):
    """get_file接口数据模型"""
    endpoint: str = "get_file"
    method: str = "POST"
    Req: type[BaseModel] = GetFileReq
    Res: type[BaseModel] = GetFileRes
    logger = logging.getLogger(__name__)

    def __init__(self) -> None:
        super().__init__()
        self.logger.debug("初始化 GetFileAPI")

    def __call__(self, req: GetFileReq) -> GetFileRes:
        """
        调用API的方法（仅作为接口定义，不包含实际请求逻辑）
        
        Args:
            req: 请求参数对象
            
        Returns:
            响应对象
        """
        # 调试日志
        self.logger.debug(f"调用 GetFileAPI API")
        self.logger.debug(f"请求参数: {req.model_dump_json()}")
        
        # 注意：这里不应该包含实际的请求逻辑
        # 这个方法只是定义了接口，实际的请求应由适配器或客户端实现
        raise NotImplementedError("此方法需要由实际的API客户端实现")

# region api/
# region code/
