# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: 群聊相关
@homepage: https://napcat.apifox.cn/226658678e0
@llms.txt: https://napcat.apifox.cn/226658678e0.md
@last_update: 2025-04-26 01:17:44

@description: 

summary:删除群精华消息

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "delete_essence_msg"
__id__ = "226658678e0"
__method__ = "POST"

# endregion METADATA


# region code
import logging
from pydantic import BaseModel, Field, Literal

logger = logging.getLogger(__name__)

# region req
class DeleteEssenceMsgReq(BaseModel): # type: ignore
    """
    请求体模型
    """

    message_id: int | str = Field(
        ...,
        description="消息ID (可以是数字或字符串)"
    )
# endregion req



# region res
class DeleteEssenceMsgResData(BaseModel): # type: ignore
    """
    响应数据字段 (根据schema, data是一个空对象)
    """
    # Note: The schema defines 'data' as an object with no specific properties.
    # If the actual API returns more, this model would need to be updated.
    pass # Schema indicates empty properties


class DeleteEssenceMsgRes(BaseModel): # type: ignore
    """
    响应体模型
    """
    status: Literal["ok"] = Field(
        "ok",
        description="状态"
    )
    retcode: int = Field(
        ...,
        description="返回码"
    )
    data: dict = Field(
        default_factory=dict,
        description="响应数据"
    )
    message: str = Field(
        ...,
        description="消息"
    )
    wording: str = Field(
        ...,
        description="提示"
    )
    echo: str | None = Field(
        None,
        description="回显"
    )
# endregion res

# region api
class DeleteEssenceMsgAPI(BaseModel):
    """delete_essence_msg接口数据模型"""
    endpoint: str = "delete_essence_msg"
    method: str = "POST"
    Req: type[BaseModel] = DeleteEssenceMsgReq
    Res: type[BaseModel] = DeleteEssenceMsgRes
# endregion api




# endregion code
