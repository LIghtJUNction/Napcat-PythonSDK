# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: 群聊相关
@homepage: https://napcat.apifox.cn/226658674e0
@llms.txt: https://napcat.apifox.cn/226658674e0.md
@last_update: 2025-04-26 01:17:44

@description: 

summary:设置群精华消息

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "set_essence_msg"
__id__ = "226658674e0"
__method__ = "POST"

# endregion METADATA


# region code
from pydantic import BaseModel, Field

# region req
class SetEssenceMsgReq(BaseModel):
    """
    设置群精华消息 请求参数
    """
    message_id: int | str = Field(..., description="消息ID")
# endregion req



# region res
class SetEssenceMsgRes(BaseModel):
    """
    设置群精华消息 响应参数
    """
    status: str = Field(..., description="状态, 总是 'ok'")
    retcode: int = Field(..., description="返回码")
    data: dict = Field(..., description="响应数据, 空对象") # Based on schema, ignoring example
    message: str = Field(..., description="信息")
    wording: str = Field(..., description="文字")
    echo: str | None = Field(None, description="回显数据")
# endregion res

# region api
class SetEssenceMsgAPI(BaseModel):
    """set_essence_msg接口数据模型"""
    endpoint: str = "set_essence_msg"
    method: str = "POST"
    Req: type[BaseModel] = SetEssenceMsgReq
    Res: type[BaseModel] = SetEssenceMsgRes
# endregion api




# endregion code
