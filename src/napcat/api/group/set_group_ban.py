# -*- coding: utf-8 -*-
"""
@author: LIghtJUNction
@builder: AI

@build_id: 165
@api_id: 226656791e0
@endpoint: set_group_ban
@tags: 群聊相关
@homepage: https://api.napcat.com/226656791e0
@llms.txt: https://api.napcat.com/226656791e0.md
@version: 4.7.17
@last_update: 2025-04-22 22:32:34

@description: set_group_ban API
@usage: 使用 `client.set_group_ban()` 调用此API

"""
# region METADATA

__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "set_group_ban"
__method__ = "POST"


# region {
from typing import Literal, Any

from pydantic import BaseModel, Field
from napcat.base.models import BaseHttpAPI, BaseHttpResponse, BaseHttpRequest

    # 示例 endpoint : send_group_message  特殊 endpoint : _开头 .开头 给类命名时 .忽略即可(如 _get_model_show -> GetModelShowAPI)
    # 示例 class : SendGroupMessageAPI
    # 示例 request : SendGroupMessageReq
    # 示例 response : SendGroupMessageRes
    # 示例 data : SendGroupMessageData
    # 请将你需要展示给用户的注释符："#"放置于行首
    # 否则将被清理掉


# request model
class SetGroupBanReq(BaseHttpRequest):
    """
    set_group_ban 请求参数
    """

    pass


class SetGroupBanData(BaseModel):
    """
    set_group_ban 数据结构
    """
    # 定义可选数据字段
    # 例如：
    # param1: str = Field(..., description="参数1的描述")
    # param2: int = Field(..., description="参数2的描述")
    
    pass


# response model
class SetGroupBanRes(BaseHttpResponse[SetGroupBanData]):
    """
    set_group_ban 响应参数
    """
    # 定义响应参数
    # 例如：
    # param1: str = Field(..., description="参数1的描述")
    # param2: int = Field(..., description="参数2的描述")
    
    pass


# API class
class SetGroupBanAPI(BaseHttpAPI[SetGroupBanReq, SetGroupBanRes]):
    """
    群禁言
    """
    api: str = "/set_group_ban"
    method: Literal["POST", "GET"] = "POST"

    Request = SetGroupBanReq
    Response = SetGroupBanRes

    request: SetGroupBanReq
    response: SetGroupBanRes
    

if __name__ == "__main__":

    from napcat.base.utils import test_model
    test_model(SetGroupBanAPI)

# region }

