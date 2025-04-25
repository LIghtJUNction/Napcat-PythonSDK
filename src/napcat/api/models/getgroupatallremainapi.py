# -*- coding: utf-8 -*- 
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/227245941e0
@llms.txt: https://napcat.apifox.cn/227245941e0.md
@last_update: 2025-04-25 23:00:50

@description: 

summary:获取群 @全体成员 剩余次数

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "get_group_at_all_remain"
__id__ = "227245941e0"
__method__ = "POST"

# region METADATA/


# region code
from pydantic import BaseModel, Field
from typing import Any
import logging

logger = logging.getLogger(__name__)

# region component_models
class GroupId(BaseModel):
    """群ID类型"""
    id: str | int = Field(description="标识ID")
    name: str | None = Field(default=None, description="名称")

    model_config = {
        "extra": "allow",
    }


# region component_models/

# region req
class GetGroupAtAllRemainReq(BaseModel):
    """获取群 @全体成员 剩余次数 请求参数"""
    group_id: GroupId = Field(description="群ID")

    model_config = {
        "extra": "allow",
    }


# region req/


# region res
class GetGroupAtAllRemainRes(BaseModel):
    """获取群 @全体成员 剩余次数 响应结果"""

    class ResponseData(BaseModel):
        """响应数据类型"""
        can_at_all: bool = Field(default=False, description="是否可以@全体成员")
        remain_at_all_count_for_group: float = Field(default=0.0, description="群剩余@全体成员次数")
        remain_at_all_count_for_uin: float = Field(default=0.0, description="用户剩余@全体成员次数")

        model_config = {
            "extra": "allow",
        }

    status: str = Field(default="ok", description="状态")
    retcode: float = Field(default=0.0, description="返回码")
    data: ResponseData = Field(default_factory=ResponseData, description="数据")
    message: str = Field(default="", description="消息")
    wording: str = Field(default="", description="提示语")
    echo: str | None = Field(default=None, description="回显数据")

    model_config = {
        "extra": "allow",
    }


# region res/

# region api
class GetGroupAtAllRemainAPI(BaseModel):
    """get_group_at_all_remain接口数据模型"""
    endpoint: str = "get_group_at_all_remain"
    method: str = "POST"
    Req: type[BaseModel] = GetGroupAtAllRemainReq
    Res: type[BaseModel] = GetGroupAtAllRemainRes
    logger = logging.getLogger(__name__)

    def __init__(self) -> None:
        super().__init__()
        self.logger.debug("初始化 GetGroupAtAllRemainAPI")

    def __call__(self, req: GetGroupAtAllRemainReq) -> GetGroupAtAllRemainRes:
        """
        调用API的方法（仅作为接口定义，不包含实际请求逻辑）
        
        Args:
            req: 请求参数对象
            
        Returns:
            响应对象
        """
        # 调试日志
        self.logger.debug(f"调用 GetGroupAtAllRemainAPI API")
        self.logger.debug(f"请求参数: {req.model_dump_json()}")

        # 注意：这里不应该包含实际的请求逻辑
        # 这个方法只是定义了接口，实际的请求应由适配器或客户端实现
        raise NotImplementedError("此方法需要由实际的API客户端实现")


# region api/
# region code/