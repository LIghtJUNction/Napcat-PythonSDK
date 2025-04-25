# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: 群聊相关
@homepage: https://napcat.apifox.cn/226657019e0
@llms.txt: https://napcat.apifox.cn/226657019e0.md
@last_update: 2025-04-25 23:00:49

@description: 

summary:获取群成员信息

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "get_group_member_info"
__id__ = "226657019e0"
__method__ = "POST"

# region METADATA/


# region code
from pydantic import BaseModel, Field
import logging

logger = logging.getLogger(__name__)

# region component_models
class UserId(BaseModel):
    id: str | int = Field(description="标识ID")
    # name: str | None = Field(None, description="名称") # 在openapi定义中，user_id没有name字段

    model_config = {
        "extra": "allow",
    }

class GroupId(BaseModel):
    id: str | int = Field(description="标识ID")
    # name: str | None = Field(None, description="名称") # 在openapi定义中，group_id没有name字段

    model_config = {
        "extra": "allow",
    }

class Result(BaseModel):
    status: str = Field(default="ok", description="status字段")
    retcode: float = Field(description="retcode字段")
    data: dict[str, any] = Field(default_factory=dict, description="data字段")
    message: str = Field(description="message字段")
    wording: str = Field(description="wording字段")
    echo: str | None = Field(default=None, description="echo字段")

    model_config = {
        "extra": "allow",
    }
# region component_models/

# region req
class GetGroupMemberInfoReq(BaseModel):
    """获取群成员信息"""
    group_id: GroupId = Field(description="群组ID")
    user_id: UserId = Field(description="用户ID")
    no_cache: bool = Field(description="是否不使用缓存")

    model_config = {
        "extra": "allow",
    }
# region req/


# region res
class GetGroupMemberInfoRes(Result):
    """获取群成员信息"""
    pass

# region res/

# region api
class GetGroupMemberInfoAPI(BaseModel):
    """get_group_member_info接口数据模型"""
    endpoint: str = Field(default="get_group_member_info")
    method: str = Field(default="POST")
    Req: type[BaseModel] = Field(default=GetGroupMemberInfoReq)
    Res: type[BaseModel] = Field(default=GetGroupMemberInfoRes)
    logger: logging.Logger = Field(default_factory=lambda: logging.getLogger(__name__))

    def __init__(self) -> None:
        super().__init__()
        self.logger.debug("初始化 GetGroupMemberInfoAPI")

    def __call__(self, req: GetGroupMemberInfoReq) -> GetGroupMemberInfoRes:
        """
        调用API的方法（仅作为接口定义，不包含实际请求逻辑）
        
        Args:
            req: 请求参数对象
            
        Returns:
            响应对象
        """
        # 调试日志
        self.logger.debug(f"调用 GetGroupMemberInfoAPI API")
        self.logger.debug(f"请求参数: {req.model_dump_json()}")
        
        # 注意：这里不应该包含实际的请求逻辑
        # 这个方法只是定义了接口，实际的请求应由适配器或客户端实现
        raise NotImplementedError("此方法需要由实际的API客户端实现")

# region api/
# region code/