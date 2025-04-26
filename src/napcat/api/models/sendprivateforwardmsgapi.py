# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: 消息相关/发送私聊消息
@homepage: https://napcat.apifox.cn/226657399e0
@llms.txt: https://napcat.apifox.cn/226657399e0.md
@last_update: 2025-04-26 01:17:44

@description: 

summary:发送私聊合并转发消息

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "send_private_forward_msg"
__id__ = "226657399e0"
__method__ = "POST"

# endregion METADATA


# region code
from pydantic import BaseModel, Field
from typing import Literal # Use Literal for const fields

# region req


class TextMessage(BaseModel):
    """文本消息段"""
    class TextMsgData(BaseModel):
        """文本消息数据"""
        text: str = Field(..., description="文本内容")

    type: Literal['text'] = Field(..., description="消息段类型，固定为 'text'")
    data: TextMsgData = Field(..., description="消息数据")
class AtMessage(BaseModel):
    """@消息段"""

    class AtMsgData(BaseModel):
        """@消息数据"""
        qq: str | int = Field(..., description="@的 QQ 号，'all' 表示@全体成员")
        name: str = Field(..., description="@的群名片，仅在群聊中有效")

    type: Literal['at'] = Field(..., description="消息段类型，固定为 'at'")
    data: AtMsgData = Field(..., description="消息数据")

class FaceMessage(BaseModel):
    """表情消息段"""
    class FaceMsgData(BaseModel):
        """表情消息数据"""
        id: int = Field(..., description="表情 ID")
    
    type: Literal['face'] = Field(..., description="消息段类型，固定为 'face'")
    data: FaceMsgData = Field(..., description="消息数据")

class ImageMessage(BaseModel):
    """图片消息段"""
    class ImageMsgData(BaseModel):
        """图片消息数据"""
        file: str = Field(..., description="图片文件名或 URL")
        summary: str = Field('[图片]', description="图片简介，默认 '[图片]'")

    type: Literal['image'] = Field(..., description="消息段类型，固定为 'image'")
    data: ImageMsgData = Field(..., description="消息数据")
class ReplyMessage(BaseModel):
    """回复消息段"""
    class ReplyMsgData(BaseModel):
        """回复消息数据"""
        id: str | int = Field(..., description="回复消息的 ID")

    type: Literal['reply'] = Field(..., description="消息段类型，固定为 'reply'")
    data: ReplyMsgData = Field(..., description="消息数据")
class JsonMessage(BaseModel):
    """JSON消息段"""
    class JsonMsgData(BaseModel):
        """JSON消息数据"""
        data: str = Field(..., description="JSON 字符串") # Note: field name is 'data' in OpenAPI


    type: Literal['json'] = Field(..., description="消息段类型，固定为 'json'")
    data: JsonMsgData = Field(..., description="消息数据")
class RecordMessage(BaseModel):
    """语音消息段"""
    class RecordMsgData(BaseModel):
        """语音消息数据"""
        file: str = Field(..., description="语音文件名或 URL")


    type: Literal['record'] = Field(..., description="消息段类型，固定为 'record'")
    data: RecordMsgData = Field(..., description="消息数据")
class VideoMessage(BaseModel):
    """视频消息段"""
    class VideoMsgData(BaseModel):
        """视频消息数据"""
        file: str = Field(..., description="视频文件名或 URL")


    type: Literal['video'] = Field(..., description="消息段类型，固定为 'video'")
    data: VideoMsgData = Field(..., description="消息数据")

type MessageSegment = TextMessage | AtMessage | FaceMessage | ImageMessage | ReplyMessage | JsonMessage | RecordMessage | VideoMessage

class SendPrivateForwardMsgReq(BaseModel):
    """
    发送私聊合并转发消息的请求模型
    """
    class NodeMessage(BaseModel):
        """合并转发消息节点"""
        class NodeData(BaseModel):
            """合并转发消息节点数据"""
            nickname: str = Field(..., description="节点发送者昵称")
            user_id: str | int = Field(..., description="节点发送者 QQ 号")
            content: list[MessageSegment] = Field(..., description="节点消息内容列表")

        type: Literal['node'] = Field(..., description="消息节点类型，固定为 'node'")
        data: NodeData = Field(..., description="节点数据")


    user_id: str | int = Field(..., description="私聊对象 QQ 号")
    messages: list[NodeMessage] = Field(..., description="合并转发消息节点列表")

# endregion req



# region res


class SendPrivateForwardMsgRes(BaseModel):
    """
    发送私聊合并转发消息的响应模型
    """
    class SendPrivateForwardMsgDataRes(BaseModel):
        """发送私聊合并转发消息的响应数据"""
        message_id: int = Field(..., description="消息 ID")
        res_id: str = Field(..., description="资源 ID")


    status: Literal['ok'] = Field("ok", description="响应状态")
    retcode: int = Field(..., description="状态码")
    data: SendPrivateForwardMsgDataRes = Field(..., description="响应数据")
    message: str = Field(..., description="错误信息")
    wording: str = Field(..., description="错误描述")
    echo: str | None = Field(None, description="echo")

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
