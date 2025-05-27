# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/226659229e0
@llms.txt: https://napcat.apifox.cn/226659229e0.md
@last_update: 2025-05-28 01:34:10

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
from pydantic import BaseModel, Field
from typing import Literal

# region component_models
# OpenAPI schema defines group_id as oneOf: [number, string], not an object.
# No class for group_id is needed as it's a direct type in the request.
# endregion component_models/

# region req
class GetGroupInfoExReq(BaseModel):
    """获取群信息ex"""
    group_id: int | str = Field(description="群ID，可以是数字或字符串")

    model_config = {
        "extra": "allow",
    }
# endregion req/


# region res
class GetGroupInfoExRes(BaseModel):
    """获取群信息ex"""

    class Data(BaseModel):
        """响应数据类型"""

        class ExtInfo(BaseModel):
            """extInfo字段"""

            class GroupOwnerId(BaseModel):
                """groupOwnerId字段"""
                memberUin: str = Field(description="memberUin字段")
                memberUid: str = Field(description="memberUid字段")
                memberQid: str = Field(description="memberQid字段")

                model_config = {
                    "extra": "allow",
                }

            class GroupBindGuildIds(BaseModel):
                """groupBindGuildIds字段"""
                guildIds: list[str] = Field(description="guildIds字段")

                model_config = {
                    "extra": "allow",
                }

            class GroupExtFlameData(BaseModel):
                """groupExtFlameData字段"""
                switchState: int = Field(description="switchState字段")
                state: int = Field(description="state字段")
                dayNums: list[str] = Field(description="dayNums字段")
                version: int = Field(description="version字段")
                updateTime: str = Field(description="updateTime字段")
                isDisplayDayNum: bool = Field(description="isDisplayDayNum字段")

                model_config = {
                    "extra": "allow",
                }

            class GroupExcludeGuildIds(BaseModel):
                """groupExcludeGuildIds字段"""
                guildIds: list[str] = Field(description="guildIds字段")

                model_config = {
                    "extra": "allow",
                }

            groupInfoExtSeq: int = Field(description="groupInfoExtSeq字段")
            reserve: int = Field(description="reserve字段")
            luckyWordId: str = Field(description="luckyWordId字段")
            lightCharNum: int = Field(description="lightCharNum字段")
            luckyWord: str = Field(description="luckyWord字段")
            starId: int = Field(description="starId字段")
            essentialMsgSwitch: int = Field(description="essentialMsgSwitch字段")
            todoSeq: int = Field(description="todoSeq字段")
            blacklistExpireTime: int = Field(description="blacklistExpireTime字段")
            isLimitGroupRtc: int = Field(description="isLimitGroupRtc字段")
            companyId: int = Field(description="companyId字段")
            hasGroupCustomPortrait: int = Field(description="hasGroupCustomPortrait字段")
            bindGuildId: str = Field(description="bindGuildId字段")
            groupOwnerId: GroupOwnerId = Field(description="groupOwnerId字段")
            essentialMsgPrivilege: int = Field(description="essentialMsgPrivilege字段")
            msgEventSeq: str = Field(description="msgEventSeq字段")
            inviteRobotSwitch: int = Field(description="inviteRobotSwitch字段")
            gangUpId: str = Field(description="gangUpId字段")
            qqMusicMedalSwitch: int = Field(description="qqMusicMedalSwitch字段")
            showPlayTogetherSwitch: int = Field(description="showPlayTogetherSwitch字段")
            groupFlagPro1: str = Field(description="groupFlagPro1字段")
            groupBindGuildIds: GroupBindGuildIds = Field(description="groupBindGuildIds字段")
            viewedMsgDisappearTime: str = Field(description="viewedMsgDisappearTime字段")
            groupExtFlameData: GroupExtFlameData = Field(description="groupExtFlameData字段")
            groupBindGuildSwitch: int = Field(description="groupBindGuildSwitch字段")
            groupAioBindGuildId: str = Field(description="groupAioBindGuildId字段")
            groupExcludeGuildIds: GroupExcludeGuildIds = Field(description="groupExcludeGuildIds字段")
            fullGroupExpansionSwitch: int = Field(description="fullGroupExpansionSwitch字段")
            fullGroupExpansionSeq: str = Field(description="fullGroupExpansionSeq字段")
            inviteRobotMemberSwitch: int = Field(description="inviteRobotMemberSwitch字段")
            inviteRobotMemberExamine: int = Field(description="inviteRobotMemberExamine字段")
            groupSquareSwitch: int = Field(description="groupSquareSwitch字段")

            model_config = {
                "extra": "allow",
            }

        groupCode: str = Field(description="groupCode字段")
        resultCode: float = Field(description="resultCode字段")
        extInfo: ExtInfo = Field(description="extInfo字段")

        model_config = {
            "extra": "allow",
        }

    status: Literal["ok"] = Field(description="status字段", default="ok")
    retcode: float = Field(description="retcode字段", default=0.0)
    data: Data = Field(description="data字段")
    message: str = Field(description="message字段", default="")
    wording: str = Field(description="wording字段", default="")
    echo: None = Field(description="echo字段", default=None)

    model_config = {
        "extra": "allow",
    }
# endregion res/

# region api
class GetGroupInfoExAPI(BaseModel):
    """get_group_info_ex接口数据模型"""
    endpoint: str = "get_group_info_ex"
    method: str = "POST"
    Req: type[BaseModel] = GetGroupInfoExReq
    Res: type[BaseModel] = GetGroupInfoExRes

# endregion api/
# endregion code
