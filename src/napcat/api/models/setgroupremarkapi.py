# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: 群聊相关
@homepage: https://napcat.apifox.cn/283136268e0
@llms.txt: https://napcat.apifox.cn/283136268e0.md
@last_update: 2025-04-26 01:17:45

@description: 

summary:设置群备注

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "set_group_remark"
__id__ = "283136268e0"
__method__ = "POST"

# endregion METADATA


# region code
import logging
from typing import Literal
from pydantic import BaseModel, Field

logger = logging.getLogger(__name__)

# region req
class SetGroupRemarkReq(BaseModel):
    """
    请求参数模型
    """

    group_id: str = Field(..., description="群号")
    remark: str = Field(..., description="群备注")
# endregion req



# region res
class SetGroupRemarkRes(BaseModel):
    """
    响应参数模型
    """

    status: Literal["ok"] = Field(
        ..., description="状态，目前固定为 'ok'"
    )
    retcode: int = Field(..., description="返回码")
    data: None = Field(..., description="数据，固定为 null")
    message: str = Field(..., description="错误信息")
    wording: str = Field(..., description="错误信息的友好表达")
    echo: str | None = Field(None, description="用户传入的 echo 字段")
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
