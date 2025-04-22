# -*- coding: utf-8 -*-
"""
@author: LIghtJUNction
@builder: AI

@build_id: 165
@api_id: 226658674e0
@endpoint: set_essence_msg
@tags: 群聊相关
@homepage: https://api.napcat.com/226658674e0
@llms.txt: https://api.napcat.com/226658674e0.md
@version: 4.7.17
@last_update: 2025-04-22 22:32:34

@description: set_essence_msg API
@usage: 使用 `client.set_essence_msg()` 调用此API

"""
# region METADATA

__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "set_essence_msg"
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
class SetEssenceMsgReq(BaseHttpRequest):
    """
    set_essence_msg 请求参数
    """

    pass


class SetEssenceMsgData(BaseModel):
    """
    set_essence_msg 数据结构
    """
    # 定义可选数据字段
    # 例如：
    # param1: str = Field(..., description="参数1的描述")
    # param2: int = Field(..., description="参数2的描述")
    
    pass


# response model
class SetEssenceMsgRes(BaseHttpResponse[SetEssenceMsgData]):
    """
    set_essence_msg 响应参数
    """
    # 定义响应参数
    # 例如：
    # param1: str = Field(..., description="参数1的描述")
    # param2: int = Field(..., description="参数2的描述")
    
    pass


# API class
class SetEssenceMsgAPI(BaseHttpAPI[SetEssenceMsgReq, SetEssenceMsgRes]):
    """
    设置群精华消息
    """
    api: str = "/set_essence_msg"
    method: Literal["POST", "GET"] = "POST"

    Request = SetEssenceMsgReq
    Response = SetEssenceMsgRes

    request: SetEssenceMsgReq
    response: SetEssenceMsgRes
    

if __name__ == "__main__":

    from napcat.base.utils import test_model
    test_model(SetEssenceMsgAPI)

# region }

