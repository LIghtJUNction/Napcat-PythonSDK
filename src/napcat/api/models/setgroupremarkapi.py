# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: 
@homepage: https://napcat.apifox.cn/283136268e0
@llms.txt: https://napcat.apifox.cn/283136268e0.md
@last_update: 2025-04-27 00:53:41

@description: 

summary:设置群备注

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.43"
__endpoint__ = "set_group_remark"
__id__ = "283136268e0"
__method__ = "POST"

# endregion METADATA


# region code
import logging
from pydantic import BaseModel, Field
from typing import Literal

logger = logging.getLogger(__name__)

# region req
class SetGroupRemarkReq(BaseModel):
    """
    设置群备注请求参数
    """
    group_id: str = Field(..., description="群号")
    remark: str = Field(..., description="群备注")
# endregion req



# region res
class SetGroupRemarkRes(BaseModel):
    """
    设置群备注响应参数
    """
    status: Literal["ok"] = Field("ok", description="状态码，固定为 'ok'")
    retcode: int = Field(..., description="状态码")
    data: None = Field(..., description="响应数据体，固定为null")
    message: str = Field(..., description="错误信息")
    wording: str = Field(..., description="错误信息")
    echo: str | None = Field(default=None, description="Echo回传，如果请求时指定了echo字段则会自动带上")
# endregion res

# region api
class SetGroupRemarkAPI(BaseModel):
    """set_group_remark接口数据模型"""
    endpoint: str = "set_group_remark"
    method: str = "POST"
    Req: type[BaseModel] = SetGroupRemarkReq
    Res: type[BaseModel] = SetGroupRemarkRes
# endregion api




# endregion code
