# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: [
    "\u8d26\u53f7\u76f8\u5173"
]
@homepage: https://napcat.apifox.cn/226657083e0
@llms.txt: https://napcat.apifox.cn/226657083e0.md
@last_update: 2025-04-27 00:53:40

@description: 

summary:\u83b7\u53d6\u72b6\u6001

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.43"
__endpoint__ = "get_status"
__id__ = "226657083e0"
__method__ = "POST"

# endregion METADATA


# region code
from typing import Literal
from pydantic import BaseModel, Field

# region req
class GetStatusReq(BaseModel):
    """
    \u83b7\u53d6\u72b6\u6001\u8bf7\u6c42\u6a21\u578b
    """

    # Request body is empty according to OpenAPI spec
    pass
# endregion req



# region res
class GetStatusResDataStat(BaseModel):
    """
    \u72b6\u6001\u8be6\u60c5\u6570\u636e\u6a21\u578b
    """

    # According to OpenAPI spec, stat is an empty object
    pass


class GetStatusResData(BaseModel):
    """
    \u72b6\u6001\u54cd\u5e94\u6570\u636e\u6a21\u578b
    """

    online: bool = Field(..., description="\u662f\u5426\u5728\u7ebf")
    good: bool = Field(..., description="\u662f\u5426\u72b6\u6001\u826f\u597d")
    stat: GetStatusResDataStat = Field(..., description="\u72b6\u6001\u8be6\u60c5")


class GetStatusRes(BaseModel):
    """
    \u83b7\u53d6\u72b6\u6001\u54cd\u5e94\u6a21\u578b
    """

    status: Literal["ok"] = Field(
        "ok", description="\u54cd\u5e94\u72b6\u6001\uff0c\u56fa\u5b9a\u4e3a 'ok'"
    )
    retcode: int = Field(..., description="\u8fd4\u56de\u7801")
    data: GetStatusResData = Field(..., description="\u5177\u4f53\u7684\u72b6\u6001\u6570\u636e")
    message: str = Field(..., description="\u54cd\u5e94\u6d88\u606f")
    wording: str = Field(..., description="\u54cd\u5e94\u63cf\u8ff0")
    echo: str | None = Field(None, description="\u56de\u663e\u5b57\u7b26\u4e32, \u53ef\u80fd\u4e3anull")
# endregion res

# region api
class GetStatusAPI(BaseModel):
    """get_status\u63a5\u53e3\u6570\u636e\u6a21\u578b"""
    endpoint: str = "get_status"
    method: str = "POST"
    Req: type[BaseModel] = GetStatusReq
    Res: type[BaseModel] = GetStatusRes
# endregion api

# endregion code