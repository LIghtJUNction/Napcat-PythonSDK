# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/226658742e0
@llms.txt: https://napcat.apifox.cn/226658742e0.md
@last_update: 2025-05-28 01:34:09

@description: 

summary:_获取群公告

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.43"
__endpoint__ = "_get_group_notice"
__id__ = "226658742e0"
__method__ = "POST"

# endregion METADATA


# region code
from pydantic import BaseModel, Field
from typing import Literal

# region req
class GetGroupNoticeReq(BaseModel):
    """_获取群公告 - 请求模型"""
    # 修复：根据OpenAPI components/schemas/group_id 定义 (oneOf: number, string)，group_id 应为 int 或 str 类型，而非对象
    group_id: int | str = Field(description="群号")

    model_config = {
        "extra": "allow",
    }
# endregion req/


# region res
class GetGroupNoticeRes(BaseModel):
    """_获取群公告 - 响应模型"""

    class MessageContentItem(BaseModel):
        """公告消息内容项"""
        id: str = Field(description="消息内容ID")
        height: str = Field(description="内容高度")
        width: str = Field(description="内容宽度")

        model_config = {
            "extra": "allow",
        }

    class NoticeItem(BaseModel):
        """单个群公告信息"""
        notice_id: str = Field(description="公告ID")
        # 修复：OpenAPI 定义为 number，但通常这类 ID 或时间戳为整数，故改为 int
        sender_id: int = Field(description="发送人账号")
        # 修复：OpenAPI 定义为 number，但通常这类 ID 或时间戳为整数，故改为 int
        publish_time: int = Field(description="发送时间戳")
        # 修复：根据 OpenAPI 响应 schema 的 data.items.properties.message 定义，为 MessageContentItem 列表，而非示例中的 text/image 结构
        message: list[MessageContentItem] = Field(description="公告消息内容列表")

        model_config = {
            "extra": "allow",
        }

    # 修复：status 字段应使用 Literal["ok"] 类型，表示固定值
    status: Literal["ok"] = Field(default="ok", description="响应状态")
    retcode: float = Field(default=0.0, description="响应码")
    # 修复：data 字段应为 NoticeItem 列表，并提供 default_factory 处理可变类型
    data: list[NoticeItem] = Field(default_factory=list, description="公告数据列表")
    message: str = Field(default="", description="响应消息")
    wording: str = Field(default="", description="响应提示")
    echo: str | None = Field(default=None, description="回显数据")

    model_config = {
        "extra": "allow",
    }
# endregion res/

# region api
class GetGroupNoticeAPI(BaseModel):
    """_get_group_notice接口数据模型"""
    endpoint: str = "_get_group_notice"
    method: str = "POST"
    Req: type[BaseModel] = GetGroupNoticeReq
    Res: type[BaseModel] = GetGroupNoticeRes

# region api/
# endregion code
