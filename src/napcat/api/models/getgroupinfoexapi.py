# -*- coding: utf-8 -*-

"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/226659229e0
@llms.txt: https://napcat.apifox.cn/226659229e0.md
@last_update: 2025-04-25 23:00:50

@description: 

summary:获取群信息ex

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "get_group_info_ex"
__id__ = "226659229e0"
__method__ = "POST"


from pydantic import BaseModel, Field
from typing import Any
import logging

logger = logging.getLogger(__name__)


class GroupId(BaseModel):
    id: str | int = Field(description="标识ID")
    name: str | None = Field(None, description="名称")

    model_config = {
        "extra": "allow",
    }


class GetGroupInfoExReq(BaseModel):
    """获取群信息ex"""
    group_id: GroupId = Field(description="群组ID")

    model_config = {
        "extra": "allow",
    }


class GroupOwnerId(BaseModel):
    member_uin: str = Field(description="Member Uin")
    member_uid: str = Field(description="Member Uid")
    member_qid: str = Field(description="Member Qid")

    model_config = {
        "extra": "allow",
    }


class GroupBindGuildIds(BaseModel):
    guild_ids: list[str] = Field(description="Guild Ids")

    model_config = {
        "extra": "allow",
    }


class GroupExtFlameData(BaseModel):
    switch_state: int = Field(description="Switch State")
    state: int = Field(description="State")
    day_nums: list[str] = Field(description="Day Nums")
    version: int = Field(description="Version")
    update_time: str = Field(description="Update Time")
    is_display_day_num: bool = Field(description="Is Display Day Num")

    model_config = {
        "extra": "allow",
    }


class GroupExcludeGuildIds(BaseModel):
    guild_ids: list[str] = Field(description="Guild Ids")

    model_config = {
        "extra": "allow",
    }


class Extinfo(BaseModel):
    group_info_ext_seq: int = Field(description="Group Info Ext Seq")
    reserve: int = Field(description="Reserve")
    lucky_word_id: str = Field(description="Lucky Word Id")
    light_char_num: int = Field(description="Light Char Num")
    lucky_word: str = Field(description="Lucky Word")
    star_id: int = Field(description="Star Id")
    essential_msg_switch: int = Field(description="Essential Msg Switch")
    todo_seq: int = Field(description="Todo Seq")
    blacklist_expire_time: int = Field(description="Blacklist Expire Time")
    is_limit_group_rtc: int = Field(description="Is Limit Group Rtc")
    company_id: int = Field(description="Company Id")
    has_group_custom_portrait: int = Field(description="Has Group Custom Portrait")
    bind_guild_id: str = Field(description="Bind Guild Id")
    group_owner_id: GroupOwnerId = Field(description="Group Owner Id")
    essential_msg_privilege: int = Field(description="Essential Msg Privilege")
    msg_event_seq: str = Field(description="Msg Event Seq")
    invite_robot_switch: int = Field(description="Invite Robot Switch")
    gang_up_id: str = Field(description="Gang Up Id")
    qq_music_medal_switch: int = Field(description="Qq Music Medal Switch")
    show_play_together_switch: int = Field(description="Show Play Together Switch")
    group_flag_pro1: str = Field(description="Group Flag Pro1")
    group_bind_guild_ids: GroupBindGuildIds = Field(description="Group Bind Guild Ids")
    viewed_msg_disappear_time: str = Field(description="Viewed Msg Disappear Time")
    group_ext_flame_data: GroupExtFlameData = Field(description="Group Ext Flame Data")
    group_bind_guild_switch: int = Field(description="Group Bind Guild Switch")
    group_aio_bind_guild_id: str = Field(description="Group Aio Bind Guild Id")
    group_exclude_guild_ids: GroupExcludeGuildIds = Field(description="Group Exclude Guild Ids")
    full_group_expansion_switch: int = Field(description="Full Group Expansion Switch")
    full_group_expansion_seq: str = Field(description="Full Group Expansion Seq")
    invite_robot_member_switch: int = Field(description="Invite Robot Member Switch")
    invite_robot_member_examine: int = Field(description="Invite Robot Member Examine")
    group_square_switch: int = Field(description="Group Square Switch")

    model_config = {
        "extra": "allow",
    }


class ResponseData(BaseModel):
    """响应数据类型"""
    group_code: str = Field(description="groupCode字段")
    result_code: float = Field(description="resultCode字段")
    ext_info: Extinfo = Field(description="extInfo字段")

    model_config = {
        "extra": "allow",
    }


class GetGroupInfoExRes(BaseModel):
    """获取群信息ex"""
    status: str = Field(default="ok", description="status字段")
    retcode: float = Field(default=0, description="retcode字段")
    data: ResponseData = Field(description="data字段")
    message: str = Field(default="", description="message字段")
    wording: str = Field(default="", description="wording字段")
    echo: None = Field(default=None, description="echo字段")

    model_config = {
        "extra": "allow",
    }


class GetGroupInfoExAPI(BaseModel):
    """get_group_info_ex接口数据模型"""
    endpoint: str = Field(default="get_group_info_ex", description="Endpoint")
    method: str = Field(default="POST", description="Method")
    Req: type[BaseModel] = Field(default=GetGroupInfoExReq, description="Request Model")
    Res: type[BaseModel] = Field(default=GetGroupInfoExRes, description="Response Model")
    logger: logging.Logger = Field(default_factory=lambda: logging.getLogger(__name__), description="Logger")

    def __init__(self) -> None:
        super().__init__()
        self.logger.debug("初始化 GetGroupInfoExAPI")

    def __call__(self, req: GetGroupInfoExReq) -> GetGroupInfoExRes:
        """
        调用API的方法（仅作为接口定义，不包含实际请求逻辑）
        
        Args:
            req: 请求参数对象
            
        Returns:
            响应对象
        """
        # 调试日志
        self.logger.debug(f"调用 GetGroupInfoExAPI API")
        self.logger.debug(f"请求参数: {req.model_dump_json()}")
        
        # 注意：这里不应该包含实际的请求逻辑
        # 这个方法只是定义了接口，实际的请求应由适配器或客户端实现
        raise NotImplementedError("此方法需要由实际的API客户端实现")
