# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: 账号相关
@homepage: https://napcat.apifox.cn/226659210e0
@llms.txt: https://napcat.apifox.cn/226659210e0.md
@last_update: 2025-04-26 01:17:45

@description: 

summary:获取收藏表情

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "fetch_custom_face"
__id__ = "226659210e0"
__method__ = "POST"

# endregion METADATA


# region code

from pydantic import BaseModel, Field
from typing import Literal

# region req
class FetchCustomFaceReq(BaseModel):
    """
    {{DESC_EndPointReq}}
    """

    count: int = Field(..., description="数量，默认为40")
# endregion req



# region res
class FetchCustomFaceRes(BaseModel):
    # 定义响应参数
    # 例如：
    # param1: str = Field(..., description="参数1的描述")
    # param2: int = Field(..., description="参数2的描述")
    
    status: Literal["ok"] = Field(
        ..., description="状态，永远为'ok'"
    )  # type: ignore
    retcode: int = Field(..., description="返回码")
    data: list[str] = Field(..., description="表情ID列表")
    message: str = Field(..., description="消息")
    wording: str = Field(..., description="额外消息")
    echo: str | None = Field(None, description="echo")

# endregion res

# region api
class FetchCustomFaceAPI(BaseModel):
    """fetch_custom_face接口数据模型"""
    endpoint: str = "fetch_custom_face"
    method: str = "POST"
    Req: type[BaseModel] = FetchCustomFaceReq
    Res: type[BaseModel] = FetchCustomFaceRes
# endregion api




# endregion code