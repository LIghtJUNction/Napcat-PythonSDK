# -*- coding: utf-8 -*- 
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/226659254e0
@llms.txt: https://napcat.apifox.cn/226659254e0.md
@last_update: 2025-04-25 23:00:50

@description: 

summary:fetch_user_profile_like

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "fetch_user_profile_like"
__id__ = "226659254e0"
__method__ = "POST"

# region METADATA/


# region code
from pydantic import BaseModel, Field
import logging

logger = logging.getLogger(__name__)

# region component_models
class UserID(BaseModel):
    id: str | int = Field(description="标识ID")

    model_config = {
        "extra": "allow",
    }


class Result(BaseModel):
    status: str = Field(default="ok", const=True, description="status字段")
    retcode: float = Field(description="retcode字段")
    data: dict = Field(default_factory=dict, description="data字段")
    message: str = Field(description="message字段")
    wording: str = Field(description="wording字段")
    echo: str | None = Field(None, description="echo字段")

    model_config = {
        "extra": "allow",
    }
# region component_models/

# region req
class FetchUserProfileLikeReq(BaseModel):
    """fetch_user_profile_like"""
    user_id: UserID = Field(description="用户ID")

    model_config = {
        "extra": "allow",
    }
# region req/


# region res
class FetchUserProfileLikeRes(Result):
    """fetch_user_profile_like"""
    pass
# region res/

# region api
class FetchUserProfileLikeAPI(BaseModel):
    """fetch_user_profile_like接口数据模型"""
    endpoint: str = "fetch_user_profile_like"
    method: str = "POST"
    Req: type[BaseModel] = FetchUserProfileLikeReq
    Res: type[BaseModel] = FetchUserProfileLikeRes
    logger = logging.getLogger(__name__)

    def __init__(self) -> None:
        super().__init__()
        self.logger.debug("初始化 FetchUserProfileLikeAPI")

    def __call__(self, req: FetchUserProfileLikeReq) -> FetchUserProfileLikeRes:
        """
        调用API的方法（仅作为接口定义，不包含实际请求逻辑）
        
        Args:
            req: 请求参数对象
            
        Returns:
            响应对象
        """
        # 调试日志
        self.logger.debug(f"调用 FetchUserProfileLikeAPI API")
        self.logger.debug(f"请求参数: {req.model_dump_json()}")
        
        # 注意：这里不应该包含实际的请求逻辑
        # 这个方法只是定义了接口，实际的请求应由适配器或客户端实现
        raise NotImplementedError("此方法需要由实际的API客户端实现")

# region api/
# region code/