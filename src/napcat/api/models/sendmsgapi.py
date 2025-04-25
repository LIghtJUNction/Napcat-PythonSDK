# -*- coding: utf-8 -*- 
# region METADATA
"""
@tags: 其他/保留
@homepage: https://napcat.apifox.cn/226656652e0
@llms.txt: https://napcat.apifox.cn/226656652e0.md
@last_update: 2025-04-25 23:00:48

@description: 

summary:send_msg

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "send_msg"
__id__ = "226656652e0"
__method__ = "POST"

# region METADATA/


# region code
from pydantic import BaseModel, Field
from typing import Any
import logging
from typing import Union

logger = logging.getLogger(__name__)

# region component_models
class Markdown消息Data(BaseModel):
    content: str = Field(..., description="markdown内容")

class Markdown消息(BaseModel):
    type: str = Field("record", const=True, description="消息类型，固定为record")
    data: Markdown消息Data = Field(..., description="markdown数据")

class 视频消息Data(BaseModel):
    file: str = Field(..., description="视频文件路径")

class 视频消息(BaseModel):
    type: str = Field("video", const=True, description="消息类型，固定为video")
    data: 视频消息Data = Field(..., description="视频数据")

class 语音消息Data(BaseModel):
    file: str = Field(..., description="语音文件路径")

class 语音消息(BaseModel):
    type: str = Field("record", const=True, description="消息类型，固定为record")
    data: 语音消息Data = Field(..., description="语音数据")

class JSON消息Data(BaseModel):
    data: str = Field(..., description="JSON数据")

class JSON消息(BaseModel):
    type: str = Field("json", const=True, description="消息类型，固定为json")
    data: JSON消息Data = Field(..., description="JSON数据")

class 回复消息Data(BaseModel):
    id: str | int = Field(..., description="回复的消息ID")

class 回复消息(BaseModel):
    type: str = Field("reply", const=True, description="消息类型，固定为reply")
    data: 回复消息Data = Field(..., description="回复数据")

class 图片消息Data(BaseModel):
    file: str = Field(..., description="图片文件路径")
    summary: str = Field("[图片]", description="图片描述")

class 图片消息(BaseModel):
    type: str = Field("image", const=True, description="消息类型，固定为image")
    data: 图片消息Data = Field(..., description="图片数据")

class 表情消息Data(BaseModel):
    id: int = Field(..., description="表情ID")

class 表情消息(BaseModel):
    type: str = Field("face", const=True, description="消息类型，固定为face")
    data: 表情消息Data = Field(..., description="表情数据")

class 艾特消息Data(BaseModel):
    qq: str | int | str = Field(..., description="要艾特的QQ号，all表示全体成员")
    name: str = Field(..., description="艾特昵称")

class 艾特消息(BaseModel):
    type: str = Field("at", const=True, description="消息类型，固定为at")
    data: 艾特消息Data = Field(..., description="艾特数据")

class 文本消息Data(BaseModel):
    text: str = Field(..., description="文本内容")

class 文本消息(BaseModel):
    type: str = Field("text", const=True, description="消息类型，固定为text")
    data: 文本消息Data = Field(..., description="文本数据")

GroupId = str | int
UserId = str | int

class ResultData(BaseModel):
    message_id: float = Field(..., description="消息ID")

class Result(BaseModel):
    status: str = Field("ok", const=True, description="状态码，固定为ok")
    retcode: float = Field(..., description="返回码")
    data: ResultData = Field(..., description="返回数据")
    message: str = Field(..., description="消息内容")
    wording: str = Field(..., description="提示语")
    echo: str | None = Field(None, description="回显数据")

# region component_models/

# region req
class SendMsgReq(BaseModel):
    """send_msg"""
    message_type: str = Field(..., description="消息类型 group | private", const=True)
    group_id: GroupId = Field(..., description="群ID")
    user_id: UserId = Field(..., description="用户ID, type为group时不填写")
    message: list[Union[文本消息, 艾特消息, 表情消息, 图片消息, 回复消息, JSON消息, 语音消息, 视频消息, Markdown消息]] = Field(..., description="消息体")

# region req/


# region res
class SendMsgRes(BaseModel):
    """send_msg"""

    status: str = Field("ok", description="status字段")
    retcode: float = Field(0, description="retcode字段")
    data: ResultData = Field(description="data字段")
    message: str = Field("", description="message字段")
    wording: str = Field("", description="wording字段")
    echo: str | None = Field(None, description="echo字段")

# region res/

# region api
class SendMsgAPI(BaseModel):
    """send_msg接口数据模型"""
    endpoint: str = "send_msg"
    method: str = "POST"
    Req: type[BaseModel] = SendMsgReq
    Res: type[BaseModel] = SendMsgRes
    logger = logging.getLogger(__name__)

    def __init__(self) -> None:
        super().__init__()
        self.logger.debug("初始化 SendMsgAPI")

    def __call__(self, req: SendMsgReq) -> SendMsgRes:
        """
        调用API的方法（仅作为接口定义，不包含实际请求逻辑）
        
        Args:
            req: 请求参数对象
            
        Returns:
            响应对象
        """
        # 调试日志
        self.logger.debug(f"调用 SendMsgAPI API")
        self.logger.debug(f"请求参数: {req.model_dump_json()}")
        
        # 注意：这里不应该包含实际的请求逻辑
        # 这个方法只是定义了接口，实际的请求应由适配器或客户端实现
        raise NotImplementedError("此方法需要由实际的API客户端实现")

# region api/
# region code/
