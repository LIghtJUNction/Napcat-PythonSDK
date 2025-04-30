# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: 群聊相关
@homepage: https://napcat.apifox.cn/226659240e0
@llms.txt: https://napcat.apifox.cn/226659240e0.md
@last_update: 2025-04-27 00:53:40

@description: 

summary:_删除群公告

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.43"
__endpoint__ = "_del_group_notice"
__id__ = "226659240e0"
__method__ = "POST"

# endregion METADATA


# region code
from pydantic import BaseModel, Field
from typing import Literal


# region req
class DelGroupNoticeReq(BaseModel):
    """
    _del_group_notice请求参数
    """

    group_id: int | str = Field(..., description="群号")
    notice_id: str = Field(..., description="群公告ID")

# endregion req



# region res
class DelGroupNoticeResData(BaseModel):
    """
    _del_group_notice响应数据data字段模型
    """
    result: int | float = Field(..., description="结果")
    errMsg: str = Field(..., description="错误信息")


class DelGroupNoticeRes(BaseModel):
    """
    _del_group_notice响应参数
    """

    status: Literal["ok"] = Field("ok", description="状态码，固定为 'ok'")
    retcode: int | float = Field(..., description="返回码")
    data: DelGroupNoticeResData = Field(..., description="响应数据")
    message: str = Field(..., description="消息")
    wording: str = Field(..., description="文本")
    echo: str | None = Field(None, description="回显")

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