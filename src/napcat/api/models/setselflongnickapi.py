# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: 
@homepage: https://napcat.apifox.cn/226659186e0
@llms.txt: https://napcat.apifox.cn/226659186e0.md
@last_update: 2025-04-27 00:53:40

@description: 

summary:设置个性签名

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.43"
__endpoint__ = "set_self_longnick"
__id__ = "226659186e0"
__method__ = "POST"

# endregion METADATA


# region code
from typing import Literal 
from pydantic import BaseModel, Field

# region req
class SetSelfLongnickReq(BaseModel):
    """
    设置个性签名请求模型
    """

    longNick: str = Field(..., description="个性签名内容")

# endregion req



# region res
class SetSelfLongnickRes(BaseModel):
    """
    设置个性签名响应模型
    """

    class Data(BaseModel):
        """
        响应数据详情
        """
        result: int = Field(..., description="结果") 
        errMsg: str = Field(..., description="错误信息")

    status: Literal["ok"] = Field("ok", description="状态码，固定为 'ok'") 
    retcode: int = Field(..., description="返回码") 
    data: Data = Field(..., description="响应数据")
    message: str = Field(..., description="消息")
    wording: str = Field(..., description="说明")
    echo: str | None = Field(None, description="Echo")

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