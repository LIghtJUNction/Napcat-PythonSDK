# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: 账号相关
@homepage: https://napcat.apifox.cn/226658978e0
@llms.txt: https://napcat.apifox.cn/226658978e0.md
@last_update: 2025-04-25 23:00:49

@description: 

summary:获取好友分组列表

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "get_friends_with_category"
__id__ = "226658978e0"
__method__ = "POST"

# region METADATA/


# region code
from pydantic import BaseModel, Field
from typing import Any
import logging

logger = logging.getLogger(__name__)

# region component_models
class 好友信息(BaseModel):
    """好友信息"""
    qid: str = Field(..., description="QQID")
    longNick: str = Field(..., description="个性签名")
    birthday_year: float = Field(..., description="生日_年")
    birthday_month: float = Field(..., description="生日_月")
    birthday_day: float = Field(..., description="生日_日")
    age: float = Field(..., description="年龄")
    sex: str = Field(..., description="性别")
    eMail: str = Field(..., description="邮箱")
    phoneNum: str = Field(..., description="手机号")
    categoryId: float = Field(..., description="分类")
    richTime: float = Field(..., description="注册时间")
    richBuffer: dict[str, Any] = Field(..., description="richBuffer字段")
    uid: str = Field(..., description="uid字段")
    uin: str = Field(..., description="uin字段")
    nick: str = Field(..., description="nick字段")
    remark: str = Field(..., description="备注")
    user_id: float = Field(..., description="user_id字段")
    nickname: str = Field(..., description="nickname字段")
    level: float = Field(..., description="等级")

    model_config = {
        "extra": "allow",
    }

class CategoryData(BaseModel):
    """分组数据"""
    categoryId: float = Field(..., description="分组ID")
    categorySortId: float = Field(..., description="分组排序ID")
    categoryName: str = Field(..., description="分组名")
    categoryMbCount: float = Field(..., description="好友数量")
    onlineCount: float = Field(..., description="在线好友数量")
    buddyList: list[好友信息] = Field(..., description="好友列表")

    model_config = {
        "extra": "allow",
    }

# region component_models/

# region req
class GetFriendsWithCategoryReq(BaseModel):
    """获取好友分组列表请求参数"""
    model_config = {
        "extra": "allow",
    }
# region req/


# region res
class GetFriendsWithCategoryRes(BaseModel):
    """获取好友分组列表响应"""
    status: str = Field("ok", description="status字段")
    retcode: float = Field(0, description="retcode字段")
    data: list[CategoryData] = Field(..., description="data字段")
    message: str = Field("", description="message字段")
    wording: str = Field("", description="wording字段")
    echo: str | None = Field(None, description="echo字段")

    model_config = {
        "extra": "allow",
    }
# region res/

# region api
class GetFriendsWithCategoryAPI(BaseModel):
    """get_friends_with_category接口数据模型"""
    endpoint: str = "get_friends_with_category"
    method: str = "POST"
    Req: type[BaseModel] = GetFriendsWithCategoryReq
    Res: type[BaseModel] = GetFriendsWithCategoryRes
    logger = logging.getLogger(__name__)

    def __init__(self) -> None:
        super().__init__()
        self.logger.debug("初始化 GetFriendsWithCategoryAPI")

    def __call__(self, req: GetFriendsWithCategoryReq) -> GetFriendsWithCategoryRes:
        """
        调用API的方法（仅作为接口定义，不包含实际请求逻辑）
        
        Args:
            req: 请求参数对象
            
        Returns:
            响应对象
        """
        # 调试日志
        self.logger.debug(f"调用 GetFriendsWithCategoryAPI API")
        self.logger.debug(f"请求参数: {req.model_dump_json()}")
        
        # 注意：这里不应该包含实际的请求逻辑
        # 这个方法只是定义了接口，实际的请求应由适配器或客户端实现
        raise NotImplementedError("此方法需要由实际的API客户端实现")

# region api/
# region code/