# -*- coding: utf-8 -*- 
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/227233981e0
@llms.txt: https://napcat.apifox.cn/227233981e0.md
@last_update: 2025-04-25 23:00:50

@description: 

summary:_获取在线机型

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "_get_model_show"
__id__ = "227233981e0"
__method__ = "POST"

# region METADATA/


# region code
from pydantic import BaseModel, Field
import logging

logger = logging.getLogger(__name__)

# region component_models

# 定义 ResultData 模型
class ResultData(BaseModel): 
    variants: list[dict[str, str | bool]] = Field(default_factory=list, description="Variants data")

class Result(BaseModel):
    status: str = Field(default="ok", description="status字段")
    retcode: float = Field(default=0.0, description="retcode字段")
    data: list[ResultData] = Field(default_factory=list, description="data字段")
    message: str = Field(default="", description="message字段")
    wording: str = Field(default="", description="wording字段")
    echo: str | None = Field(default=None, description="echo字段")

    model_config = {
        "extra": "allow",
    }
# region component_models/

# region req
class GetModelShowReq(BaseModel):
    """_获取在线机型"""
    model: str = Field(..., description="Model name")

    model_config = {
        "extra": "allow",
    }
# region req/


# region res
class GetModelShowRes(BaseModel):
    """_获取在线机型"""
    class ResponseData(BaseModel):
        """响应数据类型"""
        yes: bool = Field(default=True, description="是否可用")
        reason: str | None = Field(default=None, description="原因")

        model_config = {
            "extra": "allow",
        }

    status: str = Field(default="ok", description="status字段")
    retcode: float = Field(default=0.0, description="retcode字段")
    data: list[dict[str, dict[str, str | bool]]] = Field(default_factory=list, description="data字段")
    message: str = Field(default="", description="message字段")
    wording: str = Field(default="", description="wording字段")
    echo: str | None = Field(default=None, description="echo字段")

    model_config = {
        "extra": "allow",
    }
# region res/

# region api
class GetModelShowAPI(BaseModel):
    """_get_model_show接口数据模型"""
    endpoint: str = Field(default="_get_model_show", description="Endpoint")
    method: str = Field(default="POST", description="HTTP Method")
    Req: type[BaseModel] = Field(default=GetModelShowReq, description="Request Model")
    Res: type[BaseModel] = Field(default=Result, description="Response Model")
    logger: logging.Logger = Field(default_factory=lambda: logging.getLogger(__name__), description="Logger")

    def __init__(self) -> None:
        super().__init__()
        self.logger.debug("初始化 GetModelShowAPI")

    def __call__(self, req: GetModelShowReq) -> Result:
        """
        调用API的方法（仅作为接口定义，不包含实际请求逻辑）
        
        Args:
            req: 请求参数对象
            
        Returns:
            响应对象
        """
        # 调试日志
        self.logger.debug(f"调用 GetModelShowAPI API")
        self.logger.debug(f"请求参数: {req.model_dump_json()}")
        
        # 注意：这里不应该包含实际的请求逻辑
        # 这个方法只是定义了接口，实际的请求应由适配器或客户端实现
        raise NotImplementedError("此方法需要由实际的API客户端实现")

# region api/
# region code/
