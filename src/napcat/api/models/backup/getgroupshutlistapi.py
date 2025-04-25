# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: ['群聊相关']
@homepage: https://napcat.apifox.cn/226659300e0
@llms.txt: https://napcat.apifox.cn/226659300e0.md
@last_update: 2025-04-26 01:17:45

@description: 

summary:获取群禁言列表

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "get_group_shut_list"
__id__ = "226659300e0"
__method__ = "POST"

# endregion METADATA


# region code
import logging
from pydantic import BaseModel, Field

logger = logging.getLogger(__name__)

# region req
class GetGroupShutListReq(BaseModel):
    """
    获取群禁言列表请求模型
    """
    group_id: int | str = Field(..., description="群号")
# endregion req



# region res
class GroupHonor(BaseModel):
    """
    群荣誉信息
    """
    honor_0: int = Field(..., alias='0')
    honor_1: int = Field(..., alias='1')
    honor_2: int = Field(..., alias='2')
    honor_3: int = Field(..., alias='3')

class BannedMember(BaseModel):
    """
    群禁言成员信息
    """
    uid: str = Field(..., description="用户UID")
    qid: str = Field(..., description="用户QID")
    uin: str = Field(..., description="用户UIN")
    nick: str = Field(..., description="用户昵称")
    remark: str = Field(..., description="备注")
    cardType: int = Field(..., description="名片类型")
    cardName: str = Field(..., description="名片名称")
    role: int = Field(..., description="群成员角色 (0: 普通成员, 1: 管理员, 2: 群主)")
    avatarPath: str = Field(..., description="头像路径")
    shutUpTime: int = Field(..., description="解禁时间 (Unix时间戳)")
    isDelete: bool = Field(..., description="是否已删除")
    isSpecialConcerned: bool = Field(..., description="是否特别关注")
    isSpecialShield: bool = Field(..., description="是否特别屏蔽")
    isRobot: bool = Field(..., description="是否是机器人")
    groupHonor: GroupHonor = Field(..., description="群荣誉")
    memberRealLevel: int = Field(..., description="群聊等级")
    memberLevel: int = Field(..., description="成员等级")
    globalGroupLevel: int = Field(..., description="全局群等级")
    globalGroupPoint: int = Field(..., description="全局群积分")
    memberTitleId: int = Field(..., description="成员头衔ID")
    memberSpecialTitle: str = Field(..., description="成员特殊头衔")
    specialTitleExpireTime: str = Field(..., description="特殊头衔过期时间")
    userShowFlag: int = Field(..., description="用户显示标志")
    userShowFlagNew: int = Field(..., description="新用户显示标志")
    richFlag: int = Field(..., description="富文本标志")
    mssVipType: int = Field(..., description="MSS VIP类型")
    bigClubLevel: int = Field(..., description="大乐部等级")
    bigClubFlag: int = Field(..., description="大乐部标志")
    autoRemark: str = Field(..., description="自动备注")
    creditLevel: int = Field(..., description="信用等级")
    joinTime: int = Field(..., description="入群时间 (Unix时间戳)")
    lastSpeakTime: int = Field(..., description="最后发言时间 (Unix时间戳)")
    memberFlag: int = Field(..., description="成员标志")
    memberFlagExt: int = Field(..., description="成员标志扩展")
    memberMobileFlag: int = Field(..., description="成员手机标志")
    memberFlagExt2: int = Field(..., description="成员标志扩展2")
    isSpecialShielded: bool = Field(..., description="是否被特别屏蔽")
    cardNameId: int = Field(..., description="名片ID")
    # Placeholder fields from OpenAPI spec - mapping them with aliases
    field_01JBHA466QHTSVPFFF54F8P2YT: str = Field(..., alias='01JBHA466QHTSVPFFF54F8P2YT')
    field_01JBHA46D3X7742C9TX0VM8SNR: str = Field(..., alias='01JBHA46D3X7742C9TX0VM8SNR')
    field_01JBHA5T79E4HEQ1DFJ0SY2YHV: str = Field(..., alias='01JBHA5T79E4HEQ1DFJ0SY2YHV')
    field_01JBHA5TECQZX10200ADAGYDD2: str = Field(..., alias='01JBHA5TECQZX10200ADAGYDD2')
    field_01JBHA5VJS1NBN084ZBA24DK1C: str = Field(..., alias='01JBHA5VJS1NBN084ZBA24DK1C')
    field_01JBHA5X1H6N1W1ZMZ5C54NA9X: str = Field(..., alias='01JBHA5X1H6N1W1ZMZ5C54NA9X')

class GetGroupShutListRes(BaseModel):
    """
    获取群禁言列表响应模型
    """
    status: str = Field(..., description="响应状态, 'ok' 表示成功")
    retcode: int = Field(..., description="响应码")
    data: list[BannedMember] = Field(..., description="禁言成员列表") # Assuming 'data' should be a list based on endpoint name
    message: str = Field(..., description="响应消息")
    wording: str = Field(..., description="响应提示")
    echo: str | None = Field(None, description="Echo回显")
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
