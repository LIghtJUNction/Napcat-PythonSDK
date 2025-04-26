# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: 群聊相关
@homepage: https://napcat.apifox.cn/226658674e0
@llms.txt: https://napcat.apifox.cn/226658674e0.md
@last_update: 2025-04-27 00:53:40

@description: 设置群精华消息

summary:设置群精华消息

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.43"
__endpoint__ = "set_essence_msg"
__id__ = "226658674e0"
__method__ = "POST"

# endregion METADATA


# region code
import logging
from pydantic import BaseModel, Field
from typing import Literal

logger = logging.getLogger(__name__)

# region req
class SetEssenceMsgReq(BaseModel):
    """
    设置群精华消息请求体
    """

    message_id: int | str = Field(..., description="消息id")

# endregion req



# region res
class SetEssenceMsgResMsg(BaseModel):
    """
    精华消息内容 (根据Schema, 此处为空对象)
    """
    # Although the example shows fields, the schema defines this as an empty object.
    pass

class SetEssenceMsgResResult(BaseModel):
    """
    精华消息结果详情
    """
    wording: str = Field(..., description="正常为空，异常有文本提示")
    digestUin: str = Field(..., description="处理精华消息的QQ号")
    digestTime: int = Field(..., description="处理精华消息的时间戳")
    msg: SetEssenceMsgResMsg = Field(..., description="精华消息内容")
    errorCode: int = Field(..., description="错误码，0表示成功")

class SetEssenceMsgResData(BaseModel):
    """
    设置群精华消息响应数据
    """
    errCode: str = Field(..., description="内部错误码")
    errMsg: str = Field(..., description="内部错误信息")
    result: SetEssenceMsgResResult = Field(..., description="精华消息结果")

class SetEssenceMsgRes(BaseModel):
    """
    设置群精华消息响应体
    """
    # 定义响应参数
    status: Literal["ok"] = Field(..., description="响应状态")
    retcode: int = Field(..., description="响应码")
    data: SetEssenceMsgResData = Field(..., description="响应数据")
    message: str = Field(..., description="响应消息")
    wording: str = Field(..., description="响应提示")
    echo: str | None = Field(None, description="echo")

# endregion res

# region api
class SetEssenceMsgAPI(BaseModel):
    """set_essence_msg接口数据模型"""
    endpoint: str = "set_essence_msg"
    method: str = "POST"
    Req: type = SetEssenceMsgReq
    Res: type = SetEssenceMsgRes

# endregion api




# endregion code
