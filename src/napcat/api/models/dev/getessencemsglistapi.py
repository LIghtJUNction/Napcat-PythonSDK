# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: 群聊相关
@homepage: https://napcat.apifox.cn/226658664e0
@llms.txt: https://napcat.apifox.cn/226658664e0.md
@last_update: 2025-04-27 00:53:40

@description: 

summary:获取群精华消息

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.43"
__endpoint__ = "get_essence_msg_list"
__id__ = "226658664e0"
__method__ = "POST"

# endregion METADATA


# region code
from pydantic import BaseModel, Field
from typing import Literal

# region req
class GetEssenceMsgListReq(BaseModel):
    """
    获取群精华消息请求模型
    """

    group_id: int | str = Field(
        ..., description="群号", examples=[1012451981]
    )
# endregion req


# region res

class TextMsgData(BaseModel):
    """
    文本消息数据模型
    """
    text: str


class TextMsgSegment(BaseModel):
    """
    文本消息段模型
    """

    type: Literal["text"] = Field(..., description="消息段类型")
    data: TextMsgData = Field(..., description="消息段数据")


class ImageMsgData(BaseModel):
    """
    图片消息数据模型
    """

    url: str = Field(..., description="图片URL")


class ImageMsgSegment(BaseModel):
    """
    图片消息段模型
    """

    type: Literal["image"] = Field(..., description="消息段类型")
    data: ImageMsgData = Field(..., description="消息段数据")


class EssenceMsgItem(BaseModel):
    """
    群精华消息条目模型
    """

    msg_seq: int
    msg_random: int
    sender_id: int = Field(..., description="发送人账号")
    sender_nick: str = Field(..., description="发送人昵称")
    operator_id: int = Field(..., description="设精人账号")
    operator_nick: str = Field(..., description="设精人昵称")
    message_id: int
    operator_time: int = Field(..., description="设精时间")
    content: list[TextMsgSegment | ImageMsgSegment] = Field(
        ..., description="消息内容"
    )


class GetEssenceMsgListRes(BaseModel):
    """
    获取群精华消息响应模型
    """

    status: Literal["ok"] = Field(..., description="状态")
    retcode: int = Field(..., description="返回码")
    data: list[EssenceMsgItem] = Field(..., description="精华消息列表")
    message: str = Field(..., description="消息")
    wording: str = Field(..., description="描述")
    echo: str | None = Field(None, description="Echo值")
# endregion res


# region api
class GetEssenceMsgListAPI(BaseModel):
    """get_essence_msg_list接口数据模型"""

    endpoint: str = "get_essence_msg_list"
    method: str = "POST"
    Req: type[BaseModel] = GetEssenceMsgListReq
    Res: type[BaseModel] = GetEssenceMsgListRes
# endregion api


# endregion code