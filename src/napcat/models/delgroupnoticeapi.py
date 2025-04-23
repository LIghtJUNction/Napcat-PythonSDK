# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/226659240e0
@llms.txt: https://napcat.apifox.cn/226659240e0.md
@last_update: 2025-04-23 20:23:17

@description: 

summary:_删除群公告

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "_del_group_notice"
__id__ = "226659240e0"
__method__ = "POST"

# region METADATA/


# region code
from typing import Any
from pydantic import BaseModel, Field
from typing import Union

# region req
class DelGroupNoticeReq(BaseModel):
    """
    请求参数
    """

    group_id: float | str = Field(..., description="")
    notice_id: str = Field(..., description="")
# region req/


# region res
class DelGroupNoticeRes(BaseModel):
    """
    响应参数
    """

    result: float = Field(..., description="")
    errMsg: str = Field(..., description="")
# region res/

# region api
class DelGroupNoticeAPI(BaseModel):
    
    Request : type[DelGroupNoticeReq] = DelGroupNoticeReq
    Response  : type[DelGroupNoticeRes] = DelGroupNoticeRes


# region api/
# region code/

