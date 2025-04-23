# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/226659210e0
@llms.txt: https://napcat.apifox.cn/226659210e0.md
@last_update: 2025-04-23 20:23:17

@description: 

summary:获取收藏表情

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "fetch_custom_face"
__id__ = "226659210e0"
__method__ = "POST"

# region METADATA/


# region code
from typing import Any
from pydantic import BaseModel, Field
from typing import Union

# region req
class FetchCustomFaceReq(BaseModel):
    """
    请求参数
    """

    count: float | None = Field(None, description="")
# region req/


# region res
class FetchCustomFaceRes(BaseModel):
    """
    响应参数
    """

    pass
# region res/

# region api
class FetchCustomFaceAPI(BaseModel):
    
    Request : type[FetchCustomFaceReq] = FetchCustomFaceReq
    Response  : type[FetchCustomFaceRes] = FetchCustomFaceRes


# region api/
# region code/

