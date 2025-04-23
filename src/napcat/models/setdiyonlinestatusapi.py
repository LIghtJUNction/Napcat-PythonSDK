# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/266151905e0
@llms.txt: https://napcat.apifox.cn/266151905e0.md
@last_update: 2025-04-23 20:23:18

@description: 

summary:设置自定义在线状态

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "set_diy_online_status"
__id__ = "266151905e0"
__method__ = "POST"

# region METADATA/


# region code
from typing import Any
from pydantic import BaseModel, Field
from typing import Union

# region req
class SetDiyOnlineStatusReq(BaseModel):
    """
    请求参数
    """

    face_id: Any = Field(..., description="表情ID")
    face_type: Any | None = Field(None, description="表情ID")
    wording: str | None = Field(None, description="描述文本")
# region req/


# region res
class SetDiyOnlineStatusRes(BaseModel):
    """
    响应参数
    """

    pass
# region res/

# region api
class SetDiyOnlineStatusAPI(BaseModel):
    
    Request : type[SetDiyOnlineStatusReq] = SetDiyOnlineStatusReq
    Response  : type[SetDiyOnlineStatusRes] = SetDiyOnlineStatusRes


# region api/
# region code/

