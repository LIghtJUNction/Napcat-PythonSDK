# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: [
  "个人操作"
]
@homepage: https://napcat.apifox.cn/226657080e0
@llms.txt: https://napcat.apifox.cn/226657080e0.md
@last_update: 2025-04-26 01:17:44

@description:

summary:检查是否可以发送语音

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "can_send_record"
__id__ = "226657080e0"
__method__ = "POST"

# endregion METADATA


# region code
import logging
from pydantic import BaseModel, Field

logger = logging.getLogger(__name__)

# region req
class CanSendRecordReq(BaseModel):
    """
    检查是否可以发送语音
    """
    pass
# endregion req



# region res
class CanSendRecordRes(BaseModel):
    """
    检查是否可以发送语音 响应
    """

    class CanSendRecordData(BaseModel):
        """
        响应数据
        """
        yes: bool = Field(..., description="是否可以发送语音")

    status: str = Field("ok", description="状态")
    retcode: int = Field(..., description="返回码")
    data: CanSendRecordData = Field(..., description="响应数据")
    message: str = Field(..., description="消息")
    wording: str = Field(..., description="提示")
    echo: str | None = Field(None, description="Echo")
# endregion res

# region api
class CanSendRecordAPI(BaseModel):
    """can_send_record接口数据模型"""
    endpoint: str = "can_send_record"
    method: str = "POST"
    Req: type[BaseModel] = CanSendRecordReq
    Res: type[BaseModel] = CanSendRecordRes
# endregion api




# endregion code
