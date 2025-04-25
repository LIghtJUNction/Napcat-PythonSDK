# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: ['群聊相关']
@homepage: https://napcat.apifox.cn/226659240e0
@llms.txt: https://napcat.apifox.cn/226659240e0.md
@last_update: 2025-04-26 01:17:45

@description: 

summary:_删除群公告

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "_del_group_notice"
__id__ = "226659240e0"
__method__ = "POST"

# endregion METADATA


# region code
import logging
from pydantic import BaseModel, Field
from typing import Literal

logger = logging.getLogger(__name__)

# region req
class DelGroupNoticeReq(BaseModel):
    """
    删除群公告请求模型
    """

    group_id: int | str = Field(..., description="群号")
    notice_id: str = Field(..., description="公告 ID")

# endregion req



# region res
class DelGroupNoticeRes(BaseModel):
    """
    删除群公告响应模型
    """

    class Data(BaseModel):
        """
        响应数据详情
        """
        result: int | float = Field(..., description="删除结果，可能是数字")
        errMsg: str = Field(..., description="错误信息")

    status: Literal["ok"] = Field(..., description="状态")
    retcode: int | float = Field(..., description="返回码")
    data: Data = Field(..., description="响应数据")
    message: str = Field(..., description="消息")
    wording: str = Field(..., description="提示")
    echo: str | None = Field(None, description="回显，可能为空")

# endregion res

# region api
class DelGroupNoticeAPI(BaseModel):
    """_del_group_notice接口数据模型"""
    endpoint: str = "_del_group_notice"
    method: str = "POST"
    Req: type[BaseModel] = DelGroupNoticeReq
    Res: type[BaseModel] = DelGroupNoticeRes
# endregion api




# endregion code