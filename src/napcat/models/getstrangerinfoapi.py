# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/226656970e0
@llms.txt: https://napcat.apifox.cn/226656970e0.md
@last_update: 2025-04-25 22:54:08

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
class user_id(BaseModel):
    id: str = Field(description="标识ID")
    name: str | None = Field(None, description="名称")

    model_config = {
        "extra": "allow",
    }

class result(BaseModel):
    status: str = Field(description="status字段")
    retcode: float = Field(description="retcode字段")
    data: dict[str, Any] = Field(description="data字段")
    message: str = Field(description="message字段")
    wording: str = Field(description="wording字段")
    echo: str | None = Field(description="echo字段")

    model_config = {
        "extra": "allow",
    }
# region component_models/

# region req
class GetStrangerInfoReq(BaseModel):
    """获取账号信息"""
    user_id: user_id

    model_config = {
        "extra": "allow",
    }
# region req/


# region res
class GetStrangerInfoRes(BaseModel):
    """获取账号信息"""
    class ResponseData(BaseModel):
        """响应数据类型"""
        user_id: float = Field(default=None, description="user_id字段")
        uid: str = Field(default=None, description="uid字段")
        uin: str = Field(default=None, description="uin字段")
        nickname: str = Field(default=None, description="昵称")
        age: float = Field(default=None, description="年龄")
        qid: str = Field(default=None, description="qid字段")
        qqLevel: float = Field(default=None, description="账号等级")
        sex: str = Field(default=None, description="性别")
        long_nick: str = Field(default=None, description="个性签名")
        reg_time: float = Field(default=None, description="注册时间")
        is_vip: bool = Field(default=None, description="是否会员")
        is_years_vip: bool = Field(default=None, description="是否年费会员")
        vip_level: float = Field(default=None, description="会员等级")
        remark: str = Field(default=None, description="备注")
        status: float = Field(default=None, description="status字段")
        login_days: float = Field(default=None, description="连续登录天数")

        model_config = {
            "extra": "allow",
        }

    status: str = Field(default="ok", description="status字段")
    retcode: float = Field(default=0, description="retcode字段")
    data: ResponseData = Field(default_factory=lambda: ResponseData(), description="data字段")
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
    endpoint: str = "get_stranger_info"
    method: str = "POST"
    Req: type[BaseModel] = GetStrangerInfoReq
    Res: type[BaseModel] = GetStrangerInfoRes
    logger = logging.getLogger(__name__)

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

