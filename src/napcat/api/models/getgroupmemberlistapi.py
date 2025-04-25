# -*- coding: utf-8 -*- 
# region METADATA
"""
@tags: 群聊相关
@homepage: https://napcat.apifox.cn/226657034e0
@llms.txt: https://napcat.apifox.cn/226657034e0.md
@last_update: 2025-04-25 23:00:49

@description: 获取群成员列表

summary:获取群成员列表

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "get_group_member_list"
__id__ = "226657034e0"
__method__ = "POST"

# region METADATA/


# region code
from pydantic import BaseModel, Field
import logging

logger = logging.getLogger(__name__)

# region component_models
class result(BaseModel):
    """通用结果模型"""
    status: str = Field(default="ok", description="状态")
    retcode: float = Field(default=0.0, description="返回码")
    data: list[dict[str, any]] = Field(default_factory=list, description="数据")
    message: str = Field(default="", description="消息")
    wording: str = Field(default="", description="说明")
    echo: str | None = Field(default=None, description="回显")

    model_config = {
        "extra": "allow",
    }

# region component_models/

# region req
class GetGroupMemberListReq(BaseModel):
    """获取群成员列表请求参数"""
    group_id: str | int = Field(description="群组ID (可以是字符串或数字)")
    no_cache: bool = Field(default=False, description="是否不使用缓存")

    model_config = {
        "extra": "allow",
    }
# region req/


# region res
class GetGroupMemberListRes(BaseModel):
    """获取群成员列表响应"""
    root: result
# region res/

# region api
class GetGroupMemberListAPI:
    """get_group_member_list接口数据模型"""
    endpoint: str = "get_group_member_list"
    method: str = "POST"
    logger = logging.getLogger(__name__)

    def __call__(self, req: GetGroupMemberListReq) -> result:
        """
        调用API的方法（仅作为接口定义，不包含实际请求逻辑）
        
        Args:
            req: 请求参数对象
            
        Returns:
            响应对象
        """
        # 调试日志
        self.logger.debug(f"调用 GetGroupMemberListAPI API")
        self.logger.debug(f"请求参数: {req.model_dump_json()}")
        
        # 注意：这里不应该包含实际的请求逻辑
        # 这个方法只是定义了接口，实际的请求应由适配器或客户端实现
        raise NotImplementedError("此方法需要由实际的API客户端实现")

# region api/
# region code/