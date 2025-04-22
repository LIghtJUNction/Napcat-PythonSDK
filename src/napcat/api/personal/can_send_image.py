# -*- coding: utf-8 -*-
"""
@author: LIghtJUNction
@builder: AI

@build_id: 214
@api_id: 226657071e0
@endpoint: can_send_image
@tags: 个人操作
@homepage: https://napcat.apifox.cn/226657071e0
@llms.txt: https://napcat.apifox.cn/226657071e0.md
@version: 4.7.17
@last_update: 2025-04-23 04:39:51

@description: can_send_image API
@usage: 使用 `client.can_send_image()` 调用此API

"""
# region METADATA

__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "can_send_image"
__method__ = "POST"


# region code
from typing import Literal, Any

from pydantic import BaseModel, Field
from napcat.base.models import BaseHttpAPI, BaseHttpResponse, BaseHttpRequest



# region req
class CanSendImageReq(BaseHttpRequest):
    """
    can_send_image 请求参数
    """

    pass
# region req/

# region data
class CanSendImageData(BaseModel):
    """
    can_send_image 数据结构
    """
    # 定义可选数据字段
    # 例如：
    # param1: str = Field(..., description="参数1的描述")
    # param2: int = Field(..., description="参数2的描述")
    
    pass
# region data/

# region res
class CanSendImageRes(BaseHttpResponse[CanSendImageData]):
    """
    can_send_image 响应参数
    """
    # 定义响应参数
    # 例如：
    # param1: str = Field(..., description="参数1的描述")
    # param2: int = Field(..., description="参数2的描述")
    
    pass
# region res/

# region api
class CanSendImageAPI(BaseHttpAPI[CanSendImageReq, CanSendImageRes]):
    """
    检查是否可以发送图片
    """
    api: str = "/can_send_image"
    method: Literal["POST", "GET"] = "POST"

    Request = CanSendImageReq
    Response = CanSendImageRes

    request: CanSendImageReq
    response: CanSendImageRes
# region api/


if __name__ == "__main__":

    from napcat.base.utils import test_model
    test_model(CanSendImageAPI)

# region code/

