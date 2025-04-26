# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/226658740e0
@llms.txt: https://napcat.apifox.cn/226658740e0.md
@last_update: 2025-04-26 01:17:44

@description: 

summary:_发送群公告

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "_send_group_notice"
__id__ = "226658740e0"
__method__ = "POST"

# endregion METADATA


# region code
from typing import Literal
from pydantic import BaseModel, Field


# region req
class SendGroupNoticeReq(BaseModel):
    """
    发送群公告请求体
    """

    group_id: int | str = Field(
        ...,
        description="群号",
        # group_id is oneOf number or string based on schema
    )
    content: str = Field(
        ...,
        description="内容",
    )
    image: str | None = Field(
        None,
        description="图片路径",
        # image is optional/nullable based on schema
    )
# endregion req



# region res
class SendGroupNoticeRes(BaseModel):
    """
    发送群公告响应体
    """
    # Based on the overridden schema, data is null and required
    status: Literal['ok'] = Field("ok", description="状态")
    retcode: int = Field(..., description="返回码")
    data: None = Field(..., description="数据部分，此接口为null")
    message: str = Field(..., description="消息")
    wording: str = Field(..., description="进一步的说明")
    echo: str | None = Field(
        None,
        description="回显，如果请求时指定了echo，则会原样返回",
    )
# endregion res

# region api
class SendGroupNoticeAPI(BaseModel):
    """_send_group_notice接口数据模型"""
    endpoint: str = "_send_group_notice"
    method: str = "POST"
    Req: type[BaseModel] = SendGroupNoticeReq
    Res: type[BaseModel] = SendGroupNoticeRes
# endregion api




# endregion code
