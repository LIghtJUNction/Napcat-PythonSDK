# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/226656976e0
@llms.txt: https://napcat.apifox.cn/226656976e0.md
@last_update: 2025-04-25 23:00:49

@description: 

summary:获取好友列表

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "get_friend_list"
__id__ = "226656976e0"
__method__ = "POST"

# region METADATA/


# region code
from pydantic import BaseModel, Field
from typing import Any
import logging

logger = logging.getLogger(__name__)

# region component_models
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

class 好友信息(BaseModel):
    qid: str = Field(description="QQID")
    longNick: str = Field(description="个性签名")
    birthday_year: float = Field(description="生日_年")
    birthday_month: float = Field(description="生日_月")
    birthday_day: float = Field(description="生日_日")
    age: float = Field(description="年龄")
    sex: str = Field(description="性别")
    eMail: str = Field(description="邮箱")
    phoneNum: str = Field(description="手机号")
    categoryId: float = Field(description="分类")
    richTime: float = Field(description="注册时间")
    richBuffer: dict[str, Any] = Field(description="richBuffer字段")
    uid: str = Field(description="uid字段")
    uin: str = Field(description="uin字段")
    nick: str = Field(description="nick字段")
    remark: str = Field(description="备注")
    user_id: float = Field(description="user_id字段")
    nickname: str = Field(description="nickname字段")
    level: float = Field(description="等级")

    model_config = {
        "extra": "allow",
    }
# region component_models/

# region req
class GetFriendListReq(BaseModel):
    """获取好友列表"""
    no_cache: bool = Field(description="不缓存")

    model_config = {
        "extra": "allow",
    }
# region req/


# region res
class GetFriendListRes(BaseModel):
    """获取好友列表"""
    class ResponseData(BaseModel):
        """响应数据类型"""
        yes: bool = Field(default=True, description="是否可用")
        reason: str | None = Field(default=None, description="原因")

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
class GetFriendListAPI(BaseModel):
    """get_friend_list接口数据模型"""
    endpoint: str = "get_friend_list"
    method: str = "POST"
    Req: type[BaseModel] = GetFriendListReq
    Res: type[BaseModel] = GetFriendListRes
    logger = logging.getLogger(__name__)

    def __init__(self) -> None:
        super().__init__()
        self.logger.debug("初始化 GetFriendListAPI")

    def __call__(self, req: GetFriendListReq) -> GetFriendListRes:
        """
        调用API的方法（仅作为接口定义，不包含实际请求逻辑）
        
        Args:
            req: 请求参数对象
            
        Returns:
            响应对象
        """
        # 调试日志
        self.logger.debug(f"调用 GetFriendListAPI API")
        self.logger.debug(f"请求参数: {req.model_dump_json()}")
        
        # 注意：这里不应该包含实际的请求逻辑
        # 这个方法只是定义了接口，实际的请求应由适配器或客户端实现
        raise NotImplementedError("此方法需要由实际的API客户端实现")

# region api/
# region code/

