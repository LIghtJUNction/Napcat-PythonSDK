# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: 文件相关
@homepage: https://napcat.apifox.cn/283136366e0
@llms.txt: https://napcat.apifox.cn/283136366e0.md
@last_update: 2025-04-26 01:17:46

@description: 

summary:转存为永久文件

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "trans_group_file"
__id__ = "283136366e0"
__method__ = "POST"

# endregion METADATA


# region code
from pydantic import BaseModel, Field
from typing import Literal # Import Literal for constant values

# region req
class TransGroupFileReq(BaseModel):
    """
    转存为永久文件请求体
    """

    group_id: int | str = Field(
        ..., # Ellipsis indicates this field is required
        description="群号"
    )
    file_id: str = Field(
        ..., # Ellipsis indicates this field is required
        description="文件 ID"
    )
# endregion req



# region res
class TransGroupFileRes(BaseModel):
    """
    转存为永久文件响应体
    """

    class TransGroupFileData(BaseModel):
        """
        响应数据字段
        """
        ok: bool = Field(
            ..., # Ellipsis indicates this field is required
            description="是否成功"
        )

    status: Literal['ok'] = Field(
        ..., # Ellipsis indicates this field is required
        description="状态码"
    )
    retcode: int = Field(
        ..., # Ellipsis indicates this field is required
        description="返回码"
    )
    data: TransGroupFileData = Field(
        ..., # Ellipsis indicates this field is required
        description="响应数据"
    )
    message: str = Field(
        ..., # Ellipsis indicates this field is required
        description="消息"
    )
    wording: str = Field(
        ..., # Ellipsis indicates this field is required
        description="wording"
    )
    echo: str | None = Field(
        default=None, # Default value makes this field optional
        description="echo"
    )
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
