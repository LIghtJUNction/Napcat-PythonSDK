# -*- coding: utf-8 -*- 
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/226656970e0
@llms.txt: https://napcat.apifox.cn/226656970e0.md
@last_update: 2025-04-25 23:00:49

@description: 

summary:获取账号信息

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "get_stranger_info"
__id__ = "226656970e0"
__method__ = "POST"

# region METADATA/


# region code
from pydantic import BaseModel, Field
from typing import Any
import logging

logger = logging.getLogger(__name__)

# region component_models
class UserId(BaseModel):
    id: str | float = Field(description="标识ID")
    name: str | None = Field(None, description="名称")

    model_config = {
        "extra": "allow",
    }

class Result(BaseModel):
    status: str = Field(default="ok", description="status字段")
    retcode: float = Field(default=0, description="retcode字段")
    data: dict[str, Any] = Field(description="data字段")
    message: str = Field(default="", description="message字段")
    wording: str = Field(default="", description="wording字段")
    echo: str | None = Field(default=None, description="echo字段")

    model_config = {
        "extra": "allow",
    }
# region component_models/

# region req
class GetStrangerInfoReq(BaseModel):
    """获取账号信息"""
    user_id: UserId = Field(description="用户ID")

    model_config = {
        "extra": "allow",
    }
# region req/


# region res
class GetStrangerInfoRes(BaseModel):
    """获取账号信息"""
    class ResponseData(BaseModel):
        """响应数据类型"""
        user_id: float = Field(description="user_id字段")
        uid: str = Field(description="uid字段")
        uin: str = Field(description="uin字段")
        nickname: str = Field(description="昵称")
        age: float = Field(description="年龄")
        qid: str = Field(description="qid字段")
        qqLevel: float = Field(description="账号等级")
        sex: str = Field(description="性别")
        long_nick: str = Field(description="个性签名")
        reg_time: float = Field(description="注册时间")
        is_vip: bool = Field(description="是否会员")
        is_years_vip: bool = Field(description="是否年费会员")
        vip_level: float = Field(description="会员等级")
        remark: str = Field(description="备注")
        status: float = Field(description="status字段")
        login_days: float = Field(description="连续登录天数")

        model_config = {
            "extra": "allow",
        }

    status: str = Field(default="ok", description="status字段")
    retcode: float = Field(default=0, description="retcode字段")
    data: ResponseData = Field(description="data字段")
    message: str = Field(default="", description="message字段")
    wording: str = Field(default="", description="wording字段")
    echo: str | None = Field(default=None, description="echo字段")

    model_config = {
        "extra": "allow",
    }
# region res/

# region api
class GetStrangerInfoAPI(BaseModel):
    """get_stranger_info接口数据模型"""
    endpoint: str = Field(default="get_stranger_info", description="Endpoint", const=True)
    method: str = Field(default="POST", description="HTTP Method", const=True)
    Req: type[BaseModel] = Field(default=GetStrangerInfoReq, description="Request Model", const=True)
    Res: type[BaseModel] = Field(default=GetStrangerInfoRes, description="Response Model", const=True)
    logger: logging.Logger = Field(default_factory=lambda: logging.getLogger(__name__), description="Logger", const=True)

    def __init__(self) -> None:
        super().__init__()
        self.logger.debug("初始化 GetStrangerInfoAPI")

    def __call__(self, req: GetStrangerInfoReq) -> GetStrangerInfoRes:
        """
        调用API的方法（仅作为接口定义，不包含实际请求逻辑）
        
        Args:
            req: 请求参数对象
            
        Returns:
            响应对象
        """
        # 调试日志
        self.logger.debug(f"调用 GetStrangerInfoAPI API")
        self.logger.debug(f"请求参数: {req.model_dump_json()}")
        
        # 注意：这里不应该包含实际的请求逻辑
        # 这个方法只是定义了接口，实际的请求应由适配器或客户端实现
        raise NotImplementedError("此方法需要由实际的API客户端实现")

# region api/
# region code/