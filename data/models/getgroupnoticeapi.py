# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: 群聊相关
@homepage: https://napcat.apifox.cn/226658742e0
@llms.txt: https://napcat.apifox.cn/226658742e0.md
@last_update: 2025-04-30 00:00:00

@description: 
获取群聊公告内容，支持查询指定群聊的全部公告信息

summary:_获取群公告

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.43"
__endpoint__ = "_get_group_notice"
__id__ = "226658742e0"
__method__ = "POST"

# endregion METADATA


# region code
import logging
from typing import Literal
from pydantic import BaseModel, Field

logger = logging.getLogger(__name__)

# region req
class GetGroupNoticeReq(BaseModel):
    """
    获取群公告请求参数
    """
    group_id: int | str = Field(..., description="群号")
# endregion req


# region res
class NoticeMessageItem(BaseModel):
    """
    公告消息中的图片项
    """
    id: str = Field(..., description="图片ID")
    height: str = Field(..., description="图片高度")
    width: str = Field(..., description="图片宽度")


class GroupNoticeInfo(BaseModel):
    """
    群公告信息
    """
    notice_id: str = Field(..., description="公告ID")
    sender_id: int = Field(..., description="发送人账号")
    publish_time: int = Field(..., description="发送时间")
    message: list[NoticeMessageItem] = Field(..., description="公告消息内容")


class GetGroupNoticeRes(BaseModel):
    """
    获取群公告响应数据
    """
    status: Literal["ok"] = Field("ok", description="状态码，固定为 'ok'")
    retcode: int = Field(..., description="返回码")
    data: list[GroupNoticeInfo] = Field(..., description="群公告列表")
    message: str = Field(..., description="消息")
    wording: str = Field(..., description="提示词")
    echo: str | None = Field(default=None, description="回显")
# endregion res

# region api
class GetGroupNoticeAPI(BaseModel):
    """_get_group_notice接口数据模型"""
    endpoint: str = "_get_group_notice"
    method: str = "POST"
    Req: type[BaseModel] = GetGroupNoticeReq
    Res: type[BaseModel] = GetGroupNoticeRes
# endregion api


# endregion code

