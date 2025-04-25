# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/226656712e0
@llms.txt: https://napcat.apifox.cn/226656712e0.md
@last_update: 2025-04-25 23:00:48

@description: 

summary:获取合并转发消息

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "get_forward_msg"
__id__ = "226656712e0"
__method__ = "POST"

# region METADATA/


# region code
from pydantic import BaseModel, Field
import logging

logger = logging.getLogger(__name__)

# region req
class GetForwardMsgReq(BaseModel):
    """获取合并转发消息请求模型"""
    message_id: str = Field(..., description="消息ID")

    model_config = {
        "extra": "allow",
    }
# region req/


# region res
class GetForwardMsgRes(BaseModel):
    """获取合并转发消息响应模型"""
    status: str = Field(default="ok", description="状态")
    retcode: float = Field(default=0.0, description="返回码")
    data: dict = Field(default_factory=dict, description="数据")
    message: str = Field(default="", description="消息")
    wording: str = Field(default="", description="提示语")
    echo: str | None = Field(default=None, description="回显数据")

    model_config = {
        "extra": "allow",
    }
# region res/

# region api
class GetForwardMsgAPI(BaseModel):
    """get_forward_msg接口数据模型"""
    endpoint: str = Field(default="get_forward_msg", description="接口端点")
    method: str = Field(default="POST", description="请求方法")
    Req: type[BaseModel] = Field(default=GetForwardMsgReq, description="请求模型")
    Res: type[BaseModel] = Field(default=GetForwardMsgRes, description="响应模型")
    logger: logging.Logger = Field(default_factory=lambda: logging.getLogger(__name__), description="日志记录器")

    def __init__(self) -> None:
        super().__init__()
        self.logger.debug("初始化 GetForwardMsgAPI")

    def __call__(self, req: GetForwardMsgReq) -> GetForwardMsgRes:
        """
        调用API的方法（仅作为接口定义，不包含实际请求逻辑）
        
        Args:
            req: 请求参数对象
            
        Returns:
            响应对象
        """
        # 调试日志
        self.logger.debug(f"调用 GetForwardMsgAPI API")
        self.logger.debug(f"请求参数: {req.model_dump_json()}")
        
        # 注意：这里不应该包含实际的请求逻辑
        # 这个方法只是定义了接口，实际的请求应由适配器或客户端实现
        raise NotImplementedError("此方法需要由实际的API客户端实现")

# region api/
# region code/