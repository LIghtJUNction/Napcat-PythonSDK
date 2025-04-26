# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: 文件相关
@homepage: https://napcat.apifox.cn/283136366e0
@llms.txt: https://napcat.apifox.cn/283136366e0.md
@last_update: 2025-04-27 00:53:41

@description: 转存为永久文件

summary:转存为永久文件

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.43"
__endpoint__ = "trans_group_file"
__id__ = "283136366e0"
__method__ = "POST"

# endregion METADATA


# region code
import logging
from pydantic import BaseModel, Field
from typing import Literal

logger = logging.getLogger(__name__)

# region req
class TransGroupFileReq(BaseModel):
    """
    转存为永久文件 请求模型
    """

    group_id: int | str = Field(..., description="群号")
    file_id: str = Field(..., description="文件ID")
# endregion req



# region res
class TransGroupFileRes(BaseModel):
    """
    转存为永久文件 响应模型
    """
    class Data(BaseModel):
        """
        响应数据
        """
        ok: bool = Field(..., description="是否成功")

    status: Literal["ok"] = Field("ok", description="状态")
    retcode: int = Field(..., description="返回码")
    data: Data = Field(..., description="响应数据")
    message: str = Field(..., description="消息")
    wording: str = Field(..., description="详细消息")
    echo: str | None = Field(None, description="Echo")
# endregion res

# region api
class TransGroupFileAPI(BaseModel):
    """trans_group_file接口数据模型"""
    endpoint: str = "trans_group_file"
    method: str = "POST"
    Req: type[BaseModel] = TransGroupFileReq
    Res: type[BaseModel] = TransGroupFileRes
# endregion api




# endregion code