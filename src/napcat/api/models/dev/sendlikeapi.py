# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: ['账号相关']
@homepage: https://napcat.apifox.cn/226656717e0
@llms.txt: https://napcat.apifox.cn/226656717e0.md
@last_update: 2025-04-27 00:53:40

@description: 

summary:点赞

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.43"
__endpoint__ = "send_like"
__id__ = "226656717e0"
__method__ = "POST"

# endregion METADATA


# region code
import logging
from typing import Literal
from pydantic import BaseModel, Field

logger = logging.getLogger(__name__)

# region req
class SendLikeReq(BaseModel):
    """
    点赞请求模型
    """
    user_id: int | str = Field(..., description="用户ID")
    times: int = Field(default=1, description="点赞次数")

# endregion req



# region res
class SendLikeRes(BaseModel):
    """
    点赞响应模型
    """
    status: Literal["ok"] = Field(..., description="状态")
    retcode: int = Field(..., description="返回码")
    # 'data' is explicitly defined as 'null' in the response override
    data: None = Field(..., description="数据")
    message: str = Field(..., description="消息")
    wording: str = Field(..., description="文案")
    echo: str | None = Field(..., description="回显信息")

# endregion res

# region api
class SendLikeAPI(BaseModel):
    """send_like接口数据模型"""
    endpoint: str = "send_like"
    method: str = "POST"
    Req: type[BaseModel] = SendLikeReq
    Res: type[BaseModel] = SendLikeRes
# endregion api




# endregion code
