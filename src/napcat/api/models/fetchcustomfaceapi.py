# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: 账号相关
@homepage: https://napcat.apifox.cn/226659210e0
@llms.txt: https://napcat.apifox.cn/226659210e0.md
@last_update: 2025-04-27 00:53:40

@description: 

summary:获取收藏表情

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.43"
__endpoint__ = "fetch_custom_face"
__id__ = "226659210e0"
__method__ = "POST"

# endregion METADATA


# region code
import logging
from pydantic import BaseModel, Field
from typing import Literal

logger = logging.getLogger(__name__)

# region req
class FetchCustomFaceReq(BaseModel):
    """
    获取收藏表情 请求参数
    """
    count: int = Field(default=48, description="获取数量")
# endregion req



# region res
class FetchCustomFaceRes(BaseModel):
    """
    获取收藏表情 响应参数
    """
    status: Literal["ok"] = Field("ok", description="状态码，固定为 'ok'")
    retcode: int = Field(description="响应码")
    data: list[str] = Field(description="收藏表情列表，每个元素是一个表情的唯一标识符")
    message: str = Field(description="错误信息")
    wording: str = Field(description="错误信息（中文）")
    echo: str | None = Field(default=None, description="echo")
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