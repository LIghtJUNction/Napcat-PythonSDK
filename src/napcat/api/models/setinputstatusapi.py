# -*- coding: utf-8 -*- 
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/226659225e0
@llms.txt: https://napcat.apifox.cn/226659225e0.md
@last_update: 2025-04-25 23:00:50

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
from pydantic import BaseModel, Field
import logging

logger = logging.getLogger(__name__)

# region component_models
class UserID(BaseModel):
    id: str | int = Field(description="标识ID")
    name: str | None = Field(default=None, description="名称")

    model_config = {
        "extra": "allow",
    }


class Result(BaseModel):
    status: str = Field(const='ok', description="status字段")
    retcode: float = Field(description="retcode字段")
    data: dict[str, any] = Field(description="data字段")
    message: str = Field(description="message字段")
    wording: str = Field(description="wording字段")
    echo: str | None = Field(default=None, description="echo字段")

    model_config = {
        "extra": "allow",
    }

# region component_models/

# region req
class SetInputStatusReq(BaseModel):
    """设置输入状态"""
    eventType: float = Field(description="事件类型")
    user_id: UserID = Field(description="用户ID")

    model_config = {
        "extra": "allow",
    }

# region req/


# region res
class SetInputStatusRes(BaseModel):
    """设置输入状态"""

    class ResponseData(BaseModel):
        """响应数据类型"""
        result: float = Field(description="result字段")
        errMsg: str = Field(description="errMsg字段")

        model_config = {
            "extra": "allow",
        }

    status: str = Field(default="ok", description="status字段")
    retcode: float = Field(default=0, description="retcode字段")
    data: ResponseData = Field(description="data字段")
    message: str = Field(default="", description="message字段")
    wording: str = Field(default="", description="wording字段")
    echo: str | None = Field(default=None, description="echo字段")

    model_config = {
        "extra": "allow",
    }

# region res/

# region api
class SetInputStatusAPI(BaseModel):
    """set_input_status接口数据模型"""
    endpoint: str = "set_input_status"
    method: str = "POST"
    Req: type[BaseModel] = SetInputStatusReq
    Res: type[BaseModel] = SetInputStatusRes
    logger = logging.getLogger(__name__)

    def __init__(self) -> None:
        super().__init__()
        self.logger.debug("初始化 SetInputStatusAPI")

    def __call__(self, req: SetInputStatusReq) -> SetInputStatusRes:
        """
        调用API的方法（仅作为接口定义，不包含实际请求逻辑）
        
        Args:
            req: 请求参数对象
            
        Returns:
            响应对象
        """
        # 调试日志
        self.logger.debug(f"调用 SetInputStatusAPI API")
        self.logger.debug(f"请求参数: {req.model_dump_json()}")

        # 注意：这里不应该包含实际的请求逻辑
        # 这个方法只是定义了接口，实际的请求应由适配器或客户端实现
        raise NotImplementedError("此方法需要由实际的API客户端实现")

# region api/
# region code/