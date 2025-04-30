# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: ["其他/接口"]
@homepage: https://napcat.apifox.cn/226658925e0
@llms.txt: https://napcat.apifox.cn/226658925e0.md
@last_update: 2025-04-27 00:53:40

@description: 

summary:unknown

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.43"
__endpoint__ = "unknown"
__id__ = "226658925e0"
__method__ = "POST"

# endregion METADATA


# region code
from pydantic import BaseModel

# region req
class UnknownReq(BaseModel):
    """
    请求模型，无请求体参数。
    """
    pass
# endregion req



# region res
class UnknownRes(BaseModel):
    """
    响应模型，无响应参数。
    """
    pass
# endregion res

# region api
class UnknownAPI(BaseModel):
    """unknown接口数据模型"""
    endpoint: str = "unknown"
    method: str = "POST"
    Req: type[BaseModel] = UnknownReq
    Res: type[BaseModel] = UnknownRes
# endregion api




# endregion code