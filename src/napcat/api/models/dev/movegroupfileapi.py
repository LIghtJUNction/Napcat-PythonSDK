# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: 文件相关
@homepage: https://napcat.apifox.cn/283136359e0
@llms.txt: https://napcat.apifox.cn/283136359e0.md
@last_update: 2025-04-27 00:53:41

@description: 

summary:移动群文件

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.43"
__endpoint__ = "move_group_file"
__id__ = "283136359e0"
__method__ = "POST"

# endregion METADATA


# region code
import logging
from typing import Literal
from pydantic import BaseModel, Field

logger = logging.getLogger(__name__)

# region req
class MoveGroupFileReq(BaseModel):
    """
    移动群文件请求模型
    """

    group_id: int | str = Field(..., description="群号")
    file_id: str = Field(..., description="文件ID")
    current_parent_directory: str = Field(..., description="当前父目录，根目录填 /")
    target_parent_directory: str = Field(..., description="目标父目录")

# endregion req



# region res
class MoveGroupFileRes(BaseModel):
    """
    移动群文件响应模型
    """
    class Data(BaseModel):
        """
        响应数据
        """
        ok: bool = Field(..., description="是否成功")

    status: Literal["ok"] = Field(..., description="状态")
    retcode: int = Field(..., description="返回码")
    data: Data = Field(..., description="响应数据")
    message: str = Field(..., description="消息")
    wording: str = Field(..., description="词语")
    echo: str | None = Field(..., description="echo")

# endregion res

# region api
class MoveGroupFileAPI(BaseModel):
    """move_group_file接口数据模型"""
    endpoint: str = "move_group_file"
    method: str = "POST"
    Req: type[BaseModel] = MoveGroupFileReq
    Res: type[BaseModel] = MoveGroupFileRes
# endregion api




# endregion code
