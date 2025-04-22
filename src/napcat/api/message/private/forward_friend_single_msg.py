# -*- coding: utf-8 -*-
"""
@author: LIghtJUNction
@builder: AI

@build_id: 214
@api_id: 226659051e0
@endpoint: forward_friend_single_msg
@tags: 消息相关/发送私聊消息
@homepage: https://napcat.apifox.cn/226659051e0
@llms.txt: https://napcat.apifox.cn/226659051e0.md
@version: 4.7.17
@last_update: 2025-04-23 04:39:49

@description: forward_friend_single_msg API
@usage: 使用 `client.forward_friend_single_msg()` 调用此API

"""
# region METADATA

__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "forward_friend_single_msg"
__method__ = "POST"


# region code
from typing import Literal, Any

from pydantic import BaseModel, Field
from napcat.base.models import BaseHttpAPI, BaseHttpResponse, BaseHttpRequest



# region req
class ForwardFriendSingleMsgReq(BaseHttpRequest):
    """
    forward_friend_single_msg 请求参数
    """

    pass
# region req/

# region data
class ForwardFriendSingleMsgData(BaseModel):
    """
    forward_friend_single_msg 数据结构
    """
    # 定义可选数据字段
    # 例如：
    # param1: str = Field(..., description="参数1的描述")
    # param2: int = Field(..., description="参数2的描述")
    
    pass
# region data/

# region res
class ForwardFriendSingleMsgRes(BaseHttpResponse[None]):
    """
    forward_friend_single_msg 响应参数
    """
    # 定义响应参数
    # 例如：
    # param1: str = Field(..., description="参数1的描述")
    # param2: int = Field(..., description="参数2的描述")
    
    pass
# region res/

# region api
class ForwardFriendSingleMsgAPI(BaseHttpAPI[ForwardFriendSingleMsgReq, ForwardFriendSingleMsgRes]):
    """
    消息转发到私聊
    """
    api: str = "/forward_friend_single_msg"
    method: Literal["POST", "GET"] = "POST"

    Request = ForwardFriendSingleMsgReq
    Response = ForwardFriendSingleMsgRes

    request: ForwardFriendSingleMsgReq
    response: ForwardFriendSingleMsgRes
# region api/


if __name__ == "__main__":

    from napcat.base.utils import test_model
    test_model(ForwardFriendSingleMsgAPI)

# region code/

