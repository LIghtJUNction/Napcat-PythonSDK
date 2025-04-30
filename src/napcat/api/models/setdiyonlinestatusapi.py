# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: 账号相关
@homepage: https://napcat.apifox.cn/266151905e0
@llms.txt: https://napcat.apifox.cn/266151905e0.md
@last_update: 2025-04-27 00:53:41

@description: 

summary:设置自定义在线状态

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.43"
__endpoint__ = "set_diy_online_status"
__id__ = "266151905e0"
__method__ = "POST"

# endregion METADATA


# region code
import logging
from pydantic import BaseModel, Field
from typing import Literal

logger = logging.getLogger(__name__)

# region req
class SetDiyOnlineStatusReq(BaseModel):
    """
    设置自定义在线状态请求模型
    """

    face_id: int | str = Field(..., description="表情ID")
    face_type: int | str | None = Field(None, description="表情ID") # Based on example and type ref, seems identical to face_id, but optional
    wording: str | None = Field(None, description="描述文本") # Based on example, not explicitly required

# endregion req



# region res
class SetDiyOnlineStatusRes(BaseModel):
    """
    设置自定义在线状态响应模型
    """

    status: Literal["ok"] = Field("ok", description="状态码，固定为 'ok'")
    retcode: int = Field(..., description="返回码")
    data: str = Field(..., description="数据内容 (字符串类型)")
    message: str = Field(..., description="消息")
    wording: str = Field(..., description="词语")
    echo: str | None = Field(None, description="回显数据") # Corrected default value to None

# endregion res

# region api
class SetDiyOnlineStatusAPI(BaseModel):
    """set_diy_online_status接口数据模型"""
    endpoint: str = "set_diy_online_status"
    method: str = "POST"
    Req: type[BaseModel] = SetDiyOnlineStatusReq
    Res: type[BaseModel] = SetDiyOnlineStatusRes
# endregion api




# endregion code
