# -*- coding: utf-8 -*-
# region METADATA
"""
@author: LIghtJUNction

@api_id: 226658678e0
@endpoint: delete_essence_msg
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/226658678e0
@llms.txt: https://napcat.apifox.cn/226658678e0.md
@version: 4.7.17
@last_update: 2025-04-23 20:09:55

@description: 

summary:删除群精华消息

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "delete_essence_msg"
__method__ = "POST"

# region METADATA/


# region code
from typing import Any , Literal

from pydantic import BaseModel, Field

# region req
class DeleteEssenceMsgReq(BaseModel): # type: ignore
    """
    {{DESC_EndPointReq}}
    """

    pass
# region req/



# region res
class DeleteEssenceMsgRes(BaseModel): # type: ignore
    # 定义响应参数
    # 例如：
    # param1: str = Field(..., description="参数1的描述")
    # param2: int = Field(..., description="参数2的描述")
    
    pass
# region res/

# region api
class DeleteEssenceMsgAPI(BaseModel):
    
    Request : type[DeleteEssenceMsgReq] = DeleteEssenceMsgReq
    Response  : type[DeleteEssenceMsgRes] = DeleteEssenceMsgRes


# region api/




# region code/

