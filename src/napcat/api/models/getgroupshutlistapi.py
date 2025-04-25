# -*- coding: utf-8 -*- 

# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/226659300e0
@llms.txt: https://napcat.apifox.cn/226659300e0.md
@last_update: 2025-04-25 23:00:50

@description: 

summary:获取群禁言列表

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "get_group_shut_list"
__id__ = "226659300e0"
__method__ = "POST"

# region METADATA/


# region code
from pydantic import BaseModel, Field
from typing import Any
import logging

logger = logging.getLogger(__name__)

# region component_models
class GroupId(BaseModel):
    id: str | int = Field(description="标识ID")
    name: str | None = Field(None, description="名称")

    model_config = {
        "extra": "allow",
    }

class Result(BaseModel):
    status: str = Field(description="status字段")
    retcode: float = Field(description="retcode字段")
    data: dict[str, Any] = Field(description="data字段")
    message: str = Field(description="message字段")
    wording: str = Field(description="wording字段")
    echo: str | None = Field(default=None, description="echo字段")

    model_config = {
        "extra": "allow",
    }
# region component_models/

# region req
class GetGroupShutListReq(BaseModel):
    """获取群禁言列表"""
    groupId: GroupId = Field(description="群组ID")

    model_config = {
        "extra": "allow",
    }
# region req/


# region res
class GetGroupShutListRes(BaseModel):
    """获取群禁言列表"""

    class ResponseData(BaseModel):
        """响应数据类型"""
        uid: str | None = Field(default=None, description="uid字段")
        qid: str | None = Field(default=None, description="qid字段")
        uin: str | None = Field(default=None, description="uin字段")
        nick: str | None = Field(default=None, description="nick字段")
        remark: str | None = Field(default=None, description="remark字段")
        cardType: float | None = Field(default=None, description="cardType字段")
        cardName: str | None = Field(default=None, description="cardName字段")
        role: float | None = Field(default=None, description="role字段")
        avatarPath: str | None = Field(default=None, description="avatarPath字段")
        shutUpTime: float | None = Field(default=None, description="解禁时间")
        isDelete: bool | None = Field(default=None, description="isDelete字段")
        isSpecialConcerned: bool | None = Field(default=None, description="isSpecialConcerned字段")
        isSpecialShield: bool | None = Field(default=None, description="isSpecialShield字段")
        isRobot: bool | None = Field(default=None, description="isRobot字段")
        class GroupHonor(BaseModel):
            field_0: float = Field(description="groupHonor 0")
            field_1: float = Field(description="groupHonor 1")
            field_2: float = Field(description="groupHonor 2")
            field_3: float = Field(description="groupHonor 3")

            model_config = {
                "extra": "allow",
            }

        groupHonor: GroupHonor | None = Field(default=None, description="groupHonor字段")
        memberRealLevel: float | None = Field(default=None, description="群聊等级")
        memberLevel: float | None = Field(default=None, description="memberLevel字段")
        globalGroupLevel: float | None = Field(default=None, description="globalGroupLevel字段")
        globalGroupPoint: float | None = Field(default=None, description="globalGroupPoint字段")
        memberTitleId: float | None = Field(default=None, description="memberTitleId字段")
        memberSpecialTitle: str | None = Field(default=None, description="memberSpecialTitle字段")
        specialTitleExpireTime: str | None = Field(default=None, description="specialTitleExpireTime字段")
        userShowFlag: float | None = Field(default=None, description="userShowFlag字段")
        userShowFlagNew: float | None = Field(default=None, description="userShowFlagNew字段")
        richFlag: float | None = Field(default=None, description="richFlag字段")
        mssVipType: float | None = Field(default=None, description="mssVipType字段")
        bigClubLevel: float | None = Field(default=None, description="bigClubLevel字段")
        bigClubFlag: float | None = Field(default=None, description="bigClubFlag字段")
        autoRemark: str | None = Field(default=None, description="autoRemark字段")
        creditLevel: float | None = Field(default=None, description="creditLevel字段")
        joinTime: float | None = Field(default=None, description="入群时间")
        lastSpeakTime: float | None = Field(default=None, description="最后发言时间")
        memberFlag: float | None = Field(default=None, description="memberFlag字段")
        memberFlagExt: float | None = Field(default=None, description="memberFlagExt字段")
        memberMobileFlag: float | None = Field(default=None, description="memberMobileFlag字段")
        memberFlagExt2: float | None = Field(default=None, description="memberFlagExt2字段")
        isSpecialShielded: bool | None = Field(default=None, description="isSpecialShielded字段")
        cardNameId: float | None = Field(default=None, description="cardNameId字段")

        model_config = {
            "extra": "allow",
        }

    status: str = Field(default="ok", description="status字段")
    retcode: float = Field(default=0, description="retcode字段")
    data: ResponseData = Field(default_factory=ResponseData, description="data字段")
    message: str = Field(default="", description="message字段")
    wording: str = Field(default="", description="wording字段")
    echo: str | None = Field(default=None, description="echo字段")

    model_config = {
        "extra": "allow",
    }
# region res/

# region api
class GetGroupShutListAPI(BaseModel):
    """get_group_shut_list接口数据模型"""
    endpoint: str = Field(default="get_group_shut_list", description="Endpoint", const=True)
    method: str = Field(default="POST", description="HTTP Method", const=True)
    Req: type[BaseModel] = Field(default=GetGroupShutListReq, description="Request Model", const=True)
    Res: type[BaseModel] = Field(default=GetGroupShutListRes, description="Response Model", const=True)

    model_config = {
        "arbitrary_types_allowed": True
    }

    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        logger.debug("初始化 GetGroupShutListAPI")

    def __call__(self, req: GetGroupShutListReq) -> GetGroupShutListRes:
        """
        调用API的方法（仅作为接口定义，不包含实际请求逻辑）
        
        Args:
            req: 请求参数对象
            
        Returns:
            响应对象
        """
        # 调试日志
        logger.debug(f"调用 GetGroupShutListAPI API")
        logger.debug(f"请求参数: {req.model_dump_json()}")
        
        # 注意：这里不应该包含实际的请求逻辑
        # 这个方法只是定义了接口，实际的请求应由适配器或客户端实现
        raise NotImplementedError("此方法需要由实际的API客户端实现")

# region api/
# region code/