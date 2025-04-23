# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/226658740e0
@llms.txt: https://napcat.apifox.cn/226658740e0.md
@last_update: 2025-04-23 20:23:17

@description: 

summary:_发送群公告

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "_send_group_notice"
__id__ = "226658740e0"
__method__ = "POST"

# region METADATA/


# region code
from typing import Any
from pydantic import BaseModel, Field
from typing import Union

# region req
class SendGroupNoticeReq(BaseModel):
    """
    请求参数
    """

    group_id: float | str = Field(..., description="")
    content: str = Field(..., description="内容")
    image: str | None = Field(None, description="图片路径")
# region req/


# region res
class SendGroupNoticeRes(BaseModel):
    """
    响应参数
    """

    pass
# region res/

# region api
class SendGroupNoticeAPI(BaseModel):
    
    Request : type[SendGroupNoticeReq] = SendGroupNoticeReq
    Response  : type[SendGroupNoticeRes] = SendGroupNoticeRes


# region api/
# region code/

