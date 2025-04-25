# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: ['群聊相关']
@homepage: https://napcat.apifox.cn/226656931e0
@llms.txt: https://napcat.apifox.cn/226656931e0.md
@last_update: 2025-04-26 01:17:44

@description: 

summary:设置群头衔

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "set_group_special_title"
__id__ = "226656931e0"
__method__ = "POST"

# endregion METADATA


# region code
import logging
from pydantic import BaseModel, Field
from typing import Literal # Use Literal for constant values

logger = logging.getLogger(__name__)

# region req
class SetGroupSpecialTitleReq(BaseModel):
    """
    设置群头衔请求模型
    """

    group_id: int | str = Field(
        ..., description="群号"
    )
    user_id: int | str = Field(
        ..., description="用户号"
    )
    special_title: str = Field(
        ..., description="头衔，空字符串即为解除"
    )
# endregion req



# region res
class SetGroupSpecialTitleRes(BaseModel):
    """
    设置群头衔响应模型
    """

    status: Literal["ok"] = Field("ok", description="状态: 'ok'")
    retcode: int = Field(..., description="返回码")
    data: None = Field(None, description="固定为 null") # According to OpenAPI spec override
    message: str = Field(..., description="消息")
    wording: str = Field(..., description="提示信息")
    echo: str | None = Field(None, description="Echo信息，可能为 null")
# endregion res

# region api
class SetGroupSpecialTitleAPI(BaseModel):
    """set_group_special_title接口数据模型"""
    endpoint: str = "set_group_special_title"
    method: str = "POST"
    Req: type[BaseModel] = SetGroupSpecialTitleReq
    Res: type[BaseModel] = SetGroupSpecialTitleRes
# endregion api




# endregion code
