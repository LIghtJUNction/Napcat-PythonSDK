# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/226656802e0
@llms.txt: https://napcat.apifox.cn/226656802e0.md
@last_update: 2025-04-23 20:23:17

@description: 

summary:全体禁言

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "set_group_whole_ban"
__id__ = "226656802e0"
__method__ = "POST"

# region METADATA/


# region code
from typing import Any
from pydantic import BaseModel, Field
from typing import Union

# region req
class SetGroupWholeBanReq(BaseModel):
    """
    请求参数
    """

    group_id: float | str = Field(..., description="")
    enable: bool = Field(..., description="")
# region req/


# region res
class SetGroupWholeBanRes(BaseModel):
    """
    响应参数
    """

    pass
# region res/

# region api
class SetGroupWholeBanAPI(BaseModel):
    
    Request : type[SetGroupWholeBanReq] = SetGroupWholeBanReq
    Response  : type[SetGroupWholeBanRes] = SetGroupWholeBanRes


# region api/
# region code/

