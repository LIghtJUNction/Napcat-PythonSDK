# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/226658977e0
@llms.txt: https://napcat.apifox.cn/226658977e0.md
@last_update: 2025-04-25 22:54:09

@description: ## 状态列表

### 在线

```json5
{ "status": 10, "ext_status": 0, "battery_status": 0 } 
```

### Q我吧

```json5
{ "status": 60, "ext_status": 0, "battery_status": 0 } 
```

### 离开

```json5
{ "status": 30, "ext_status": 0, "battery_status": 0 } 
```

### 忙碌

```json5
{ "status": 50, "ext_status": 0, "battery_status": 0 } 
```

### 请勿打扰

```json5
{ "status": 70, "ext_status": 0, "battery_status": 0 } 
```

### 隐身

```json5
{ "status": 40, "ext_status": 0, "battery_status": 0 } 
```

### 听歌中

```json5
{ "status": 10, "ext_status": 1028, "battery_status": 0 } 
```

### 春日限定

```json5
{ "status": 10, "ext_status": 2037, "battery_status": 0 } 
```

### 一起元梦

```json5
{ "status": 10, "ext_status": 2025, "battery_status": 0 } 
```

### 求星搭子

```json5
{ "status": 10, "ext_status": 2026, "battery_status": 0 } 
```

### 被掏空

```json5
{ "status": 10, "ext_status": 2014, "battery_status": 0 } 
```

### 今日天气

```json5
{ "status": 10, "ext_status": 1030, "battery_status": 0 } 
```

### 我crash了

```json5
{ "status": 10, "ext_status": 2019, "battery_status": 0 } 
```

### 爱你

```json5
{ "status": 10, "ext_status": 2006, "battery_status": 0 } 
```

### 恋爱中

```json5
{ "status": 10, "ext_status": 1051, "battery_status": 0 } 
```

### 好运锦鲤

```json5
{ "status": 10, "ext_status": 1071, "battery_status": 0 } 
```

### 水逆退散

```json5
{ "status": 10, "ext_status": 1201, "battery_status": 0 } 
```

### 嗨到飞起

```json5
{ "status": 10, "ext_status": 1056, "battery_status": 0 } 
```

### 元气满满

```json5
{ "status": 10, "ext_status": 1058, "battery_status": 0 } 
```

### 宝宝认证

```json5
{ "status": 10, "ext_status": 1070, "battery_status": 0 } 
```

### 一言难尽

```json5
{ "status": 10, "ext_status": 1063, "battery_status": 0 } 
```

### 难得糊涂

```json5
{ "status": 10, "ext_status": 2001, "battery_status": 0 } 
```

### emo中

```json5
{ "status": 10, "ext_status": 1401, "battery_status": 0 } 
```

### 我太难了

```json5
{ "status": 10, "ext_status": 1062, "battery_status": 0 } 
```

### 我想开了

```json5
{ "status": 10, "ext_status": 2013, "battery_status": 0 } 
```

### 我没事

```json5
{ "status": 10, "ext_status": 1052, "battery_status": 0 } 
```

### 想静静

```json5
{ "status": 10, "ext_status": 1061, "battery_status": 0 } 
```

### 悠哉哉

```json5
{ "status": 10, "ext_status": 1059, "battery_status": 0 } 
```

### 去旅行

```json5
{ "status": 10, "ext_status": 2015, "battery_status": 0 } 
```

### 信号弱

```json5
{ "status": 10, "ext_status": 1011, "battery_status": 0 } 
```

### 出去浪

```json5
{ "status": 10, "ext_status": 2003, "battery_status": 0 } 
```

### 肝作业

```json5
{ "status": 10, "ext_status": 2012, "battery_status": 0 } 
```

### 学习中

```json5
{ "status": 10, "ext_status": 1018, "battery_status": 0 } 
```

### 搬砖中

```json5
{ "status": 10, "ext_status": 2023, "battery_status": 0 } 
```

### 摸鱼中

```json5
{ "status": 10, "ext_status": 1300, "battery_status": 0 } 
```

### 无聊中

```json5
{ "status": 10, "ext_status": 1060, "battery_status": 0 } 
```

### timi中

```json5
{ "status": 10, "ext_status": 1027, "battery_status": 0 } 
```

### 睡觉中

```json5
{ "status": 10, "ext_status": 1016, "battery_status": 0 } 
```

### 熬夜中

```json5
{ "status": 10, "ext_status": 1032, "battery_status": 0 } 
```

### 追剧中

```json5
{ "status": 10, "ext_status": 1021, "battery_status": 0 } 
```

### 我的电量

```json5
{ 
    "status": 10, 
    "ext_status": 1000,
    "battery_status": 0
}
```

summary:设置在线状态

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "set_online_status"
__id__ = "226658977e0"
__method__ = "POST"

# region METADATA/


# region code
from pydantic import BaseModel, Field
from typing import Any
import logging

logger = logging.getLogger(__name__)

# region component_models
class result(BaseModel):
    status: str = Field(description="status字段")
    retcode: float = Field(description="retcode字段")
    data: dict[str, Any] = Field(description="data字段")
    message: str = Field(description="message字段")
    wording: str = Field(description="wording字段")
    echo: str | None = Field(description="echo字段")

    model_config = {
        "extra": "allow",
    }
# region component_models/

# region req
class SetOnlineStatusReq(BaseModel):
    """设置在线状态"""
    status: float = Field(description="详情看顶部")
    extStatus: float = Field(description="详情看顶部")
    batteryStatus: float = Field(description="电量")

    model_config = {
        "extra": "allow",
    }
# region req/


# region res
class SetOnlineStatusRes(BaseModel):
    """设置在线状态"""
    class ResponseData(BaseModel):
        """响应数据类型"""
        yes: bool = Field(default=True, description="是否可用")
        reason: str | None = Field(default=None, description="原因")

        model_config = {
            "extra": "allow",
        }

    status: str = Field(default="ok", description="status字段")
    retcode: float = Field(default=0, description="retcode字段")
    data: ResponseData = Field(default_factory=lambda: ResponseData(), description="data字段")
    message: str = Field(default="", description="message字段")
    wording: str = Field(default="", description="wording字段")
    echo: str | None = Field(default=None, description="echo字段")

    model_config = {
        "extra": "allow",
    }
# region res/

# region api
class SetOnlineStatusAPI(BaseModel):
    """set_online_status接口数据模型"""
    endpoint: str = "set_online_status"
    method: str = "POST"
    Req: type[BaseModel] = SetOnlineStatusReq
    Res: type[BaseModel] = SetOnlineStatusRes
    logger = logging.getLogger(__name__)

    def __init__(self) -> None:
        super().__init__()
        self.logger.debug("初始化 SetOnlineStatusAPI")

    def __call__(self, req: SetOnlineStatusReq) -> SetOnlineStatusRes:
        """
        调用API的方法（仅作为接口定义，不包含实际请求逻辑）
        
        Args:
            req: 请求参数对象
            
        Returns:
            响应对象
        """
        # 调试日志
        self.logger.debug(f"调用 SetOnlineStatusAPI API")
        self.logger.debug(f"请求参数: {req.model_dump_json()}")
        
        # 注意：这里不应该包含实际的请求逻辑
        # 这个方法只是定义了接口，实际的请求应由适配器或客户端实现
        raise NotImplementedError("此方法需要由实际的API客户端实现")

# region api/
# region code/

