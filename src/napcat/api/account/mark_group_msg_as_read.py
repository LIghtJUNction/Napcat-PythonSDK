# -*- coding: utf-8 -*-
"""
@author: LIghtJUNction
@builder: AI

@build_id: 214
@api_id: 226659167e0
@endpoint: mark_group_msg_as_read
@tags: 账号相关
@homepage: https://napcat.apifox.cn/226659167e0
@llms.txt: https://napcat.apifox.cn/226659167e0.md
@version: 4.7.17
@last_update: 2025-04-23 04:39:50

@description: mark_group_msg_as_read API
@usage: 使用 `client.mark_group_msg_as_read()` 调用此API

"""
# region METADATA

__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "mark_group_msg_as_read"
__method__ = "POST"


# region code
from typing import Literal, Any

from pydantic import BaseModel, Field
from napcat.base.models import BaseHttpAPI, BaseHttpResponse, BaseHttpRequest



# region req
class MarkGroupMsgAsReadReq(BaseHttpRequest):
    """
    mark_group_msg_as_read 请求参数
    """

    pass
# region req/

# region data
class MarkGroupMsgAsReadData(BaseModel):
    """
    mark_group_msg_as_read 数据结构
    """
    # 定义可选数据字段
    # 例如：
    # param1: str = Field(..., description="参数1的描述")
    # param2: int = Field(..., description="参数2的描述")
    
    pass
# region data/

# region res
class MarkGroupMsgAsReadRes(BaseHttpResponse[None]):
    """
    mark_group_msg_as_read 响应参数
    """
    # 定义响应参数
    # 例如：
    # param1: str = Field(..., description="参数1的描述")
    # param2: int = Field(..., description="参数2的描述")
    
    pass
# region res/

# region api
class MarkGroupMsgAsReadAPI(BaseHttpAPI[MarkGroupMsgAsReadReq, MarkGroupMsgAsReadRes]):
    """
    设置群聊已读
    """
    api: str = "/mark_group_msg_as_read"
    method: Literal["POST", "GET"] = "POST"

    Request = MarkGroupMsgAsReadReq
    Response = MarkGroupMsgAsReadRes

    request: MarkGroupMsgAsReadReq
    response: MarkGroupMsgAsReadRes
# region api/


if __name__ == "__main__":

    from napcat.base.utils import test_model
    test_model(MarkGroupMsgAsReadAPI)

# region code/

