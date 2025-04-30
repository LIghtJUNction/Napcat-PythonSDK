# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: 消息相关/发送私聊消息
@homepage: https://napcat.apifox.cn/226657399e0
@llms.txt: https://napcat.apifox.cn/226657399e0.md
@last_update: 2025-04-27 00:53:40

@description: 

summary:发送私聊合并转发消息

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.43"
__endpoint__ = "send_private_forward_msg"
__id__ = "226657399e0"
__method__ = "POST"

# endregion METADATA


# region code
from pydantic import BaseModel, Field
from typing import Literal # Used for specific string values like 'ok', 'node'

# region req sub-models

class ForwardTextMsgData(BaseModel):
    """文本消息数据"""
    text: str = Field(..., description="文本内容")

class ForwardTextMsg(BaseModel):
    """文本消息"""
    type: Literal["text"] = Field("text", description="消息类型")
    data: ForwardTextMsgData = Field(..., description="消息数据")

class ForwardAtMsgData(BaseModel):
    """艾特消息数据"""
    qq: int | str | Literal["all"] = Field(..., description="艾特对象的QQ号或all")
    name: str | None = Field(None, description="艾特对象昵称 (可选)")

class ForwardAtMsg(BaseModel):
    """艾特消息"""
    type: Literal["at"] = Field("at", description="消息类型")
    data: ForwardAtMsgData = Field(..., description="消息数据")

class ForwardFaceMsgData(BaseModel):
    """表情消息数据"""
    id: int = Field(..., description="表情ID")

class ForwardFaceMsg(BaseModel):
    """表情消息"""
    type: Literal["face"] = Field("face", description="消息类型")
    data: ForwardFaceMsgData = Field(..., description="消息数据")

class ForwardImageMsgData(BaseModel):
    """图片消息数据"""
    file: str = Field(..., description="图片文件名")
    summary: str | None = Field("[图片]", description="外显 (可选, 默认为[图片])")

class ForwardImageMsg(BaseModel):
    """图片消息"""
    type: Literal["image"] = Field("image", description="消息类型")
    data: ForwardImageMsgData = Field(..., description="消息数据")

class ForwardReplyMsgData(BaseModel):
    """回复消息数据"""
    id: int | str = Field(..., description="回复消息的ID")

class ForwardReplyMsg(BaseModel):
    """回复消息"""
    type: Literal["reply"] = Field("reply", description="消息类型")
    data: ForwardReplyMsgData = Field(..., description="消息数据")

class ForwardJsonMsgData(BaseModel):
    """JSON消息数据"""
    data: str = Field(..., description="JSON字符串")

class ForwardJsonMsg(BaseModel):
    """JSON消息"""
    type: Literal["json"] = Field("json", description="消息类型")
    data: ForwardJsonMsgData = Field(..., description="消息数据")

class ForwardRecordMsgData(BaseModel):
    """语音消息数据"""
    file: str = Field(..., description="语音文件名")

class ForwardRecordMsg(BaseModel):
    """语音消息"""
    type: Literal["record"] = Field("record", description="消息类型")
    data: ForwardRecordMsgData = Field(..., description="消息数据")

class ForwardVideoMsgData(BaseModel):
    """视频消息数据"""
    file: str = Field(..., description="视频文件名")

class ForwardVideoMsg(BaseModel):
    """视频消息"""
    type: Literal["video"] = Field("video", description="消息类型")
    data: ForwardVideoMsgData = Field(..., description="消息数据")

# Define the union of possible message content types
# Using | syntax as per guidelines
ForwardContent = ForwardTextMsg | ForwardAtMsg | ForwardFaceMsg | ForwardImageMsg | ForwardReplyMsg | ForwardJsonMsg | ForwardRecordMsg | ForwardVideoMsg

class ForwardNodeData(BaseModel):
    """合并转发节点数据"""
    nickname: str = Field(..., description="发送者昵称")
    user_id: int | str = Field(..., description="发送者QQ号")
    content: list[ForwardContent] = Field(..., description="节点内容，一个消息列表")

class ForwardNode(BaseModel):
    """合并转发消息节点"""
    type: Literal["node"] = Field("node", description="节点类型，固定为 node")
    data: ForwardNodeData = Field(..., description="节点数据")

# endregion req sub-models

# region req
class SendPrivateForwardMsgReq(BaseModel):
    """
    发送私聊合并转发消息请求模型
    """
    user_id: int | str = Field(..., description="私聊对象QQ号")
    messages: list[ForwardNode] = Field(..., description="合并转发消息节点列表")
# endregion req


# region res sub-models

class SendPrivateForwardMsgResData(BaseModel):
    """发送私聊合并转发消息响应数据模型"""
    message_id: int | float = Field(..., description="发送的消息id")
    res_id: str = Field(..., description="发送的随机id")

# endregion res sub-models

# region res
class SendPrivateForwardMsgRes(BaseModel):
    """
    发送私聊合并转发消息响应模型
    """
    status: Literal["ok"] = Field("ok", description="状态码，固定为 'ok'") # Modified status field
    retcode: int | float = Field(..., description="返回码")
    data: SendPrivateForwardMsgResData = Field(..., description="数据")
    message: str = Field(..., description="消息")
    wording: str = Field(..., description="提示")
    echo: str | None = Field(None, description="echo") # nullable is mapped to | None
# endregion res

# region api
class SendPrivateForwardMsgAPI(BaseModel):
    """send_private_forward_msg接口数据模型"""
    endpoint: str = "send_private_forward_msg"
    method: str = "POST"
    Req: type[BaseModel] = SendPrivateForwardMsgReq
    Res: type[BaseModel] = SendPrivateForwardMsgRes
# endregion api




# endregion code