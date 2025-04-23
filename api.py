# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: {{homepage}}
@llms.txt: {{llms.txt}}
@last_update: {{last_update}}

@description: {{description}}

"""
__author__ = "LIghtJUNction"
__version__ = "{{version}}"
__endpoint__ = "{{endpoint}}"
__id__ = "{{api_id}}"
__method__ = "POST"

# region METADATA/


# region code
from typing import Any , Literal

from pydantic import BaseModel, Field

# region req
class {{EndPointReq}}(BaseModel): # type: ignore
    """
    {{DESC_EndPointReq}}
    """

    pass
# region req/



# region res
class {{EndPointRes}}(BaseModel): # type: ignore
    # 定义响应参数
    # 例如：
    # param1: str = Field(..., description="参数1的描述")
    # param2: int = Field(..., description="参数2的描述")
    
    pass
# region res/

# region api
class {{EndPointAPI}}(BaseModel):
    
    Request : type[{{EndPointReq}}] = {{EndPointReq}}
    Response  : type[{{EndPointRes}}] = {{EndPointRes}}


# region api/




# region code/

