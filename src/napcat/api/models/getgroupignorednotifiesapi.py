# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: ['群聊相关']
@homepage: https://napcat.apifox.cn/226659323e0
@llms.txt: https://napcat.apifox.cn/226659323e0.md
@last_update: 2025-04-27 00:53:40

@description: 

summary:获取群过滤系统消息

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.43"
__endpoint__ = "get_group_ignored_notifies"
__id__ = "226659323e0"
__method__ = "POST"

# endregion METADATA


# region code
import logging
from pydantic import BaseModel, Field
from typing import Literal

logger = logging.getLogger(__name__)

# region req
class GetGroupIgnoredNotifiesReq(BaseModel):
    """
    请求参数
    """
    # 请求体为空，无需定义字段
    pass
# endregion req



# region res
class GetGroupIgnoredNotifiesRes(BaseModel):
    """
    响应参数
    """



    class Data(BaseModel):
        """
        响应数据详情
        """
        class SystemInfo(BaseModel):
            """
            系统信息详情
            """
            request_id: int = Field(..., description="请求ID")
            invitor_uin: int = Field(..., description="邀请者UIN")
            invitor_nick: str = Field(..., description="邀请者昵称")
            group_id: int = Field(..., description="群组ID")
            message: str = Field(..., description="消息内容")
            group_name: str = Field(..., description="群组名称")
            checked: bool = Field(..., description="是否已处理")
            actor: int = Field(..., description="处理者UIN，0表示未处理")
            requester_nick: str = Field(..., description="请求者昵称")

        join_requests: list[SystemInfo] = Field(..., description="加群请求列表")
        InvitedRequest: list[SystemInfo] = Field(..., description="邀请加入群组请求列表")

    status: Literal["ok"] = Field("ok", description="状态码，固定为 'ok'")
    retcode: int = Field(..., description="返回码")
    data: Data = Field(..., description="响应数据")
    message: str = Field(..., description="消息")
    wording: str = Field(..., description="提示文本")
    echo: str | None = Field(..., description="Echo")


# endregion res

# region api
class GetGroupIgnoredNotifiesAPI(BaseModel):
    """get_group_ignored_notifies接口数据模型"""
    endpoint: str = "get_group_ignored_notifies"
    method: str = "POST"
    Req: type[BaseModel] = GetGroupIgnoredNotifiesReq
    Res: type[BaseModel] = GetGroupIgnoredNotifiesRes
# endregion api




# endregion code