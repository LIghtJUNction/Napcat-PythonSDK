# -*- coding: utf-8 -*-
"""
@author: LIghtJUNction
@builder: AI

@build_id: 214
@api_id: 226659219e0
@endpoint: fetch_emoji_like
@tags: 消息相关
@homepage: https://napcat.apifox.cn/226659219e0
@llms.txt: https://napcat.apifox.cn/226659219e0.md
@version: 4.7.17
@last_update: 2025-04-23 04:39:49

@description: fetch_emoji_like API
@usage: 使用 `client.fetch_emoji_like()` 调用此API

"""
# region METADATA

__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "fetch_emoji_like"
__method__ = "POST"


# region code
from typing import Literal, Any

from pydantic import BaseModel, Field
from napcat.base.models import BaseHttpAPI, BaseHttpResponse, BaseHttpRequest



# region req
class FetchEmojiLikeReq(BaseHttpRequest):
    """
    fetch_emoji_like 请求参数
    """

    pass
# region req/

# region data
class FetchEmojiLikeData(BaseModel):
    """
    fetch_emoji_like 数据结构
    """
    # 定义可选数据字段
    # 例如：
    # param1: str = Field(..., description="参数1的描述")
    # param2: int = Field(..., description="参数2的描述")
    
    pass
# region data/

# region res
class FetchEmojiLikeRes(BaseHttpResponse[FetchEmojiLikeData]):
    """
    fetch_emoji_like 响应参数
    """
    # 定义响应参数
    # 例如：
    # param1: str = Field(..., description="参数1的描述")
    # param2: int = Field(..., description="参数2的描述")
    
    pass
# region res/

# region api
class FetchEmojiLikeAPI(BaseHttpAPI[FetchEmojiLikeReq, FetchEmojiLikeRes]):
    """
    获取贴表情详情
    """
    api: str = "/fetch_emoji_like"
    method: Literal["POST", "GET"] = "POST"

    Request = FetchEmojiLikeReq
    Response = FetchEmojiLikeRes

    request: FetchEmojiLikeReq
    response: FetchEmojiLikeRes
# region api/


if __name__ == "__main__":

    from napcat.base.utils import test_model
    test_model(FetchEmojiLikeAPI)

# region code/

