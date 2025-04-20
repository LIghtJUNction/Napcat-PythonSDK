# -*- coding: utf-8 -*-
"""
设置群聊已读 API
开发完毕
@作者：GitHub Copilot
@日期：2025/04/20
"""

from typing import Literal

from pydantic import ConfigDict, Field
from ..base.models import BaseHttpAPI, BaseHttpRequest, BaseHttpResponse, BaseModel


class Request(BaseHttpRequest):
    """
    设置群聊已读请求参数
    """
    group_id: int | str = Field(description="要标记已读的群号")


class ResponseData(BaseModel):
    """
    设置群聊已读响应数据模型
    """
    success: bool = Field(default=False, description="是否标记成功")
    message: str = Field(default="", description="结果消息")
    
    model_config = ConfigDict(
        extra="allow",  # 允许额外字段
        frozen=False,   # 不冻结模型
        populate_by_name=True,  # 通过名称填充字段
        arbitrary_types_allowed=True,  # 允许任意类型
    )


class Response(BaseHttpResponse[ResponseData]):
    """
    设置群聊已读响应参数
    """
    pass


class MarkGroupMsgAsReadAPI(BaseHttpAPI):
    """
    设置群聊已读 API
    用于将指定群聊的所有未读消息标记为已读状态
    接口地址: https://napcat.apifox.cn/226659167e0.md

    参数：
    {
      "group_id": 123456789  // 群号
    }

    返回：
    - 标记群聊消息已读的结果状态，包含是否成功和相关消息
    """

    api: str = "/mark_group_msg_as_read"
    method: Literal['POST', 'GET'] = "POST"
    request: BaseHttpRequest = Request()
    response: BaseHttpResponse[ResponseData] = Response()

if __name__ == "__main__":
    from ..base.utils import test_model
    # uv pip install -e . 
    # python -m napcat.api.account.mark_group_msg_as_read
    test_model(Request)
    test_model(ResponseData)
    test_model(Response)