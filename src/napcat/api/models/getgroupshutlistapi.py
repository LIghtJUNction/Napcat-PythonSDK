# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: ['群聊相关']
@homepage: https://napcat.apifox.cn/226659300e0
@llms.txt: https://napcat.apifox.cn/226659300e0.md
@last_update: 2025-04-27 00:53:40

@description: 获取群禁言列表

summary:获取群禁言列表

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.43"
__endpoint__ = "get_group_shut_list"
__id__ = "226659300e0"
__method__ = "POST"

# endregion METADATA


# region code
import logging
from typing import Any, Literal
from pydantic import BaseModel, Field

logger = logging.getLogger(__name__)

# region req
class GetGroupShutListReq(BaseModel):
    """
    获取群禁言列表接口请求参数
    """

    group_id: int | str = Field(..., description="群号")

# endregion req


# region res



class GetGroupShutListRes(BaseModel):
    """
    获取群禁言列表接口响应参数
    """
    class GroupShutMember(BaseModel):
        """
        群禁言成员信息
        """
        uid: str = Field(..., description="用户ID")
        qid: str = Field(..., description="QID")
        uin: str = Field(..., description="UIN")
        nick: str = Field(..., description="昵称")
        remark: str = Field(..., description="备注")
        cardType: int = Field(..., description="群名片类型")
        cardName: str = Field(..., description="群名片")
        role: int = Field(..., description="群角色")
        avatarPath: str = Field(..., description="头像路径")
        shutUpTime: int = Field(..., description="解禁时间")
        isDelete: bool = Field(..., description="是否已删除")
        isSpecialConcerned: bool = Field(..., description="是否特别关注")
        isSpecialShield: bool = Field(..., description="是否被屏蔽")
        isRobot: bool = Field(..., description="是否机器人")
        groupHonor: dict[Any, Any] = Field(..., description="群荣誉信息")
        memberRealLevel: int = Field(..., description="群聊等级")
        memberLevel: int = Field(..., description="成员等级")
        globalGroupLevel: int = Field(..., description="全局群等级")
        globalGroupPoint: int = Field(..., description="全局群积分")
        memberTitleId: int = Field(..., description="成员头衔ID")
        memberSpecialTitle: str = Field(..., description="成员特殊头衔")
        lastSpeakTime: int = Field(..., description="最后发言时间")
        joinTime: int = Field(..., description="入群时间")
        specialTitleExpireTime: str = Field(..., description="特殊头衔过期时间")
        userShowFlag: int = Field(..., description="用户展示Flag")
        userShowFlagNew: int = Field(..., description="新的用户展示Flag")
        richFlag: int = Field(..., description="富豪Flag")
        mssVipType: int = Field(..., description="MSS VIP类型")
        bigClubLevel: int = Field(..., description="大会员等级")
        bigClubFlag: int = Field(..., description="大会员Flag")
        autoRemark: str = Field(..., description="自动备注")
        creditLevel: int = Field(..., description="信用等级")
        memberFlag: int = Field(..., description="成员Flag")
        memberFlagExt: int = Field(..., description="成员扩展Flag")
        memberMobileFlag: int = Field(..., description="成员手机Flag")
        memberFlagExt2: int = Field(..., description="成员扩展Flag 2")
        isSpecialShielded: bool = Field(..., description="是否被特别屏蔽")
        cardNameId: int = Field(..., description="群名片ID")


    status: Literal["ok"] = Field("ok", description="状态码，固定为 'ok'")
    retcode: int = Field(..., description="返回码")
    data: list[GroupShutMember] = Field(..., description="禁言成员列表")
    message: str = Field(..., description="消息")
    wording: str = Field(..., description="提示词")
    echo: str | None = Field(default=None, description="Echo")

# endregion res

# region api
class GetGroupShutListAPI(BaseModel):
    """get_group_shut_list接口数据模型"""
    endpoint: str = "get_group_shut_list"
    method: str = "POST"
    Req: type[BaseModel] = GetGroupShutListReq
    Res: type[BaseModel] = GetGroupShutListRes
# endregion api


# endregion code