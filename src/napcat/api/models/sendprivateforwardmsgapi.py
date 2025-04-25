# -*- coding: utf-8 -*- 
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/226657399e0
@llms.txt: https://napcat.apifox.cn/226657399e0.md
@last_update: 2025-04-25 23:00:49

@description: 

summary:发送私聊合并转发消息

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "send_private_forward_msg"
__id__ = "226657399e0"
__method__ = "POST"

# region METADATA/


# region code
from pydantic import BaseModel, Field
import logging

logger = logging.getLogger(__name__)

# region component_models
class VideoMessageData(BaseModel):
    file: str = Field(..., description="文件")

class VideoMessage(BaseModel):
    type: str = Field("video", const=True, description="类型")
    data: VideoMessageData = Field(..., description="数据")


class VoiceMessageData(BaseModel):
    file: str = Field(..., description="文件")

class VoiceMessage(BaseModel):
    type: str = Field("record", const=True, description="类型")
    data: VoiceMessageData = Field(..., description="数据")


class JSONMessageData(BaseModel):
    data: str = Field(..., description="数据")

class JSONMessage(BaseModel):
    type: str = Field("json", const=True, description="类型")
    data: JSONMessageData = Field(..., description="数据")


class ReplyMessageData(BaseModel):
    id: str | int = Field(..., description="ID")


class ReplyMessage(BaseModel):
    type: str = Field("reply", const=True, description="类型")
    data: ReplyMessageData = Field(..., description="数据")


class ImageMessageData(BaseModel):
    file: str = Field(..., description="文件")
    summary: str = Field("[图片]", description="概要")


class ImageMessage(BaseModel):
    type: str = Field("image", const=True, description="类型")
    data: ImageMessageData = Field(..., description="数据")


class FaceMessageData(BaseModel):
    id: int = Field(..., description="ID")


class FaceMessage(BaseModel):
    type: str = Field("face", const=True, description="类型")
    data: FaceMessageData = Field(..., description="数据")


class AtMessageData(BaseModel):
    qq: str | int = Field(..., description="QQ")
    name: str = Field(..., description="名称")


class AtMessage(BaseModel):
    type: str = Field("at", const=True, description="类型")
    data: AtMessageData = Field(..., description="数据")


class TextMessageData(BaseModel):
    text: str = Field(..., description="文本")


class TextMessage(BaseModel):
    type: str = Field("text", const=True, description="类型")
    data: TextMessageData = Field(..., description="数据")


UserId = str | int


class ResultData(BaseModel):
    pass


class Result(BaseModel):
    status: str = Field("ok", const=True, description="状态")
    retcode: float = Field(..., description="返回码")
    data: ResultData = Field(..., description="数据")
    message: str = Field(..., description="消息")
    wording: str = Field(..., description="提示语")
    echo: str | None = Field(None, description="回显")


# region component_models/

# region req
class NodeMessageContentItem(BaseModel):
    __root__: TextMessage | AtMessage | FaceMessage | ImageMessage | ReplyMessage | JSONMessage | VoiceMessage | VideoMessage

class NodeMessageData(BaseModel):
    nickname: str = Field(..., description="昵称")
    user_id: UserId = Field(..., description="用户ID")
    content: list[NodeMessageContentItem] = Field(..., description="内容")

class NodeMessage(BaseModel):
    type: str = Field("node", const=True, description="类型")
    data: NodeMessageData = Field(..., description="数据")

class SendPrivateForwardMsgReq(BaseModel):
    """发送私聊合并转发消息"""
    user_id: UserId = Field(..., description="用户ID")
    messages: list[NodeMessage] = Field(..., description="消息列表")

    model_config = {
        "extra": "allow",
    }


# region req/


# region res
class SendPrivateForwardMsgRes(BaseModel):
    """发送私聊合并转发消息"""

    class ResponseData(BaseModel):
        """响应数据类型"""
        message_id: float = Field(..., description="消息ID")
        res_id: str = Field(..., description="资源ID")

        model_config = {
            "extra": "allow",
        }

    status: str = Field("ok", const=True, description="状态")
    retcode: float = Field(..., description="返回码")
    data: ResponseData = Field(..., description="数据")
    message: str = Field(..., description="消息")
    wording: str = Field(..., description="提示语")
    echo: str | None = Field(None, description="回显")

    model_config = {
        "extra": "allow",
    }


# region res/

# region api
class SendPrivateForwardMsgAPI(BaseModel):
    """send_private_forward_msg接口数据模型"""
    endpoint: str = Field("send_private_forward_msg", description="端点")
    method: str = Field("POST", description="方法")
    Req: type[BaseModel] = Field(SendPrivateForwardMsgReq, description="请求模型")
    Res: type[BaseModel] = Field(SendPrivateForwardMsgRes, description="响应模型")
    logger: logging.Logger = Field(default_factory=lambda: logging.getLogger(__name__), description="日志记录器")

    def __call__(self, req: SendPrivateForwardMsgReq) -> SendPrivateForwardMsgRes:
        """
        调用API的方法（仅作为接口定义，不包含实际请求逻辑）

        Args:
            req: 请求参数对象

        Returns:
            响应对象
        """
        # 调试日志
        self.logger.debug(f"调用 SendPrivateForwardMsgAPI API")
        self.logger.debug(f"请求参数: {req.model_dump_json()}")

        # 注意：这里不应该包含实际的请求逻辑
        # 这个方法只是定义了接口，实际的请求应由适配器或客户端实现
        raise NotImplementedError("此方法需要由实际的API客户端实现")


# region api/
# region code/