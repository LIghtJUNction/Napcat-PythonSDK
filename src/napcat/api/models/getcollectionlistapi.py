# -*- coding: utf-8 -*- 
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/226659182e0
@llms.txt: https://napcat.apifox.cn/226659182e0.md
@last_update: 2025-04-25 23:00:49

@description: 

summary:获取收藏列表

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "get_collection_list"
__id__ = "226659182e0"
__method__ = "POST"

# region METADATA/


# region code
from pydantic import BaseModel, Field
import logging

logger = logging.getLogger(__name__)

# region component_models
class Result(BaseModel):
    """通用结果模型"""
    status: str = Field(default="ok", description="status字段")
    retcode: float = Field(default=0.0, description="retcode字段")
    data: dict[str, str] = Field(default_factory=dict, description="data字段")
    message: str = Field(default="", description="message字段")
    wording: str = Field(default="", description="wording字段")
    echo: str | None = Field(default=None, description="echo字段")

    model_config = {
        "extra": "allow",
    }
# region component_models/

# region req
class GetCollectionListReq(BaseModel):
    """获取收藏列表请求参数"""
    category: str = Field(..., description="分类")
    count: str = Field(..., description="数量")

    model_config = {
        "extra": "allow",
    }
# region req/


# region res
class GetCollectionListRes(BaseModel):
    """获取收藏列表响应"""
    class ResponseData(BaseModel):
        """响应数据类型"""
        yes: bool = Field(default=True, description="是否可用")
        reason: str | None = Field(default=None, description="原因")

        model_config = {
            "extra": "allow",
        }

    status: str = Field(default="ok", description="status字段")
    retcode: float = Field(default=0.0, description="retcode字段")
    data: list[str] = Field(default_factory=list, description="data字段")
    message: str = Field(default="", description="message字段")
    wording: str = Field(default="", description="wording字段")
    echo: str | None = Field(default=None, description="echo字段")

    model_config = {
        "extra": "allow",
    }
# region res/

# region api
class GetCollectionListAPI(BaseModel):
    """get_collection_list接口数据模型"""
    endpoint: str = "get_collection_list"
    method: str = "POST"
    Req: type[BaseModel] = GetCollectionListReq
    Res: type[BaseModel] = GetCollectionListRes
    logger = logging.getLogger(__name__)

    def __init__(self) -> None:
        super().__init__()
        self.logger.debug("初始化 GetCollectionListAPI")

    def __call__(self, req: GetCollectionListReq) -> GetCollectionListRes:
        """
        调用API的方法（仅作为接口定义，不包含实际请求逻辑）
        
        Args:
            req: 请求参数对象
            
        Returns:
            响应对象
        """
        # 调试日志
        self.logger.debug(f"调用 GetCollectionListAPI API")
        self.logger.debug(f"请求参数: {req.model_dump_json()}")
        
        # 注意：这里不应该包含实际的请求逻辑
        # 这个方法只是定义了接口，实际的请求应由适配器或客户端实现
        raise NotImplementedError("此方法需要由实际的API客户端实现")

# region api/
# region code/