# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: 账号相关
@homepage: https://napcat.apifox.cn/226659178e0
@llms.txt: https://napcat.apifox.cn/226659178e0.md
@last_update: 2025-04-26 01:17:44

@description: 创建收藏

summary:创建收藏

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "create_collection"
__id__ = "226659178e0"
__method__ = "POST"

# endregion METADATA


# region code
from pydantic import BaseModel, Field, AliasChoices
from typing import Literal

# region req
class CreateCollectionReq(BaseModel):
    """
    请求模型
    """

    # 使用 AliasChoices 允许同时接受 raw_data 和 rawData
    rawData: str = Field(
        ...,
        description="内容",
        validation_alias=AliasChoices('raw_data', 'rawData')
    )
    # 使用 AliasChoices 允许同时接受 brief 和 brief
    brief: str = Field(
        ...,
        description="标题",
        validation_alias=AliasChoices('brief')
    )

# endregion req



# region res
class CreateCollectionResData(BaseModel):
    """
    响应数据模型
    """
    result: float = Field(..., description="结果")
    err_msg: str = Field(
        ...,
        description="错误信息",
        validation_alias=AliasChoices('err_msg', 'errMsg')
    )

class CreateCollectionRes(BaseModel):
    """
    响应模型
    """
    status: Literal["ok"] = Field(..., description="状态")
    retcode: float = Field(..., description="返回码")
    data: CreateCollectionResData = Field(..., description="响应数据")
    message: str = Field(..., description="消息")
    wording: str = Field(..., description="词语")
    echo: str | None = Field(..., description="回显")


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
