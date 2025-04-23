# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/228534361e0
@llms.txt: https://napcat.apifox.cn/228534361e0.md
@last_update: 2025-04-23 20:23:18

@description: 

summary:检查链接安全性

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "check_url_safely"
__id__ = "228534361e0"
__method__ = "POST"

# region METADATA/


# region code
from typing import Any
from pydantic import BaseModel, Field

# region req

# region req/


# region res
class CheckUrlSafelyRes(BaseModel):
    """
    响应参数
    """

    pass
# region res/

# region api
class CheckUrlSafelyAPI(BaseModel):
    
    Request : type[CheckUrlSafelyReq] = CheckUrlSafelyReq
    Response  : type[CheckUrlSafelyRes] = CheckUrlSafelyRes


# region api/
# region code/

