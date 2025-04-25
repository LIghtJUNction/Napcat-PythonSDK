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

# endregion METADATA


# region code
import logging
from typing import Any
from pydantic import BaseModel, Field

logger = logging.getLogger(__name__)

# region req
class {{EndPointReq}}(BaseModel): # type: ignore
    """
    {{DESC_EndPointReq}}
    """

    pass
# endregion req



# region res
class {{EndPointRes}}(BaseModel): # type: ignore
    # 定义响应参数
    # 例如：
    # param1: str = Field(..., description="参数1的描述")
    # param2: int = Field(..., description="参数2的描述")
    
    pass
# endregion res

# region api
class {{EndPointAPI}}(BaseModel):
    """{{endpoint}}接口数据模型"""
    endpoint: str = "{{endpoint}}"
    method: str = "{{method}}"
    Req: type[BaseModel] = {{EndPointReq}}
    Res: type[BaseModel] = {{EndPointRes}}
# endregion api




# endregion code

