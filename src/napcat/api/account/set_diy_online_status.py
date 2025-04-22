# -*- coding: utf-8 -*-
"""
@author: LIghtJUNction
@builder: AI

@build_id: 213
@api_id: 266151905e0
@endpoint: set_diy_online_status
@tags: 账号相关
@homepage: https://napcat.apifox.cn/266151905e0
@llms.txt: https://napcat.apifox.cn/266151905e0.md
@version: 4.7.17
@last_update: 2025-04-23 04:35:53

@description: set_diy_online_status API
@usage: 使用 `client.set_diy_online_status()` 调用此API

"""
# region METADATA

__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "set_diy_online_status"
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
class SetDiyOnlineStatusReq(BaseHttpRequest):
    """
    set_diy_online_status 请求参数
    """

    pass
# region req/

# region data
class SetDiyOnlineStatusData(BaseModel):
    """
    set_diy_online_status 数据结构
    """
    # 定义可选数据字段
    # 例如：
    # param1: str = Field(..., description="参数1的描述")
    # param2: int = Field(..., description="参数2的描述")
    
    pass
# region data/

# region res
class SetDiyOnlineStatusRes(BaseHttpResponse[str]):
    """
    set_diy_online_status 响应参数
    """
    # 定义响应参数
    # 例如：
    # param1: str = Field(..., description="参数1的描述")
    # param2: int = Field(..., description="参数2的描述")
    
    pass
# region res/

# region api
class SetDiyOnlineStatusAPI(BaseHttpAPI[SetDiyOnlineStatusReq, SetDiyOnlineStatusRes]):
    """
    设置自定义在线状态
    """
    api: str = "/set_diy_online_status"
    method: Literal["POST", "GET"] = "POST"

    Request = SetDiyOnlineStatusReq
    Response = SetDiyOnlineStatusRes

    request: SetDiyOnlineStatusReq
    response: SetDiyOnlineStatusRes
# region api/


if __name__ == "__main__":

    from napcat.base.utils import test_model
    test_model(SetDiyOnlineStatusAPI)

# region code/

