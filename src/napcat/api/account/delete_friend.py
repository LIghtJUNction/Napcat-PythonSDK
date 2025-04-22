# -*- coding: utf-8 -*-
"""
@author: LIghtJUNction
@builder: AI

@build_id: 214
@api_id: 227237873e0
@endpoint: delete_friend
@tags: 账号相关
@homepage: https://napcat.apifox.cn/227237873e0
@llms.txt: https://napcat.apifox.cn/227237873e0.md
@version: 4.7.17
@last_update: 2025-04-23 04:39:50

@description: delete_friend API
@usage: 使用 `client.delete_friend()` 调用此API

"""
# region METADATA

__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "delete_friend"
__method__ = "POST"


# region code
from typing import Literal, Any

from pydantic import BaseModel, Field
from napcat.base.models import BaseHttpAPI, BaseHttpResponse, BaseHttpRequest



# region req
class DeleteFriendReq(BaseHttpRequest):
    """
    delete_friend 请求参数
    """

    pass
# region req/

# region data
class DeleteFriendData(BaseModel):
    """
    delete_friend 数据结构
    """
    # 定义可选数据字段
    # 例如：
    # param1: str = Field(..., description="参数1的描述")
    # param2: int = Field(..., description="参数2的描述")
    
    pass
# region data/

# region res
class DeleteFriendRes(BaseHttpResponse[DeleteFriendData]):
    """
    delete_friend 响应参数
    """
    # 定义响应参数
    # 例如：
    # param1: str = Field(..., description="参数1的描述")
    # param2: int = Field(..., description="参数2的描述")
    
    pass
# region res/

# region api
class DeleteFriendAPI(BaseHttpAPI[DeleteFriendReq, DeleteFriendRes]):
    """
    删除好友
    """
    api: str = "/delete_friend"
    method: Literal["POST", "GET"] = "POST"

    Request = DeleteFriendReq
    Response = DeleteFriendRes

    request: DeleteFriendReq
    response: DeleteFriendRes
# region api/


if __name__ == "__main__":

    from napcat.base.utils import test_model
    test_model(DeleteFriendAPI)

# region code/

