# -*- coding: utf-8 -*-
"""
设置在线状态 API
开发完毕
@作者：GitHub Copilot
@日期：2025/04/20
"""

from typing import Literal

from pydantic import ConfigDict, Field
from ..base.models import BaseHttpAPI, BaseHttpRequest, BaseHttpResponse, BaseModel


class Request(BaseHttpRequest):
    """
    设置在线状态请求参数
    """
    status: int = Field(description="在线状态代码，如10表示在线，30表示离开，40表示隐身，50表示忙碌，60表示Q我吧，70表示请勿打扰")
    ext_status: int = Field(default=0, description="扩展在线状态，如1016表示睡觉中，1018表示学习中，1028表示听歌中，1032表示熬夜中，等")
    battery_status: int = Field(default=0, description="电量状态，0-100之间的整数表示电量百分比")


class ResponseData(BaseModel):
    """
    设置在线状态响应数据模型
    """
    success: bool = Field(default=False, description="是否设置成功")
    message: str = Field(default="", description="结果消息")
    
    model_config = ConfigDict(
        extra="allow",  # 允许额外字段
        frozen=False,   # 不冻结模型
        populate_by_name=True,  # 通过名称填充字段
        arbitrary_types_allowed=True,  # 允许任意类型
    )


class Response(BaseHttpResponse[ResponseData]):
    """
    设置在线状态响应参数
    """
    pass


class SetOnlineStatusAPI(BaseHttpAPI):
    """
    设置在线状态 API
    用于设置当前QQ账号的在线状态，如在线、离开、忙碌等
    接口地址: https://napcat.apifox.cn/226659187e0.md

    参数：
    {
      "status": 10,        // 在线状态代码，10表示在线，30表示离开，40表示隐身，50表示忙碌，60表示Q我吧，70表示请勿打扰
      "ext_status": 1018,  // 扩展在线状态，如1018表示学习中
      "battery_status": 85 // 电量状态，0-100之间的整数表示电量百分比
    }

    返回：
    - 设置在线状态的结果信息，包含是否成功和相关消息
    """

    api: str = "/set_online_status"
    method: Literal['POST', 'GET'] = "POST"
    request: BaseHttpRequest = Request()
    response: BaseHttpResponse[ResponseData] = Response()

if __name__ == "__main__":
    from ..base.utils import test_model
    # uv pip install -e . 
    # python -m napcat.api.account.set_online_status
    test_model(Request)
    test_model(ResponseData)
    test_model(Response)