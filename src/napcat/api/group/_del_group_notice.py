# -*- coding: utf-8 -*-
"""
@author: LIghtJUNction
@builder: AI

@build_id: 214
@api_id: 226659240e0
@endpoint: _del_group_notice
@tags: 群聊相关
@homepage: https://napcat.apifox.cn/226659240e0
@llms.txt: https://napcat.apifox.cn/226659240e0.md
@version: 4.7.17
@last_update: 2025-04-23 04:39:50

@description: _del_group_notice API
@usage: 使用 `client._del_group_notice()` 调用此API

"""
# region METADATA

__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "_del_group_notice"
__method__ = "POST"


# region code
from typing import Literal, Any

from pydantic import BaseModel, Field
from napcat.base.models import BaseHttpAPI, BaseHttpResponse, BaseHttpRequest



# region req
class DelGroupNoticeReq(BaseHttpRequest):
    """
    _del_group_notice 请求参数
    """

    pass
# region req/

# region data
class DelGroupNoticeData(BaseModel):
    """
    _del_group_notice 数据结构
    """
    # 定义可选数据字段
    # 例如：
    # param1: str = Field(..., description="参数1的描述")
    # param2: int = Field(..., description="参数2的描述")
    
    pass
# region data/

# region res
class DelGroupNoticeRes(BaseHttpResponse[DelGroupNoticeData]):
    """
    _del_group_notice 响应参数
    """
    # 定义响应参数
    # 例如：
    # param1: str = Field(..., description="参数1的描述")
    # param2: int = Field(..., description="参数2的描述")
    
    pass
# region res/

# region api
class DelGroupNoticeAPI(BaseHttpAPI[DelGroupNoticeReq, DelGroupNoticeRes]):
    """
    _删除群公告
    """
    api: str = "/_del_group_notice"
    method: Literal["POST", "GET"] = "POST"

    Request = DelGroupNoticeReq
    Response = DelGroupNoticeRes

    request: DelGroupNoticeReq
    response: DelGroupNoticeRes
# region api/


if __name__ == "__main__":

    from napcat.base.utils import test_model
    test_model(DelGroupNoticeAPI)

# region code/

