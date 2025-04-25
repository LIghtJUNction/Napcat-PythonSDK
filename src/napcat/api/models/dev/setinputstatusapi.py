# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: 
@homepage: https://napcat.apifox.cn/226659225e0
@llms.txt: https://napcat.apifox.cn/226659225e0.md
@last_update: 2025-04-26 01:17:45

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

# endregion METADATA


# region code
import logging
from pydantic import BaseModel, Field
from pydantic import AliasGenerator # Import AliasGenerator for camelCase conversion

logger = logging.getLogger(__name__)

# region req
class SetInputStatusReq(BaseModel):
    """
    设置输入状态请求模型
    """
    # Pydantic V2 AliasGenerator to convert camelCase (eventType) to snake_case (event_type)
    model_config = {
        "alias_generator": AliasGenerator(
            validation_alias='eventType',
            serialization_alias='eventType'
        )
    }

    # eventType: number (int or float likely), required
    event_type: int | float = Field(..., description="状态类型，0为正在说话，1为正在输入")

    # user_id: number or string, required
    user_id: int | str = Field(..., description="用户ID")
# endregion req



# region res
class SetInputStatusRes(BaseModel):
    """
    设置输入状态响应模型
    """
    # Nested model for the 'data' field
    class Data(BaseModel):
        result: int | float = Field(..., description="操作结果") # number in spec
        errMsg: str = Field(..., description="错误信息")

    status: str = Field("ok", description="状态，永远是ok")
    retcode: int = Field(..., description="返回码")
    data: Data = Field(..., description="响应数据") # Use the nested Data model
    message: str = Field(..., description="消息")
    wording: str = Field(..., description="文本描述")
    echo: str | None = Field(None, description="回显，可能为空") # nullable: true in spec, default None

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
