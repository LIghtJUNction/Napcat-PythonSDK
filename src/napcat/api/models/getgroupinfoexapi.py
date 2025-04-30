# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: ['群聊相关']
@homepage: https://napcat.apifox.cn/226659229e0
@llms.txt: https://napcat.apifox.cn/226659229e0.md
@last_update: 2025-04-27 00:53:40

@description: 

summary:获取群信息ex

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.43"
__endpoint__ = "get_group_info_ex"
__id__ = "226659229e0"
__method__ = "POST"

# endregion METADATA


# region code
from typing import Literal
from pydantic import BaseModel, Field

# region req
class GetGroupInfoExReq(BaseModel):
    """
    获取群信息ex 请求模型
    """
    group_id: str | int = Field(..., description="群号")

# endregion req



# region res
class GetGroupInfoExRes(BaseModel):
    """
    获取群信息ex 响应模型
    """
    status: Literal["ok"] = Field("ok", description="状态码，固定为 'ok'")
    retcode: int = Field(..., description="返回码")
    message: str = Field(..., description="消息")
    wording: str = Field(..., description="提示信息")
    echo: None = Field(..., description="Echo字段，总是为 null")

    class Data(BaseModel):
        """
        响应数据
        """
        groupCode: str = Field(..., description="群号")
        resultCode: int = Field(..., description="结果码")

        class ExtInfo(BaseModel):
            """
            扩展信息
            """

            class GroupOwnerId(BaseModel):
                """
                群主信息
                """
                memberUin: str = Field(..., description="成员UIN")
                memberUid: str = Field(..., description="成员UID")
                memberQid: str = Field(..., description="成员QID")

            class GroupBindGuildIds(BaseModel):
                """
                群绑定频道ID列表
                """
                guildIds: list[str] = Field(..., description="频道ID列表")

            class GroupExtFlameData(BaseModel):
                """
                群拓展火焰数据
                """
                switchState: int = Field(..., description="开关状态")
                state: int = Field(..., description="状态")
                dayNums: list[str] = Field(..., description="天数列表")
                version: int = Field(..., description="版本")
                updateTime: str = Field(..., description="更新时间")
                isDisplayDayNum: bool = Field(..., description="是否显示天数")

            class GroupExcludeGuildIds(BaseModel):
                """
                群排除频道ID列表
                """
                guildIds: list[str] = Field(..., description="频道ID列表")

            groupInfoExtSeq: int = Field(..., description="群信息扩展序列号")
            reserve: int = Field(..., description="保留字段")
            luckyWordId: str = Field(..., description="幸运词ID")
            lightCharNum: int = Field(..., description="亮字数量")
            luckyWord: str = Field(..., description="幸运词")
            starId: int = Field(..., description="星标ID")
            essentialMsgSwitch: int = Field(..., description="重要消息开关")
            todoSeq: int = Field(..., description="待办事项序列号")
            blacklistExpireTime: int = Field(..., description="黑名单过期时间")
            isLimitGroupRtc: int = Field(..., description="是否限制群实时通讯")
            companyId: int = Field(..., description="公司ID")
            hasGroupCustomPortrait: int = Field(..., description="是否有群自定义头像")
            bindGuildId: str = Field(..., description="绑定频道ID")
            groupOwnerId: GroupOwnerId = Field(..., description="群主信息")
            essentialMsgPrivilege: int = Field(..., description="重要消息权限")
            msgEventSeq: str = Field(..., description="消息事件序列号")
            inviteRobotSwitch: int = Field(..., description="邀请机器人开关")
            gangUpId: str = Field(..., description="组队ID")
            qqMusicMedalSwitch: int = Field(..., description="QQ音乐勋章开关")
            showPlayTogetherSwitch: int = Field(..., description="显示一起玩开关")
            groupFlagPro1: str = Field(..., description="群标志属性1")
            groupBindGuildIds: GroupBindGuildIds = Field(..., description="群绑定频道ID列表")
            viewedMsgDisappearTime: str = Field(..., description="已阅消息消失时间")
            groupExtFlameData: GroupExtFlameData = Field(..., description="群拓展火焰数据")
            groupBindGuildSwitch: int = Field(..., description="群绑定频道开关")
            groupAioBindGuildId: str = Field(..., description="群AIO绑定频道ID")
            groupExcludeGuildIds: GroupExcludeGuildIds = Field(..., description="群排除频道ID列表")
            fullGroupExpansionSwitch: int = Field(..., description="满员群扩展开关")
            fullGroupExpansionSeq: str = Field(..., description="满员群扩展序列号")
            inviteRobotMemberSwitch: int = Field(..., description="邀请机器人成员开关")
            inviteRobotMemberExamine: int = Field(..., description="邀请机器人成员审核")
            groupSquareSwitch: int = Field(..., description="群广场开关")

        extInfo: ExtInfo = Field(..., description="扩展信息")

    data: Data = Field(..., description="响应数据")


# endregion res

# region api
class GetGroupInfoExAPI(BaseModel):
    """get_group_info_ex接口数据模型"""
    endpoint: str = "get_group_info_ex"
    method: str = "POST"
    Req: type[BaseModel] = GetGroupInfoExReq
    Res: type[BaseModel] = GetGroupInfoExRes
# endregion api




# endregion code