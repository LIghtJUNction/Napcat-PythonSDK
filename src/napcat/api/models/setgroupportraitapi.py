# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: 群聊相关
@homepage: https://napcat.apifox.cn/226658669e0
@llms.txt: https://napcat.apifox.cn/226658669e0.md
@last_update: 2025-04-27 00:53:40

@description: 

summary:设置群头像

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.43"
__endpoint__ = "set_group_portrait"
__id__ = "226658669e0"
__method__ = "POST"

# endregion METADATA


# region code
import logging
from typing import Literal
from pydantic import BaseModel, Field

logger = logging.getLogger(__name__)

# region req
class SetGroupPortraitReq(BaseModel):
    """
    设置群头像请求模型
    """

    group_id: int | str = Field(..., description="群号")
    file: str = Field(..., description="图片文件路径或网络URL (支持 file:// 和 http(s)://)")

# endregion req



# region res
class SetGroupPortraitRes(BaseModel):
    """
    设置群头像响应模型
    """
    class SetGroupPortraitResData(BaseModel):
        """
        设置群头像响应数据详情
        """
        result: str = Field(..., description="操作结果代码") # Based on example 0 (string in schema), success likely 0
        errMsg: str = Field(..., description="错误信息")

    # 定义响应参数
    status: Literal["ok"] = Field("ok", description="状态码，固定为 'ok'")
    retcode: int = Field(..., description="返回码") # Based on example 0
    data: SetGroupPortraitResData = Field(..., description="响应数据")
    message: str = Field(..., description="消息")
    wording: str = Field(..., description="额外说明")
    echo: str | None = Field(None, description="Echo数据")

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