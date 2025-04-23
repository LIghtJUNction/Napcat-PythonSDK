# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/283136268e0
@llms.txt: https://napcat.apifox.cn/283136268e0.md
@last_update: 2025-04-23 20:23:18

@description: 

summary:设置群备注

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "set_group_remark"
__id__ = "283136268e0"
__method__ = "POST"

# region METADATA/


# region code
from typing import Any
from pydantic import BaseModel, Field

# region req
class SetGroupRemarkReq(BaseModel):
    """
    请求参数
    """

    group_id: str = Field(..., description="")
    remark: str = Field(..., description="")
# region req/


# region res
class SetGroupRemarkRes(BaseModel):
    """
    响应参数
    """

    pass
# region res/

# region api
class SetGroupRemarkAPI(BaseModel):
    
    Request : type[SetGroupRemarkReq] = SetGroupRemarkReq
    Response  : type[SetGroupRemarkRes] = SetGroupRemarkRes


# region api/
# region code/

