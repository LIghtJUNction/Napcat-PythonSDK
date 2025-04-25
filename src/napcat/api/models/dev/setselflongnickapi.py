# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: 账号相关
@homepage: https://napcat.apifox.cn/226659186e0
@llms.txt: https://napcat.apifox.cn/226659186e0.md
@last_update: 2025-04-26 01:17:44

@description: 

summary:设置个性签名

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "set_self_longnick"
__id__ = "226659186e0"
__method__ = "POST"

# endregion METADATA


# region code
import logging
from pydantic import BaseModel, Field
from typing import Literal # Import Literal for const status

logger = logging.getLogger(__name__)

# region req
class SetSelfLongnickReq(BaseModel):
    """
    请求模型: 设置个性签名
    """

    longNick: str = Field(..., description="个性签名内容")

# endregion req



# region res
class SetSelfLongnickRes(BaseModel):
    """
    响应模型: 设置个性签名
    """

    class SetSelfLongnickResData(BaseModel):
        """
        响应数据字段
        """
        result: int = Field(..., description="操作结果代码，0表示成功")
        errMsg: str = Field(..., description="错误消息")

    status: Literal['ok'] = Field('ok', description="响应状态")
    retcode: int = Field(..., description="响应码")
    data: SetSelfLongnickResData = Field(..., description="响应数据")
    message: str = Field(..., description="响应消息")
    wording: str = Field(..., description="响应提示")
    echo: str | None = Field(None, description="echo")

# endregion res

# region api
class SetSelfLongnickAPI(BaseModel):
    """set_self_longnick接口数据模型"""
    endpoint: str = "set_self_longnick"
    method: str = "POST"
    Req: type[BaseModel] = SetSelfLongnickReq
    Res: type[BaseModel] = SetSelfLongnickRes
# endregion api




# endregion code
