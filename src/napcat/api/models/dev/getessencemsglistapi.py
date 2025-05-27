# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/226658664e0
@llms.txt: https://napcat.apifox.cn/226658664e0.md
@last_update: 2025-05-28 01:34:09

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

# region component_models
# The original 'group_id' component model was incorrect based on OpenAPI `oneOf` definition.
# It's directly handled as `int | str` in the request model.
# The 'result' component model is removed as 'GetEssenceMsgListRes' explicitly defines its fields.
# '图片消息' and '文本消息' component models are not used as defined in the response structure
# and are replaced by specific nested classes within 'GetEssenceMsgListRes'.
# endregion component_models/

# region req
class GetEssenceMsgListReq(BaseModel):
    """获取群精华消息请求模型"""
    group_id: int | str = Field(description="群号，可以是数字或字符串")

    model_config = {
        "extra": "allow",
    }
# endregion req/


# region res
class GetEssenceMsgListRes(BaseModel):
    """获取群精华消息响应模型"""

    class TextContentData(BaseModel):
        text: str = Field(description="文本内容")

        model_config = {
            "extra": "allow",
        }

    class TextContent(BaseModel):
        type: Literal["text"] = Field(description="消息类型，固定为 'text'")
        data: "GetEssenceMsgListRes.TextContentData" = Field(description="消息数据")

        model_config = {
            "extra": "allow",
        }

    class ImageContentData(BaseModel):
        # This data structure is specific to the 'content' field in the response,
        # overriding the general '图片消息' component defined in OpenAPI components.
        url: str = Field(description="图片URL")

        model_config = {
            "extra": "allow",
        }

    class ImageContent(BaseModel):
        type: Literal["image"] = Field(description="消息类型，固定为 'image'")
        data: "GetEssenceMsgListRes.ImageContentData" = Field(description="消息数据")

        model_config = {
            "extra": "allow",
        }

    class EssenceMessageItem(BaseModel):
        """群精华消息条目"""
        msg_seq: float = Field(description="消息序号")
        msg_random: float = Field(description="消息随机数")
        sender_id: float = Field(description="发送人账号")
        sender_nick: str = Field(description="发送人昵称")
        operator_id: float = Field(description="设精人账号")
        operator_nick: str = Field(description="设精人昵称")
        message_id: float = Field(description="消息ID")
        operator_time: float = Field(description="设精时间")
        content: list["GetEssenceMsgListRes.TextContent | GetEssenceMsgListRes.ImageContent"] = Field(description="消息内容，包含文本或图片消息对象")

        model_config = {
            "extra": "allow",
        }

    status: Literal["ok"] = Field(default="ok", description="响应状态")
    retcode: float = Field(default=0.0, description="响应码")
    data: list["GetEssenceMsgListRes.EssenceMessageItem"] = Field(default_factory=list, description="响应数据")
    message: str = Field(default="", description="详细信息")
    wording: str = Field(default="", description="提示词")
    echo: str | None = Field(default=None, description="回显数据")

    model_config = {
        "extra": "allow",
    }
# endregion res/

# region api
class GetEssenceMsgListAPI(BaseModel):
    """get_essence_msg_list接口数据模型"""
    endpoint: str = "get_essence_msg_list"
    method: str = "POST"
    Req: type[BaseModel] = GetEssenceMsgListReq
    Res: type[BaseModel] = GetEssenceMsgListRes

# endregion api/
# endregion code
