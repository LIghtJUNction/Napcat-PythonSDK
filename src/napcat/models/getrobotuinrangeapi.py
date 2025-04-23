# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/226658975e0
@llms.txt: https://napcat.apifox.cn/226658975e0.md
@last_update: 2025-04-23 20:23:17

@description: 

summary:获取机器人账号范围

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "get_robot_uin_range"
__id__ = "226658975e0"
__method__ = "POST"

# region METADATA/


# region code
from typing import Any
from pydantic import BaseModel, Field

# region req
class GetRobotUinRangeReq(BaseModel):
    """
    请求参数
    """

    pass
# region req/


# region res
class GetRobotUinRangeRes(BaseModel):
    """
    响应参数
    """

    pass
# region res/

# region api
class GetRobotUinRangeAPI(BaseModel):
    
    Request : type[GetRobotUinRangeReq] = GetRobotUinRangeReq
    Response  : type[GetRobotUinRangeRes] = GetRobotUinRangeRes


# region api/
# region code/

