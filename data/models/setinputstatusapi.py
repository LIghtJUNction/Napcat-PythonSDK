# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/226659225e0
@llms.txt: https://napcat.apifox.cn/226659225e0.md
@last_update: 2025-04-27 00:53:40

@description: ## 状态列表

### 对方正在说话...
```json5
{ "event_type": 0 } 
```

### 对方正在输入...
```json5
{ "event_type": 1 } 
```



summary:设置输入状态

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.43"
__endpoint__ = "set_input_status"
__id__ = "226659225e0"
__method__ = "POST"

# endregion METADATA


# region code
import logging
from typing import Any
from pydantic import BaseModel, Field

logger = logging.getLogger(__name__)

# region req
class SetInputStatusReq(BaseModel): # type: ignore
    """
    {{DESC_EndPointReq}}
    """

    pass
# endregion req



# region res
class SetInputStatusRes(BaseModel): # type: ignore
    # 定义响应参数
    # 例如：
    # param1: str = Field(..., description="参数1的描述")
    # param2: int = Field(..., description="参数2的描述")
    
    pass
# endregion res

# region api
class SetInputStatusAPI(BaseModel):
    """set_input_status接口数据模型"""
    endpoint: str = "set_input_status"
    method: str = "POST"
    Req: type[BaseModel] = SetInputStatusReq
    Res: type[BaseModel] = SetInputStatusRes
# endregion api




# endregion code

