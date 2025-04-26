# -*- coding: utf-8 -*-# region METADATA
"""
@tags: 系统操作
@homepage: https://napcat.apifox.cn/226658975e0
@llms.txt: https://napcat.apifox.cn/226658975e0.md
@last_update: 2025-04-27 00:53:40

@description: 

summary:获取机器人账号范围

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.43"
__endpoint__ = "get_robot_uin_range"
__id__ = "226658975e0"
__method__ = "POST"

# endregion METADATA


# region code
import logging
from pydantic import BaseModel, Field
from typing import Literal # Literal is not deprecated

logger = logging.getLogger(__name__)

# region req
class GetRobotUinRangeReq(BaseModel):
    """
    请求：获取机器人账号范围
    """

    pass # Request body is empty
# endregion req



# region res

class UinRangeItem(BaseModel):
    """
    数据项：账号范围
    """
    minUin: str = Field(..., description="最小UIN")
    maxUin: str = Field(..., description="最大UIN")

class GetRobotUinRangeRes(BaseModel):
    """
    响应：获取机器人账号范围
    """
    # 定义响应参数
    status: Literal["ok"] = Field(..., description="状态码，固定为 'ok'")
    retcode: int = Field(..., description="返回码")
    data: list[UinRangeItem] = Field(..., description="机器人账号范围列表")
    message: str = Field(..., description="信息")
    wording: str = Field(..., description="词语")
    echo: str | None = Field(None, description="回显信息")
# endregion res

# region api
class GetRobotUinRangeAPI(BaseModel):
    """get_robot_uin_range接口数据模型"""
    endpoint: str = "get_robot_uin_range"
    method: str = "POST"
    Req: type[BaseModel] = GetRobotUinRangeReq
    Res: type[BaseModel] = GetRobotUinRangeRes
# endregion api




# endregion code
