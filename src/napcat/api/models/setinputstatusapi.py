# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: 
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
from pydantic import BaseModel, Field
from typing import Literal

# region req
class SetInputStatusReq(BaseModel):
    """
    设置输入状态请求模型
    """

    user_id: int | str = Field(
        ..., description="用户ID，可以是数字或字符串"
    )
    event_type: int = Field(
        ..., description="输入状态类型，0: 正在说话, 1: 正在输入"
    )

# endregion req



# region res
class SetInputStatusRes(BaseModel):
    """
    设置输入状态响应模型
    """
    status: Literal["ok"] = Field("ok", description="状态码，固定为 'ok'")
    retcode: int = Field(..., description="返回码")
    message: str = Field(..., description="消息")
    wording: str = Field(..., description="提示信息")
    echo: str | None = Field(None, description="Echo字段，可能为空")

    class Data(BaseModel):
        """
        响应数据详情
        """
        result: int = Field(..., description="结果")
        errMsg: str = Field(..., description="错误消息")

    data: Data = Field(..., description="响应数据")

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