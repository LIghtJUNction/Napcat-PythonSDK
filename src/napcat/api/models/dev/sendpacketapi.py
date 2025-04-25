# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: 系统操作
@homepage: https://napcat.apifox.cn/250286903e0
@llms.txt: https://napcat.apifox.cn/250286903e0.md
@last_update: 2025-04-26 01:17:45

@description: 

summary:发送自定义组包

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "send_packet"
__id__ = "250286903e0"
__method__ = "POST"

# endregion METADATA


# region code
import logging
from pydantic import BaseModel, Field

logger = logging.getLogger(__name__)

# region req
class SendPacketReq(BaseModel):
    """
    发送自定义组包 请求模型
    
    根据API文档，请求体为空对象。
    """
    # API文档定义请求体为 `{}`，因此模型为空。
    pass
# endregion req



# region res
class SendPacketRes(BaseModel):
    """
    发送自定义组包 响应模型
    
    根据API文档，响应体为空对象。
    """
    # API文档定义响应体为 `{}`，因此模型为空。
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
