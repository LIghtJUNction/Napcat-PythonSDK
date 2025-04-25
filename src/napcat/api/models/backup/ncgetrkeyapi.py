# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: 密钥相关
@homepage: https://napcat.apifox.cn/226659297e0
@llms.txt: https://napcat.apifox.cn/226659297e0.md
@last_update: 2025-04-26 01:17:45

@description: 

summary:nc获取rkey

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "nc_get_rkey"
__id__ = "226659297e0"
__method__ = "POST"

# endregion METADATA


# region code
from pydantic import BaseModel, Field


# region req
class NcGetRkeyReq(BaseModel):
    """
    nc获取rkey 请求模型
    "

    # 请求体为空，使用 pass
    pass
# endregion req



# region res
class RkeyItem(BaseModel):
    """
    rkey 数据项模型
    "
    rkey: str = Field(..., description="rkey")
    ttl: str = Field(..., description="ttl")
    time: float = Field(..., description="时间戳") # Spec says number, which usually maps to float or int
    type: int = Field(..., description="类型") # Spec says number


class NcGetRkeyRes(BaseModel):
    """
    nc获取rkey 响应模型
    "
    # 定义响应参数
    status: str = Field(
        ..., description="状态码", const="ok"
    )  # Use Field(..., const="ok") for fixed value
    retcode: int = Field(..., description="返回码") # Spec says number
    data: list[RkeyItem] = Field(..., description="rkey列表") # Data is an array of RkeyItem objects
    message: str = Field(..., description="消息")
    wording: str = Field(..., description="描述")
    echo: str | None = Field(None, description="echo") # Nullable field
# endregion res

# region api
class NcGetRkeyAPI(BaseModel):
    """nc_get_rkey接口数据模型"""
    endpoint: str = "nc_get_rkey"
    method: str = "POST"
    Req: type[BaseModel] = NcGetRkeyReq
    Res: type[BaseModel] = NcGetRkeyRes
# endregion api

# endregion code
