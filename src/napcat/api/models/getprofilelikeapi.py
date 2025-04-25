# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/226659197e0
@llms.txt: https://napcat.apifox.cn/226659197e0.md
@last_update: 2025-04-25 23:00:49

@description: 

summary:获取点赞列表

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "get_profile_like"
__id__ = "226659197e0"
__method__ = "POST"

# region METADATA/


# region code
from pydantic import BaseModel, Field
import logging

logger = logging.getLogger(__name__)

# region component_models
class Result(BaseModel):
    """通用返回结果"""
    status: str = Field(default="ok", description="status字段")
    retcode: float = Field(default=0.0, description="retcode字段")
    data: dict[str, any] = Field(default_factory=dict, description="data字段")
    message: str = Field(default="", description="message字段")
    wording: str = Field(default="", description="wording字段")
    echo: str | None = Field(default=None, description="echo字段")

    model_config = {
        "extra": "allow",
    }
# region component_models/

# region req
class GetProfileLikeReq(BaseModel):
    """获取点赞列表请求参数"""
    model_config = {
        "extra": "allow",
    }
# region req/


# region res
class UserInfosItem(BaseModel):
    """用户信息条目"""
    uid: str = Field(..., description="用户ID")
    src: float = Field(..., description="来源")
    latest_time: float = Field(..., description="最近时间")
    count: float = Field(..., description="计数")
    gift_count: float = Field(..., description="礼物计数")
    custom_id: float = Field(..., description="自定义ID")
    last_charged: float = Field(..., description="上次充值")
    b_available_cnt: float = Field(..., description="可用数量")
    b_today_voted_cnt: float = Field(..., description="今日投票数量")
    nick: str = Field(..., description="昵称")
    gender: float = Field(..., description="性别")
    age: float = Field(..., description="年龄")
    is_friend: bool = Field(..., description="是否好友")
    isvip: bool = Field(..., description="是否VIP")
    is_svip: bool = Field(..., description="是否SVIP")
    uin: float = Field(..., description="用户UIN")

    model_config = {
        "extra": "allow",
    }


class GetProfileLikeRes(BaseModel):
    """获取点赞列表响应"""

    class ResponseData(BaseModel):
        """响应数据类型"""
        total_count: float = Field(..., description="总点赞数")
        new_count: float = Field(..., description="新点赞数")
        new_nearby_count: float = Field(..., description="附近新增点赞数")
        last_visit_time: float = Field(..., description="上次访问时间")
        user_infos: list[UserInfosItem] = Field(..., description="用户信息列表")

        model_config = {
            "extra": "allow",
        }

    status: str = Field(default="ok", description="status字段")
    retcode: float = Field(default=0.0, description="retcode字段")
    data: ResponseData = Field(..., description="data字段")
    message: str = Field(default="", description="message字段")
    wording: str = Field(default="", description="wording字段")
    echo: str | None = Field(default=None, description="echo字段")

    model_config = {
        "extra": "allow",
    }
# region res/

# region api
class GetProfileLikeAPI(BaseModel):
    """get_profile_like接口数据模型"""
    endpoint: str = "get_profile_like"
    method: str = "POST"
    Req: type[BaseModel] = GetProfileLikeReq
    Res: type[BaseModel] = GetProfileLikeRes
    logger = logging.getLogger(__name__)

    def __init__(self) -> None:
        super().__init__()
        self.logger.debug("初始化 GetProfileLikeAPI")

    def __call__(self, req: GetProfileLikeReq) -> GetProfileLikeRes:
        """
        调用API的方法（仅作为接口定义，不包含实际请求逻辑）
        
        Args:
            req: 请求参数对象
            
        Returns:
            响应对象
        """
        # 调试日志
        self.logger.debug(f"调用 GetProfileLikeAPI API")
        self.logger.debug(f"请求参数: {req.model_dump_json()}")
        
        # 注意：这里不应该包含实际的请求逻辑
        # 这个方法只是定义了接口，实际的请求应由适配器或客户端实现
        raise NotImplementedError("此方法需要由实际的API客户端实现")

# region api/
# region code/