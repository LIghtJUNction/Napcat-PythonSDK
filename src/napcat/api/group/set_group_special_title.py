# -*- coding: utf-8 -*-
"""
@author: LIghtJUNction
@builder: AI

@build_id: 214
@api_id: 226656931e0
@endpoint: set_group_special_title
@tags: 群聊相关
@homepage: https://napcat.apifox.cn/226656931e0
@llms.txt: https://napcat.apifox.cn/226656931e0.md
@version: 4.7.17
@last_update: 2025-04-23 04:39:50

@description: set_group_special_title API
@usage: 使用 `client.set_group_special_title()` 调用此API

"""
# region METADATA

__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "set_group_special_title"
__method__ = "POST"


# region code
from typing import Literal, Any

from pydantic import BaseModel, Field
from napcat.base.models import BaseHttpAPI, BaseHttpResponse, BaseHttpRequest



# region req
class SetGroupSpecialTitleReq(BaseHttpRequest):
    """
    set_group_special_title 请求参数
    """

    pass
# region req/

# region data
class SetGroupSpecialTitleData(BaseModel):
    """
    set_group_special_title 数据结构
    """
    # 定义可选数据字段
    # 例如：
    # param1: str = Field(..., description="参数1的描述")
    # param2: int = Field(..., description="参数2的描述")
    
    pass
# region data/

# region res
class SetGroupSpecialTitleRes(BaseHttpResponse[None]):
    """
    set_group_special_title 响应参数
    """
    # 定义响应参数
    # 例如：
    # param1: str = Field(..., description="参数1的描述")
    # param2: int = Field(..., description="参数2的描述")
    
    pass
# region res/

# region api
class SetGroupSpecialTitleAPI(BaseHttpAPI[SetGroupSpecialTitleReq, SetGroupSpecialTitleRes]):
    """
    设置群头衔
    """
    api: str = "/set_group_special_title"
    method: Literal["POST", "GET"] = "POST"

    Request = SetGroupSpecialTitleReq
    Response = SetGroupSpecialTitleRes

    request: SetGroupSpecialTitleReq
    response: SetGroupSpecialTitleRes
# region api/


if __name__ == "__main__":

    from napcat.base.utils import test_model
    test_model(SetGroupSpecialTitleAPI)

# region code/

