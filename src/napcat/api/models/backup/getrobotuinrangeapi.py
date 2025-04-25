# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: 系统操作
@homepage: https://napcat.apifox.cn/226658975e0
@llms.txt: https://napcat.apifox.cn/226658975e0.md
@last_update: 2025-04-26 01:17:44

@description: 

summary:获取机器人账号范围

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "get_robot_uin_range"
__id__ = "226658975e0"
__method__ = "POST"

# endregion METADATA


# region code
import logging
from pydantic import BaseModel, Field

logger = logging.getLogger(__name__)

# region req
class GetRobotUinRangeReq(BaseModel):
    """
    {{DESC_EndPointReq}}
    """

    pass
# endregion req



# region res

class UinRangeItem(BaseModel):
    """机器人账号范围项"""
    min_uin: str = Field(..., alias='minUin', description="起始账号UIN")
    max_uin: str = Field(..., alias='maxUin', description="结束账号UIN")

class GetRobotUinRangeRes(BaseModel):
    """{{DESC_EndPointRes}}"""
    # 定义响应参数
    status: str = Field(..., description="状态")
    retcode: int = Field(..., description="返回码")
    data: list[UinRangeItem] = Field(..., description="账号范围列表")
    message: str = Field(..., description="消息")
    wording: str = Field(..., description="提示")
    echo: str | None = Field(None, description="Echo字段")

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
