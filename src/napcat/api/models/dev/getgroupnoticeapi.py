# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: 群聊相关
@homepage: https://napcat.apifox.cn/226658742e0
@llms.txt: https://napcat.apifox.cn/226658742e0.md
@last_update: 2025-04-26 01:17:44

@description: 

summary: _获取群公告

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "_get_group_notice"
__id__ = "226658742e0"
__method__ = "POST"

# endregion METADATA


# region code
import logging
from pydantic import BaseModel, Field

logger = logging.getLogger(__name__)

# region req
class GetGroupNoticeReq(BaseModel):
    """
    _获取群公告 请求
    """

    group_id: int | str = Field(..., description="群号")

# endregion req

# region res

class GetGroupNoticeMessageItem(BaseModel):
    """
    群公告消息列表项
    """
    id: str = Field(..., description="消息ID")
    height: str = Field(..., description="高度")
    width: str = Field(..., description="宽度")

class GetGroupNoticeDataItem(BaseModel):
    """
    群公告数据列表项
    """
    notice_id: str = Field(..., description="公告ID")
    sender_id: int = Field(..., description="发送人账号")
    publish_time: int = Field(..., description="发送时间")
    message: list[GetGroupNoticeMessageItem] = Field(..., description="消息列表")

class GetGroupNoticeRes(BaseModel):
    """
    _获取群公告 响应
    """
    status: str = Field(..., description="状态")
    retcode: int = Field(..., description="返回码")
    data: list[GetGroupNoticeDataItem] = Field(..., description="响应数据")
    message: str = Field(..., description="消息")
    wording: str = Field(..., description="补充说明")
    echo: str | None = Field(default=None, description="Echo")

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
