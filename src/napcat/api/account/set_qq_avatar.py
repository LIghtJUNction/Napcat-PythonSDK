# -*- coding: utf-8 -*-
"""
@author: LIghtJUNction
@builder: AI

@build_id: 214
@api_id: 226658980e0
@endpoint: set_qq_avatar
@tags: 账号相关
@homepage: https://napcat.apifox.cn/226658980e0
@llms.txt: https://napcat.apifox.cn/226658980e0.md
@version: 4.7.17
@last_update: 2025-04-23 04:39:50

@description: set_qq_avatar API
@usage: 使用 `client.set_qq_avatar()` 调用此API

"""
# region METADATA

__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "set_qq_avatar"
__method__ = "POST"


# region code
from typing import Literal, Any

from pydantic import BaseModel, Field
from napcat.base.models import BaseHttpAPI, BaseHttpResponse, BaseHttpRequest



# region req
class SetQqAvatarReq(BaseHttpRequest):
    """
    set_qq_avatar 请求参数
    """

    pass
# region req/

# region data
class SetQqAvatarData(BaseModel):
    """
    set_qq_avatar 数据结构
    """
    # 定义可选数据字段
    # 例如：
    # param1: str = Field(..., description="参数1的描述")
    # param2: int = Field(..., description="参数2的描述")
    
    pass
# region data/

# region res
class SetQqAvatarRes(BaseHttpResponse[None]):
    """
    set_qq_avatar 响应参数
    """
    # 定义响应参数
    # 例如：
    # param1: str = Field(..., description="参数1的描述")
    # param2: int = Field(..., description="参数2的描述")
    
    pass
# region res/

# region api
class SetQqAvatarAPI(BaseHttpAPI[SetQqAvatarReq, SetQqAvatarRes]):
    """
    设置头像
    """
    api: str = "/set_qq_avatar"
    method: Literal["POST", "GET"] = "POST"

    Request = SetQqAvatarReq
    Response = SetQqAvatarRes

    request: SetQqAvatarReq
    response: SetQqAvatarRes
# region api/


if __name__ == "__main__":

    from napcat.base.utils import test_model
    test_model(SetQqAvatarAPI)

# region code/

