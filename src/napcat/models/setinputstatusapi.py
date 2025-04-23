# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/226659225e0
@llms.txt: https://napcat.apifox.cn/226659225e0.md
@last_update: 2025-04-23 20:23:17

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
__version__ = "4.7.17"
__endpoint__ = "set_input_status"
__id__ = "226659225e0"
__method__ = "POST"

# region METADATA/


# region code
from typing import Any
from pydantic import BaseModel, Field
from typing import Union

# region req
class SetInputStatusReq(BaseModel):
    """
    请求参数
    """

    eventType: float = Field(..., description="")
    user_id: float | str = Field(..., description="")
# region req/


# region res
class SetInputStatusRes(BaseModel):
    """
    响应参数
    """

    result: float = Field(..., description="")
    errMsg: str = Field(..., description="")
# region res/

# region api
class SetInputStatusAPI(BaseModel):
    
    Request : type[SetInputStatusReq] = SetInputStatusReq
    Response  : type[SetInputStatusRes] = SetInputStatusRes


# region api/
# region code/

