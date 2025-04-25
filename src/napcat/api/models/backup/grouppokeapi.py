# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: ['消息相关/发送群聊消息']
@homepage: https://napcat.apifox.cn/226659265e0
@llms.txt: https://napcat.apifox.cn/226659265e0.md
@last_update: 2025-04-26 01:17:45

@description:

summary:发送群聊戳一戳

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "group_poke"
__id__ = "226659265e0"
__method__ = "POST"

# endregion METADATA


# region code
import logging
from pydantic import BaseModel, Field

logger = logging.getLogger(__name__)

# region req
class GroupPokeReq(BaseModel):
    """
    请求体模型
    """
    group_id: int | str = Field(..., description="群号")
    user_id: int | str = Field(..., description="被戳用户的QQ号")
# endregion req



# region res
class GroupPokeRes(BaseModel):
    """
    响应体模型
    """
    status: str = Field(
        ..., description="\nstatus: ok 为成功", const=True, json_schema_extra={'const': 'ok'}
    )
    retcode: int = Field(..., description="状态码")
    message: str = Field(..., description="状态信息")
    wording: str = Field(..., description="状态描述")
    echo: str | None = Field(None, description="echo回显")
# endregion res

# region api
class GroupPokeAPI(BaseModel):
    """group_poke接口数据模型"""

    endpoint: str = "group_poke"
    method: str = "POST"
    Req: type[BaseModel] = GroupPokeReq
    Res: type[BaseModel] = GroupPokeRes
# endregion api




# endregion code
