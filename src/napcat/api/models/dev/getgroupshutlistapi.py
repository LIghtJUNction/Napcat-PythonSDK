# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/226659300e0
@llms.txt: https://napcat.apifox.cn/226659300e0.md
@last_update: 2025-05-28 01:34:10

@description:

summary:获取群禁言列表

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.43"
__endpoint__ = "get_group_shut_list"
__id__ = "226659300e0"
__method__ = "POST"

# endregion METADATA


# region code
from pydantic import BaseModel, Field
from typing import Literal, Any # `Any` is needed for dict[str, Any]

# region req
class GetGroupShutListReq(BaseModel):
    """获取群禁言列表请求模型"""
    group_id: str | int = Field(..., description="群ID，可以是数字或字符串")

    model_config = {
        "extra": "allow",
    }
# endregion req/


# region res
class GetGroupShutListRes(BaseModel):
    """获取群禁言列表响应模型"""
    class MemberItem(BaseModel):
        """禁言成员详细信息"""
        uid: str = Field(..., description="用户ID")
        qid: str = Field(..., description="QID")
        uin: str = Field(..., description="UIN")
        nick: str = Field(..., description="昵称")
        remark: str = Field(..., description="备注")
        card_type: int = Field(..., description="卡片类型")
        card_name: str = Field(..., description="卡片名称")
        role: int = Field(..., description="角色")
        avatar_path: str = Field(..., description="头像路径")
        shut_up_time: int = Field(..., description="解禁时间，UNIX时间戳")
        is_delete: bool = Field(..., description="是否已删除")
        is_special_concerned: bool = Field(..., description="是否特别关注")
        is_special_shield: bool = Field(..., description="是否特别屏蔽")
        is_robot: bool = Field(..., description="是否是机器人")
        group_honor: dict[str, Any] = Field(default_factory=dict, description="群荣誉信息")
        member_real_level: int = Field(..., description="群聊真实等级")
        member_level: int = Field(..., description="群成员等级")
        global_group_level: int = Field(..., description="全局群等级")
        global_group_point: int = Field(..., description="全局群积分")
        member_title_id: int = Field(..., description="成员头衔ID")
        member_special_title: str = Field(..., description="成员特殊头衔")
        last_speak_time: int = Field(..., description="最后发言时间，UNIX时间戳")
        join_time: int = Field(..., description="入群时间，UNIX时间戳")
        special_title_expire_time: str = Field(..., description="特殊头衔过期时间")
        user_show_flag: int = Field(..., description="用户显示标志")
        user_show_flag_new: int = Field(..., description="新用户显示标志")
        rich_flag: int = Field(..., description="富文本标志")
        mss_vip_type: int = Field(..., description="MSS VIP类型")
        big_club_level: int = Field(..., description="大会员等级")
        big_club_flag: int = Field(..., description="大会员标志")
        auto_remark: str = Field(..., description="自动备注")
        credit_level: int = Field(..., description="信用等级")
        member_flag: int = Field(..., description="成员标志")
        member_flag_ext: int = Field(..., description="成员扩展标志")
        member_mobile_flag: int = Field(..., description="成员手机标志")
        member_flag_ext2: int = Field(..., description="成员扩展标志2")
        is_special_shielded: bool = Field(..., description="是否被特别屏蔽")
        card_name_id: int = Field(..., description="卡片名称ID")

        model_config = {
            "extra": "allow",
        }

    status: Literal["ok"] = Field("ok", description="状态码，固定为 'ok'")
    retcode: float = Field(0.0, description="返回码")
    data: list[MemberItem] = Field(default_factory=list, description="禁言成员列表")
    message: str = Field("", description="消息")
    wording: str = Field("", description="提示词")
    echo: str | None = Field(None, description="回声")

    model_config = {
        "extra": "allow",
    }
# endregion res/

# region api
class GetGroupShutListAPI(BaseModel):
    """get_group_shut_list接口数据模型"""
    endpoint: str = "get_group_shut_list"
    method: str = "POST"
    Req: type[BaseModel] = GetGroupShutListReq
    Res: type[BaseModel] = GetGroupShutListRes

# endregion api/
# endregion code
