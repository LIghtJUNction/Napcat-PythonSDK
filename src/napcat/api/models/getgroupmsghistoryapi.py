# -*- coding: utf-8 -*-
from __future__ import annotations
# region METADATA
"""
@tags: ['消息相关']
@homepage: https://napcat.apifox.cn/226657401e0
@llms.txt: https://napcat.apifox.cn/226657401e0.md
@last_update: 2025-04-27 00:53:40

@description: 

summary:获取群历史消息

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.43"
__endpoint__ = "get_group_msg_history"
__id__ = "226657401e0"
__method__ = "POST"

# endregion METADATA


# region code
from typing import Literal
from pydantic import BaseModel, Field

# region req
class GetGroupMsgHistoryReq(BaseModel):
    """
    获取群历史消息请求模型
    """
    group_id: int | str = Field(..., description="群号")
    message_seq: int | str | None = Field(default=None, description="起始消息序号，0为最新")
    count: int = Field(default=20, description="获取数量")
    reverseOrder: bool = Field(default=True, description="是否倒序获取")
# endregion req



# region res

class GetGroupMsgHistoryRes(BaseModel):
    """
    获取群历史消息响应模型
    """
    status: Literal["ok"] = Field("ok", description="状态码，固定为 'ok'") # Fixed status field
    retcode: int = Field(..., description="返回码")
    data: "GetGroupMsgHistoryRes.Data" = Field(..., description="数据") # Forward reference to nested Data
    message: str = Field(..., description="消息")
    wording: str = Field(..., description="wording")
    echo: str | None = Field(default=None, description="echo") # Fixed echo field

    class Data(BaseModel):
        """历史消息响应数据"""
        messages: list["GetGroupMsgHistoryRes.Data.MessageDetail"] = Field(..., description="历史消息列表") # Forward reference to nested MessageDetail

        class MessageDetail(BaseModel):
            """消息详情"""
            self_id: int = Field(..., description="机器人账号")
            user_id: int = Field(..., description="发送者账号")
            time: int = Field(..., description="时间戳")
            message_id: int = Field(..., description="消息ID")
            message_seq: int = Field(..., description="消息序列号")
            real_id: int = Field(..., description="实时ID")
            real_seq: str = Field(..., description="实时序列号")
            message_type: str = Field(..., description="消息类型 (e.g., group, private)")
            sender: GetGroupMsgHistoryRes.Data.MessageDetail.Sender = Field(..., description="发送者信息") 
            raw_message: str = Field(..., description="原始消息字符串")
            font: int = Field(..., description="字体")
            sub_type: str = Field(..., description="消息子类型")
            message: list[GetGroupMsgHistoryRes.Data.MessageDetail.MessageContent] = Field(..., description="消息内容列表")
            message_format: str = Field(..., description="消息格式")
            post_type: str = Field(..., description="POST类型")
            group_id: int | None = Field(default=None, description="群ID (仅群聊)")

            class Sender(BaseModel):
                """发送者信息"""
                user_id: int = Field(..., description="发送者用户ID")
                nickname: str = Field(..., description="发送者昵称")
                sex: Literal["male", "female", "unknown"] | None = Field(default=None, description="性别")
                age: int | None = Field(default=None, description="年龄")
                card: str = Field(..., description="群名片")
                role: Literal["owner", "admin", "member"] | None = Field(default=None, description="角色")

            # --- Nested Message Content Data Models (within MessageDetail) ---
            class MessageTypeTextData(BaseModel):
                """文本消息数据"""
                text: str = Field(..., description="文本内容")

            class MessageTypeAtData(BaseModel):
                """@消息数据"""
                qq: int | str = Field(..., description="@的QQ号，all为全体成员")
                name: str | None = Field(default=None, description="@的昵称")

            class MessageTypeFaceData(BaseModel):
                """表情消息数据"""
                id: int = Field(..., description="表情ID")

            class MessageTypeImageData(BaseModel):
                """图片消息数据"""
                file: str = Field(..., description="图片文件名")
                summary: str = Field(default='[图片]', description="外显内容")

            class MessageTypeFileData(BaseModel):
                """文件消息数据"""
                file: str = Field(..., description="文件ID或文件名")
                name: str = Field(..., description="文件名")

            class MessageTypeReplyData(BaseModel):
                """回复消息数据"""
                id: int | str = Field(..., description="回复的消息ID")

            class MessageTypeJsonData(BaseModel):
                """JSON消息数据"""
                data: str = Field(..., description="JSON字符串")

            class MessageTypeRecordDataVoice(BaseModel):
                """语音消息数据"""
                file: str = Field(..., description="语音文件名")

            class MessageTypeRecordDataMarkdown(BaseModel):
                 """Markdown消息数据"""
                 content: str = Field(..., description="Markdown文本内容")

            class MessageTypeVideoData(BaseModel):
                """视频消息数据"""
                file: str = Field(..., description="视频文件名")

            # --- Recursive Forward Message Data Model (within MessageDetail) ---
            class MessageTypeForwardData(BaseModel):
                """转发消息数据"""
                id: str = Field(..., description="转发消息ID")
                content: list["GetGroupMsgHistoryRes.Data.MessageDetail"] = Field(..., description="转发消息内容列表") # Recursive forward reference


            # --- Nested Message Content Models (with type discriminator, within MessageDetail) ---
            class MessageTypeText(BaseModel):
                """文本消息结构"""
                type: Literal["text"] = "text"
                data: "GetGroupMsgHistoryRes.Data.MessageDetail.MessageTypeTextData" = Field(...) # Forward reference

            class MessageTypeAt(BaseModel):
                """@消息结构"""
                type: Literal["at"] = "at"
                data: "GetGroupMsgHistoryRes.Data.MessageDetail.MessageTypeAtData" = Field(...) # Forward reference

            class MessageTypeFace(BaseModel):
                """表情消息结构"""
                type: Literal["face"] = "face"
                data: "GetGroupMsgHistoryRes.Data.MessageDetail.MessageTypeFaceData" = Field(...) # Forward reference

            class MessageTypeImage(BaseModel):
                """图片消息结构"""
                type: Literal["image"] = "image"
                data: "GetGroupMsgHistoryRes.Data.MessageDetail.MessageTypeImageData" = Field(...) # Forward reference

            class MessageTypeFile(BaseModel):
                """文件消息结构"""
                type: Literal["file"] = "file"
                data: "GetGroupMsgHistoryRes.Data.MessageDetail.MessageTypeFileData" = Field(...) # Forward reference

            class MessageTypeReply(BaseModel):
                """回复消息结构"""
                type: Literal["reply"] = "reply"
                data: "GetGroupMsgHistoryRes.Data.MessageDetail.MessageTypeReplyData" = Field(...) # Forward reference

            class MessageTypeJson(BaseModel):
                """JSON消息结构"""
                type: Literal["json"] = "json"
                data: "GetGroupMsgHistoryRes.Data.MessageDetail.MessageTypeJsonData" = Field(...) # Forward reference

            class MessageTypeVoice(BaseModel):
                """语音消息结构 (record type)"""
                type: Literal["record"] = "record"
                data: "GetGroupMsgHistoryRes.Data.MessageDetail.MessageTypeRecordDataVoice" = Field(...) # Forward reference

            class MessageTypeMarkdown(BaseModel):
                """Markdown消息结构 (record type)"""
                type: Literal["record"] = "record"
                data: "GetGroupMsgHistoryRes.Data.MessageDetail.MessageTypeRecordDataMarkdown" = Field(...) # Forward reference

            class MessageTypeVideo(BaseModel):
                """视频消息结构"""
                type: Literal["video"] = "video"
                data: "GetGroupMsgHistoryRes.Data.MessageDetail.MessageTypeVideoData" = Field(...) # Forward reference

            class MessageTypeForward(BaseModel):
                """转发消息结构"""
                type: Literal["forward"] = "forward"
                data: "GetGroupMsgHistoryRes.Data.MessageDetail.MessageTypeForwardData" = Field(...) # Forward reference

            # --- Message Content Union Type (within MessageDetail) ---
            type MessageContent = (
                MessageTypeText | MessageTypeAt | MessageTypeFace | MessageTypeImage |
                MessageTypeFile | MessageTypeReply | MessageTypeJson | MessageTypeVoice |
                MessageTypeMarkdown | MessageTypeVideo | MessageTypeForward
            )


# --- Model Rebuild for Forward References and Recursion ---
# Rebuild the top-level class which contains all nested classes involved in forward references/recursion.
GetGroupMsgHistoryRes.model_rebuild()


# endregion res

# region api
class GetGroupMsgHistoryAPI(BaseModel):
    """get_group_msg_history接口数据模型"""
    endpoint: str = "get_group_msg_history"
    method: str = "POST"
    Req: type[BaseModel] = GetGroupMsgHistoryReq
    Res: type[BaseModel] = GetGroupMsgHistoryRes
# endregion api

# endregion code