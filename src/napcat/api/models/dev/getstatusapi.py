# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: 账号相关
@homepage: https://napcat.apifox.cn/226657083e0
@llms.txt: https://napcat.apifox.cn/226657083e0.md
@last_update: 2025-04-26 01:17:44

@description: 

summary:获取状态

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "get_status"
__id__ = "226657083e0"
__method__ = "POST"

# endregion METADATA


# region code
import logging
from pydantic import BaseModel, Field

logger = logging.getLogger(__name__)

# region req
class GetStatusReq(BaseModel):
    """
    {{DESC_EndPointReq}}
    
    获取状态的请求模型，没有特定的请求参数。
    """
    pass
# endregion req



# region res
class GetStatusRes(BaseModel):
    """
    获取状态的响应模型
    """

    class Data(BaseModel):
        """
        响应数据详情
        """

        class Stat(BaseModel):
            """
            机器人统计信息
            
            目前为空对象。
            """
            pass

        online: bool = Field(..., description="机器人是否在线")
        good: bool = Field(..., description="机器人状态是否良好")
        stat: Stat = Field(..., description="机器人统计信息")

    status: str = Field(..., description="响应状态，固定为 'ok'", const='ok')
    retcode: float = Field(..., description="状态码") # OpenAPI spec uses number, float is common in python
    data: Data = Field(..., description="响应数据")
    message: str = Field(..., description="消息")
    wording: str = Field(..., description="提示语")
    echo: str | None = Field(None, description="可选的 echo 字符串")



# endregion res

# region api
class GetStatusAPI(BaseModel):
    """get_status接口数据模型"""
    endpoint: str = "get_status"
    method: str = "POST"
    Req: type[BaseModel] = GetStatusReq
    Res: type[BaseModel] = GetStatusRes
# endregion api




# endregion code
