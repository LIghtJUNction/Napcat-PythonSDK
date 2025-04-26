# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: 账号相关
@homepage: https://napcat.apifox.cn/226659178e0
@llms.txt: https://napcat.apifox.cn/226659178e0.md
@last_update: 2025-04-27 00:53:40

@description: 

summary:创建收藏

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.43"
__endpoint__ = "create_collection"
__id__ = "226659178e0"
__method__ = "POST"

# endregion METADATA


# region code
import logging
from typing import Literal
from pydantic import BaseModel, Field

logger = logging.getLogger(__name__)

# region req
class CreateCollectionReq(BaseModel):
    """
    创建收藏请求模型
    """
    rawData: str = Field(..., description="内容")
    brief: str = Field(..., description="标题")
# endregion req



# region res
class CreateCollectionRes(BaseModel):
    """
    创建收藏响应模型
    """
    class Data(BaseModel):
        """
        响应数据字段
        """
        result: int = Field(..., description="结果码")
        errMsg: str = Field(..., description="错误信息")

    status: Literal["ok"] = Field(..., description="状态码")
    retcode: int = Field(..., description="返回码")
    data: Data = Field(..., description="响应数据")
    message: str = Field(..., description="消息")
    wording: str = Field(..., description="措辞")
    echo: str | None = Field(..., description="echo")
# endregion res

# region api
class CreateCollectionAPI(BaseModel):
    """create_collection接口数据模型"""
    endpoint: str = "create_collection"
    method: str = "POST"
    Req: type[BaseModel] = CreateCollectionReq
    Res: type[BaseModel] = CreateCollectionRes
# endregion api




# endregion code
