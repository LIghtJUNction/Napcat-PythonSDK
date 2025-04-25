# -*- coding: utf-8 -*- 
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/226659136e0
@llms.txt: https://napcat.apifox.cn/226659136e0.md
@last_update: 2025-04-25 23:00:49

@description: 

summary:发送合并转发消息

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "send_forward_msg"
__id__ = "226659136e0"
__method__ = "POST"

# region METADATA/


# region code
from pydantic import BaseModel, Field
from typing import Any, Union
import logging

logger = logging.getLogger(__name__)

# region component_models
class 文本消息Data(BaseModel):
    text: str = Field(..., description="文本内容")

class 文本消息(BaseModel):
    type: str = Field("text", const=True, description="消息类型")
    data: 文本消息Data = Field(..., description="消息数据")

class 表情消息Data(BaseModel):
    id: int = Field(..., description="表情ID")

class 表情消息(BaseModel):
    type: str = Field("face", const=True, description="消息类型")
    data: 表情消息Data = Field(..., description="消息数据")

class 图片消息Data(BaseModel):
    file: str = Field(..., description="图片文件路径")
    summary: str = Field("[图片]", description="图片描述")

class 图片消息(BaseModel):
    type: str = Field("image", const=True, description="消息类型")
    data: 图片消息Data = Field(..., description="消息数据")

class 回复消息Data(BaseModel):
    id: str | int = Field(..., description="回复消息ID")

class 回复消息(BaseModel):
    type: str = Field("reply", const=True, description="消息类型")
    data: 回复消息Data = Field(..., description="消息数据")

class JSON消息Data(BaseModel):
    data: str = Field(..., description="JSON数据")

class JSON消息(BaseModel):
    type: str = Field("json", const=True, description="消息类型")
    data: JSON消息Data = Field(..., description="消息数据")

class 视频消息Data(BaseModel):
    file: str = Field(..., description="视频文件路径")

class 视频消息(BaseModel):
    type: str = Field("video", const=True, description="消息类型")
    data: 视频消息Data = Field(..., description="消息数据")

class 文件消息Data(BaseModel):
    file: str = Field(..., description="文件路径")
    name: str | None = Field(None, description="文件名")

class 文件消息(BaseModel):
    type: str = Field("file", const=True, description="消息类型")
    data: 文件消息Data = Field(..., description="消息数据")

class Markdown消息Data(BaseModel):
    content: str = Field(..., description="Markdown内容")

class Markdown消息(BaseModel):
    type: str = Field("record", const=True, description="消息类型")
    data: Markdown消息Data = Field(..., description="消息数据")


class UserID(BaseModel):
    id: str | int = Field(..., description="用户ID")
    name: str | None = Field(None, description="用户名")


class GroupID(BaseModel):
    id: str | int = Field(..., description="群组ID")
    name: str | None = Field(None, description="群组名称")


class Forward消息Data(BaseModel):
    id: str = Field(..., description="转发消息ID")

class Forward消息内容(BaseModel):
    type: str = Field("forward", const=True, description="消息类型")
    data: Forward消息Data = Field(..., description="消息数据")

class 发送forwardData(BaseModel):
    user_id: UserID = Field(..., description="用户信息")
    nickname: str = Field(..., description="用户昵称")
    content: Forward消息内容 = Field(..., description="转发消息内容")

class 发送forward(BaseModel):
    type: str = Field("node", const=True, description="消息类型")
    data: 发送forwardData = Field(..., description="消息数据")

MessageItem = Union[文本消息, 表情消息, 图片消息, 回复消息, JSON消息, 视频消息, 文件消息, Markdown消息, 发送forward]

class 二级合并转发消息Data(BaseModel):
    user_id: str | int = Field(..., description="用户ID")
    nickname: str = Field(..., description="用户昵称")
    content: list[MessageItem] = Field(..., description="消息内容")
    news: list[dict[str,str]] |None = Field(None, description="外显")
    prompt: str | None = Field(None, description="外显")
    summary: str | None= Field(None, description="底下文本")
    source: str | None = Field(None, description="标题")

class 二级合并转发消息(BaseModel):
    type: str = Field("node", const=True, description="消息类型")
    data: 二级合并转发消息Data = Field(..., description="消息数据")


MessageItem_level1 = Union[文本消息, 表情消息, 图片消息, 回复消息, JSON消息, 视频消息, 文件消息, Markdown消息, 发送forward,二级合并转发消息]

class 一级合并转发消息Data(BaseModel):
    user_id: str | int = Field(..., description="用户ID")
    nickname: str = Field(..., description="用户昵称")
    content: list[MessageItem_level1] = Field(..., description="消息内容")

class 一级合并转发消息(BaseModel):
    type: str = Field("node", const=True, description="消息类型")
    data: 一级合并转发消息Data = Field(..., description="消息数据")

class NewsItem(BaseModel):
    text: str = Field(..., description="内容")

class ResultData(BaseModel):
    pass

class Result(BaseModel):
    status: str = Field("ok", const=True, description="状态")
    retcode: int = Field(..., description="返回码")
    data: ResultData = Field(..., description="数据")
    message: str = Field(..., description="消息")
    wording: str = Field(..., description="提示语")
    echo: str | None = Field(None, description="回显")


# region component_models/

# region req
class SendForwardMsgReq(BaseModel):
    """发送合并转发消息"""
    group_id: str | int | None = Field(None, description="群组ID")
    user_id: str | int | None = Field(None, description="用户ID")
    messages: list[一级合并转发消息] = Field(..., description="消息列表")
    news: list[NewsItem] = Field(..., description="外显列表")
    prompt: str = Field(..., description="外显")
    summary: str = Field(..., description="底下文本")
    source: str = Field(..., description="内容")

# region req/


# region res
class SendForwardMsgRes(Result):
    """发送合并转发消息"""
    data: ResultData = Field(..., description="响应数据")

# region res/

# region api
class SendForwardMsgAPI(BaseModel):
    """send_forward_msg接口数据模型"""
    endpoint: str = "send_forward_msg"
    method: str = "POST"
    Req: type[BaseModel] = SendForwardMsgReq
    Res: type[BaseModel] = SendForwardMsgRes
    logger = logging.getLogger(__name__)

    def __init__(self) -> None:
        super().__init__()
        self.logger.debug("初始化 SendForwardMsgAPI")

    def __call__(self, req: SendForwardMsgReq) -> SendForwardMsgRes:
        """
        调用API的方法（仅作为接口定义，不包含实际请求逻辑）
        
        Args:
            req: 请求参数对象
            
        Returns:
            响应对象
        """
        # 调试日志
        self.logger.debug(f"调用 SendForwardMsgAPI API")
        self.logger.debug(f"请求参数: {req.model_dump_json()}")
        
        # 注意：这里不应该包含实际的请求逻辑
        # 这个方法只是定义了接口，实际的请求应由适配器或客户端实现
        raise NotImplementedError("此方法需要由实际的API客户端实现")

# region api/
# region code/
