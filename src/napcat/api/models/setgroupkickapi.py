# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/226656748e0
@llms.txt: https://napcat.apifox.cn/226656748e0.md
@last_update: 2025-04-26 01:17:44

@description: 

summary:群踢人

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "set_group_kick"
__id__ = "226656748e0"
__method__ = "POST"

# endregion METADATA


# region code
import logging
from pydantic import BaseModel, Field
from typing import Literal # Import Literal for status constant

logger = logging.getLogger(__name__)

# region req
class SetGroupKickReq(BaseModel):
    """
    请求踢出群成员
    """

    group_id: int | str = Field(..., description="群号") # group_id can be number or string
    user_id: int | str = Field(..., description="要踢出的 QQ 号") # user_id can be number or string
    reject_add_request: bool = Field(..., description="是否禁止该成员在被踢出后通过其他方式再次加入，默认为 false")
# endregion req



# region res
class SetGroupKickRes(BaseModel):
    """
    踢出群成员响应
    """
    status: Literal["ok"] = Field(..., description="响应状态")
    retcode: int = Field(..., description="响应码")
    data: None = Field(..., description="响应数据")
    message: str = Field(..., description="错误信息")
    wording: str = Field(..., description="错误描述")
    echo: str | None = Field(None, description="echo") # echo can be null

# endregion res

# region api
class SetGroupKickAPI(BaseModel):
    """set_group_kick接口数据模型"""
    endpoint: str = "set_group_kick"
    method: str = "POST"
    Req: type[BaseModel] = SetGroupKickReq
    Res: type[BaseModel] = SetGroupKickRes
# endregion api




# endregion code
