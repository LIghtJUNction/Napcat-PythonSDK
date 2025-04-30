# -*- coding: utf-8 -*-
from __future__ import annotations
# region METADATA
"""
@tags: 群聊相关
@homepage: https://napcat.apifox.cn/226658742e0
@llms.txt: https://napcat.apifox.cn/226658742e0.md
@last_update: 2025-04-27 00:53:40

@description: 

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
from typing import Literal, Any
from pydantic import BaseModel, Field

logger = logging.getLogger(__name__)
logger.debug("加载 GetGroupNoticeAPI 模型")

# region req
class GetGroupNoticeReq(BaseModel):
    """
    _获取群公告 请求参数
    """
    group_id: int | str = Field(..., description="群号")

# endregion req


# region res
class MessageItem(BaseModel):
    """
    群公告消息内容项
    """
    id: str = Field(..., description="消息内容项ID")
    height: str = Field(..., description="高度")
    width: str = Field(..., description="宽度")

class NoticeItem(BaseModel):
    """
    群公告信息项
    """
    notice_id: str = Field(..., description="公告ID")
    sender_id: int = Field(..., description="发送人账号")
    publish_time: int = Field(..., description="发送时间")
    # 注意：message 字段在规范中有冲突
    # schema 定义为 MessageItem 对象的数组
    # 但示例中是有 text 和 image 字段的对象
    message: list[MessageItem] | dict[str, Any] = Field(..., description="公告消息内容")


class GetGroupNoticeRes(BaseModel):
    """
    _获取群公告 响应参数
    """
    status: Literal["ok"] = Field("ok", description="状态码，固定为 'ok'")
    retcode: int = Field(..., description="返回码")
    data: list[NoticeItem] = Field(..., description="公告列表")
    message: str = Field(..., description="响应消息")
    wording: str = Field(..., description="响应描述")
    echo: str | None = Field(None, description="echo")

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