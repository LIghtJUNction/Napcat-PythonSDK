# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: 群聊相关
@homepage: https://napcat.apifox.cn/226658669e0
@llms.txt: https://napcat.apifox.cn/226658669e0.md
@last_update: 2025-04-26 01:17:44

@description: 

summary:设置群头像

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "set_group_portrait"
__id__ = "226658669e0"
__method__ = "POST"

# endregion METADATA


# region code
import logging
from pydantic import BaseModel, Field

logger = logging.getLogger(__name__)

# region req
class SetGroupPortraitReq(BaseModel):
    """
    设置群头像请求模型
    """

    group_id: str | int = Field(
        ..., description="群号"
    )
    file: str = Field(
        ..., description="头像文件，可以是网络路径（http/https）、本地路径（file://）"
    )
# endregion req



# region res
class SetGroupPortraitResData(BaseModel):
    """
    设置群头像响应数据模型
    """

    result: str = Field(..., description="结果") # Note: OpenAPI shows string, example shows 0
    errMsg: str = Field(..., description="错误信息") # Note: OpenAPI shows string, example shows success


class SetGroupPortraitRes(BaseModel):
    """
    设置群头像响应模型
    """

    status: str = Field(
        ..., description="响应状态", const="ok"
    )
    retcode: int = Field(
        ..., description="响应码"
    )
    data: SetGroupPortraitResData = Field(
        ..., description="响应数据"
    )
    message: str = Field(
        ..., description="消息"
    )
    wording: str = Field(
        ..., description="提示词"
    )
    echo: str | None = Field(
        None, description="echo"
    )
# endregion res

# region api
class SetGroupPortraitAPI(BaseModel):
    """set_group_portrait接口数据模型"""
    endpoint: str = "set_group_portrait"
    method: str = "POST"
    Req: type[BaseModel] = SetGroupPortraitReq
    Res: type[BaseModel] = SetGroupPortraitRes
# endregion api




# endregion code
