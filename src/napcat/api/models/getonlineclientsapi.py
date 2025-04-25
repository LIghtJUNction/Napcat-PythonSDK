# -*- coding: utf-8 -*- 
# region METADATA
"""
@tags: 账号相关
@homepage: https://napcat.apifox.cn/226657379e0
@llms.txt: https://napcat.apifox.cn/226657379e0.md
@last_update: 2025-04-25 23:00:49

@description: 获取当前账号在线客户端列表

summary: 获取当前账号在线客户端列表

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "get_online_clients"
__id__ = "226657379e0"
__method__ = "POST"

# region METADATA/


# region code
from pydantic import BaseModel, Field
import logging

logger = logging.getLogger(__name__)

# region req
class GetOnlineClientsReq(BaseModel):
    """获取当前账号在线客户端列表的请求参数"""
    no_cache: bool = Field(default=False, description="是否禁用缓存")

    model_config = {
        "extra": "allow",
    }
# region req/


# region res
class GetOnlineClientsRes(BaseModel):
    """获取当前账号在线客户端列表的响应"""

    class ResponseData(BaseModel):
        """响应数据类型"""
        clients: dict[str, any] = Field(default_factory=dict, description="客户端信息")

        model_config = {
            "extra": "allow",
        }

    status: str = Field(default="ok", description="状态")
    retcode: float = Field(default=0, description="返回码")
    data: ResponseData = Field(default_factory=ResponseData, description="数据")
    message: str = Field(default="", description="消息")
wording: str = Field(default="", description="提示语")
    echo: str | None = Field(default=None, description="回显信息")

    model_config = {
        "extra": "allow",
    }
# region res/

# region component_models
class Result(BaseModel):
    status: str = Field(default="ok", description="status字段")
    retcode: float = Field(description="retcode字段")
    data: dict[str, any] = Field(description="data字段")
    message: str = Field(description="message字段")
    wording: str = Field(description="wording字段")
    echo: str | None = Field(description="echo字段")

    model_config = {
        "extra": "allow",
    }
# region component_models/



# region api
class GetOnlineClientsAPI:
    """get_online_clients接口数据模型"""
    endpoint: str = "get_online_clients"
    method: str = "POST"
    Req = GetOnlineClientsReq
    Res = GetOnlineClientsRes
    logger = logging.getLogger(__name__)

    def __init__(self) -> None:
        self.logger.debug("初始化 GetOnlineClientsAPI")

    def __call__(self, req: GetOnlineClientsReq) -> GetOnlineClientsRes:
        """
        调用API的方法（仅作为接口定义，不包含实际请求逻辑）
        
        Args:
            req: 请求参数对象
            
        Returns:
            响应对象
        """
        # 调试日志
        self.logger.debug(f"调用 GetOnlineClientsAPI API")
        self.logger.debug(f"请求参数: {req.model_dump_json()}")
        
        # 注意：这里不应该包含实际的请求逻辑
        # 这个方法只是定义了接口，实际的请求应由适配器或客户端实现
        raise NotImplementedError("此方法需要由实际的API客户端实现")

# region api/
# region code/