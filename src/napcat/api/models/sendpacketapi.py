# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: 系统操作
@homepage: https://napcat.apifox.cn/250286903e0
@llms.txt: https://napcat.apifox.cn/250286903e0.md
@last_update: 2025-04-27 00:53:41

@description: 

summary:发送自定义组包

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.43"
__endpoint__ = "send_packet"
__id__ = "250286903e0"
__method__ = "POST"

# endregion METADATA


# region code
import logging
from pydantic import BaseModel

logger = logging.getLogger(__name__)

# region req
class SendPacketReq(BaseModel):
    """
    请求参数：发送自定义组包
    （OpenAPI spec indicates an empty object request body）
    """
    pass
# endregion req



# region res
class SendPacketRes(BaseModel):
    """
    响应参数：发送自定义组包
    （OpenAPI spec indicates an empty object response body）
    """
    pass
# endregion res

# region api
class SendPacketAPI(BaseModel):
    """send_packet接口数据模型"""
    endpoint: str = "send_packet"
    method: str = "POST"
    Req: type[BaseModel] = SendPacketReq
    Res: type[BaseModel] = SendPacketRes
# endregion api




# endregion code