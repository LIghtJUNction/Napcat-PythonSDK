# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/226658740e0
@llms.txt: https://napcat.apifox.cn/226658740e0.md
@last_update: 2025-04-27 00:53:40

@description: 

summary:_发送群公告

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.43"
__endpoint__ = "_send_group_notice"
__id__ = "226658740e0"
__method__ = "POST"

# endregion METADATA


# region code
from typing import Literal
from pydantic import BaseModel, Field

# region req
class SendGroupNoticeReq(BaseModel):
    """
    _发送群公告 请求模型
    """
    group_id: int | str = Field(..., description="群号")
    content: str = Field(..., description="内容")
    image: str | None = Field(None, description="图片路径")
    pinned: int | str | None = Field(None, description="是否置顶")
    type: int | str | None = Field(None, description="公告类型")
    confirm_required: int | str | None = Field(None, description="是否需要群成员确认")
    is_show_edit_card: int | str | None = Field(None, description="是否显示编辑卡")
    tip_window_type: int | str | None = Field(None, description="弹窗类型")
# endregion req



# region res
class SendGroupNoticeRes(BaseModel):
    """
    _发送群公告 响应模型
    """
    status: Literal["ok"] = Field("ok", description="状态码")
    retcode: int = Field(..., description="返回码")
    data: None = Field(None, description="数据") # API定义中data为null
    message: str = Field(..., description="消息")
    wording: str = Field(..., description="提示")
    echo: str | None = Field(None, description="Echo回显")
# endregion res

# region api
class SendGroupNoticeAPI(BaseModel):
    """_send_group_notice接口数据模型"""
    endpoint: str = "_send_group_notice"
    method: str = "POST"
    Req: type[BaseModel] = SendGroupNoticeReq
    Res: type[BaseModel] = SendGroupNoticeRes
# endregion api




# endregion code
