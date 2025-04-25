# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: 消息相关
@homepage: https://napcat.apifox.cn/226659174e0
@llms.txt: https://napcat.apifox.cn/226659174e0.md
@last_update: 2025-04-26 01:17:44

@description: 获取好友历史消息

summary:获取好友历史消息

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "get_friend_msg_history"
__id__ = "226659174e0"
__method__ = "POST"

# endregion METADATA


# region code
import logging
import enum
from pydantic import BaseModel, Field

logger = logging.getLogger(__name__)

# region enums

class Sex(enum.Enum):
    male = "male"
    female = "female"
    unknown = "unknown"

class Role(enum.Enum):
    owner = "owner"
    admin = "admin"
    member = "member"

# endregion enums

# region nested_models

class Sender(BaseModel):
    """发送者信息"""
    user_id: int = Field(..., description="用户 ID")
    nickname: str = Field(..., description="昵称")
    sex: Sex | None = Field(None, description="性别, male 或 female 或 unknown")
    age: int | None = Field(None, description="年龄")
    card: str | None = Field(None, description="群名片/备注")
    role: Role | None = Field(None, description="群角色, owner 或 admin 或 member")

class TextMsgData(BaseModel):
    text: str

class TextMsg(BaseModel):
    """文本消息"""
    type: str = Field("text", literal=True)
    data: TextMsgData

class AtMsgData(BaseModel):
    qq: str | int | Literal["all"]
    name: str | None = Field(None)

class AtMsg(BaseModel):
    """@消息"""
    type: str = Field("at", literal=True)
    data: AtMsgData

class FaceMsgData(BaseModel):
    id: int

class FaceMsg(BaseModel):
    """表情消息"""
    type: str = Field("face", literal=True)
    data: FaceMsgData

class ImageMsgData(BaseModel):
    file: str
    summary: str = Field("[图片]", description="图片摘要")

class ImageMsg(BaseModel):
    """图片消息"""
    type: str = Field("image", literal=True)
    data: ImageMsgData

class FileMsgData(BaseModel):
    file: str
    name: str | None = Field(None, description="文件名")

class FileMsg(BaseModel):
    """文件消息"""
    type: str = Field("file", literal=True)
    data: FileMsgData

class ReplyMsgData(BaseModel):
    id: str | int

class ReplyMsg(BaseModel):
    """回复消息"""
    type: str = Field("reply", literal=True)
    data: ReplyMsgData

class JsonMsgData(BaseModel):
    data: str

class JsonMsg(BaseModel):
    """JSON消息"""
    type: str = Field("json", literal=True)
    data: JsonMsgData

class VoiceMsgData(BaseModel):
    file: str

class VoiceMsg(BaseModel):
    """语音消息 (注意: OpenAPI spec has conflicting type 'record' with MarkdownMsg)"""
    type: str = Field("record", literal=True)
    data: VoiceMsgData

class VideoMsgData(BaseModel):
    file: str

class VideoMsg(BaseModel):
    """视频消息"""
    type: str = Field("video", literal=True)
    data: VideoMsgData

class MarkdownMsgData(BaseModel):
    content: str

class MarkdownMsg(BaseModel):
    """Markdown消息 (注意: OpenAPI spec has conflicting type 'record' with VoiceMsg)"""
    type: str = Field("record", literal=True)
    data: MarkdownMsgData

class ForwardMsgData(BaseModel):
    id: str
    content: list['Message']

class ForwardMsg(BaseModel):
    """Forward消息"""
    type: str = Field("forward", literal=True)
    data: ForwardMsgData

# Define the union of all possible message types
MsgData = TextMsg | AtMsg | FaceMsg | ImageMsg | FileMsg | ReplyMsg | JsonMsg | VoiceMsg | VideoMsg | MarkdownMsg | ForwardMsg

class Message(BaseModel):
    """消息详情"""
    self_id: int = Field(..., description="接收此消息的机器人的 QQ 号")
    user_id: int = Field(..., description="发送者的 QQ 号")
    time: int = Field(..., description="消息发送的时间戳")
    message_id: int = Field(..., description="消息 ID")
    message_seq: int = Field(..., description="消息序列号")
    real_id: int = Field(..., description="实际消息 ID (目前和 message_id 一致)")
    real_seq: str = Field(..., description="实际消息序列号 (目前和 message_seq 一致)")
    message_type: str = Field(..., description="消息类型, 如: private, group")
    sender: Sender = Field(..., description="发送者信息")
    raw_message: str = Field(..., description="原始消息字符串")
    font: int = Field(..., description="字体")
    sub_type: str = Field(..., description="消息子类型, 如: friend")
    message: list[MsgData] = Field(..., description="消息内容") # list of message segments
    message_format: str = Field(..., description="消息格式, 如: string, array")
    post_type: str = Field(..., description="上报类型, 如: message")
    group_id: int | None = Field(None, description="群号 (如果是群消息)")

# endregion nested_models

# region req
class GetFriendMsgHistoryReq(BaseModel):
    """获取好友历史消息请求"""
    user_id: str | int = Field(..., description="好友 QQ 号")
    message_seq: str | int | None = Field(None, description="消息序列号, 0 为最新")
    count: int | None = Field(None, description="数量")
    reverseOrder: bool = Field(False, description="是否倒序")

# endregion req



# region res
class GetFriendMsgHistoryResData(BaseModel):
    """响应数据"""
    messages: list[Message] = Field(..., description="历史消息列表")

class GetFriendMsgHistoryRes(BaseModel):
    """获取好友历史消息响应"""
    status: str = Field(..., description="状态")
    retcode: int = Field(..., description="返回码")
    data: GetFriendMsgHistoryResData = Field(..., description="响应数据")
    message: str = Field(..., description="消息")
    wording: str = Field(..., description="wording")
    echo: str | None = Field(None, description="echo")

# endregion res

# region api
class GetFriendMsgHistoryAPI(BaseModel):
    """get_friend_msg_history接口数据模型"""
    endpoint: str = "get_friend_msg_history"
    method: str = "POST"
    Req: type[BaseModel] = GetFriendMsgHistoryReq
    Res: type[BaseModel] = GetFriendMsgHistoryRes
# endregion api




# endregion code
