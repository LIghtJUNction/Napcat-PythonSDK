# -*- coding: utf-8 -*- 
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/226659323e0
@llms.txt: https://napcat.apifox.cn/226659323e0.md
@last_update: 2025-04-25 23:00:50

@description: 获取群过滤系统消息

summary:获取群过滤系统消息

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "get_group_ignored_notifies"
__id__ = "226659323e0"
__method__ = "POST"

# region METADATA/


# region code
from pydantic import BaseModel, Field
import logging

logger = logging.getLogger(__name__)

# region component_models

# region component_models/

# region req
class GetGroupIgnoredNotifiesReq(BaseModel):
    """获取群过滤系统消息"""
    group_id: str | int = Field(description="标识ID")

    model_config = {
        "extra": "allow",
    }
# region req/


# region res
class GetGroupIgnoredNotifiesRes(BaseModel):
    """获取群过滤系统消息"""
    class JoinRequestsItem(BaseModel):
        """join_requests 元素"""
        request_id: str = Field(..., description="请求ID")
        requester_uin: str = Field(..., description="请求者UIN")
        requester_nick: str = Field(..., description="请求者昵称")
        group_id: str = Field(..., description="群ID")
        group_name: str = Field(..., description="群名称")
        checked: bool = Field(..., description="是否已检查")
        actor: str | int = Field(..., description="操作者")

        model_config = {
            "extra": "allow",
        }

    class ResponseData(BaseModel):
        """响应数据类型"""
        join_requests: list[JoinRequestsItem] = Field(default=[], description="join_requests字段")

        model_config = {
            "extra": "allow",
        }

    status: str = Field(default="ok", description="status字段")
    retcode: int = Field(default=0, description="retcode字段")
    data: ResponseData = Field(default_factory=lambda: ResponseData(), description="data字段")
    message: str = Field(default="", description="message字段")
    wording: str = Field(default="", description="wording字段")
    echo: str | None = Field(default=None, description="echo字段")

    model_config = {
        "extra": "allow",
    }
# region res/

# region api
class GetGroupIgnoredNotifiesAPI(BaseModel):
    """get_group_ignored_notifies接口数据模型"""
    endpoint: str = "get_group_ignored_notifies"
    method: str = "POST"
    Req: type[BaseModel] = GetGroupIgnoredNotifiesReq
    Res: type[BaseModel] = GetGroupIgnoredNotifiesRes
    logger = logging.getLogger(__name__)


    def __call__(self, req: GetGroupIgnoredNotifiesReq) -> GetGroupIgnoredNotifiesRes:
        """
        调用API的方法（仅作为接口定义，不包含实际请求逻辑）
        
        Args:
            req: 请求参数对象
            
        Returns:
            响应对象
        """
        # 调试日志
        self.logger.debug(f"调用 GetGroupIgnoredNotifiesAPI API")
        self.logger.debug(f"请求参数: {req.model_dump_json()}")
        
        # 注意：这里不应该包含实际的请求逻辑
        # 这个方法只是定义了接口，实际的请求应由适配器或客户端实现
        raise NotImplementedError("此方法需要由实际的API客户端实现")

# region api/
# region code/