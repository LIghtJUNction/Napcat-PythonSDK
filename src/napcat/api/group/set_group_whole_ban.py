# -*- coding: utf-8 -*-
"""
@author: LIghtJUNction
@builder: AI

@build_id: 213
@api_id: 226656802e0
@endpoint: set_group_whole_ban
@tags: 群聊相关
@homepage: https://napcat.apifox.cn/226656802e0
@llms.txt: https://napcat.apifox.cn/226656802e0.md
@version: 4.7.17
@last_update: 2025-04-23 04:35:53

@description: set_group_whole_ban API
@usage: 使用 `client.set_group_whole_ban()` 调用此API

"""
# region METADATA

__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "set_group_whole_ban"
__method__ = "POST"


# region code
from typing import Literal, Any

from pydantic import BaseModel, Field
from napcat.base.models import BaseHttpAPI, BaseHttpResponse, BaseHttpRequest

    -
    -
    -
    -
    -
    -
    -
    # 本行注释旨在测试构建清理逻辑


# region req
class SetGroupWholeBanReq(BaseHttpRequest):
    """
    set_group_whole_ban 请求参数
    """

    pass
# region req/

# region data
class SetGroupWholeBanData(BaseModel):
    """
    set_group_whole_ban 数据结构
    """
    # 定义可选数据字段
    # 例如：
    # param1: str = Field(..., description="参数1的描述")
    # param2: int = Field(..., description="参数2的描述")
    
    pass
# region data/

# region res
class SetGroupWholeBanRes(BaseHttpResponse[None]):
    """
    set_group_whole_ban 响应参数
    """
    # 定义响应参数
    # 例如：
    # param1: str = Field(..., description="参数1的描述")
    # param2: int = Field(..., description="参数2的描述")
    
    pass
# region res/

# region api
class SetGroupWholeBanAPI(BaseHttpAPI[SetGroupWholeBanReq, SetGroupWholeBanRes]):
    """
    全体禁言
    """
    api: str = "/set_group_whole_ban"
    method: Literal["POST", "GET"] = "POST"

    Request = SetGroupWholeBanReq
    Response = SetGroupWholeBanRes

    request: SetGroupWholeBanReq
    response: SetGroupWholeBanRes
# region api/


if __name__ == "__main__":

    from napcat.base.utils import test_model
    test_model(SetGroupWholeBanAPI)

# region code/

