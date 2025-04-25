# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/226657374e0
@llms.txt: https://napcat.apifox.cn/226657374e0.md
@last_update: 2025-04-25 23:00:49

@description: 

summary:设置账号信息

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "set_qq_profile"
__id__ = "226657374e0"
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
class SetQqProfileReq(BaseModel):
    """设置账号信息"""
    nickname: str = Field(description="昵称")
    personal_note: str = Field(description="个性签名")
    sex: str = Field(description="性别")

    model_config = {
        "extra": "allow",
    }
# region req/


# region res
class SetQqProfileRes(BaseModel):
    """设置账号信息"""
    class ResponseData(BaseModel):
        """响应数据类型"""
        result: float = Field(default=None, description="result字段")
        errMsg: str = Field(default=None, description="errMsg字段")

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
class SetQqProfileAPI(BaseModel):
    """set_qq_profile接口数据模型"""
    endpoint: str = "set_qq_profile"
    method: str = "POST"
    Req: type[BaseModel] = SetQqProfileReq
    Res: type[BaseModel] = SetQqProfileRes
    logger = logging.getLogger(__name__)

    def __init__(self) -> None:
        super().__init__()
        self.logger.debug("初始化 SetQqProfileAPI")

    def __call__(self, req: SetQqProfileReq) -> SetQqProfileRes:
        """
        调用API的方法（仅作为接口定义，不包含实际请求逻辑）
        
        Args:
            req: 请求参数对象
            
        Returns:
            响应对象
        """
        # 调试日志
        self.logger.debug(f"调用 SetQqProfileAPI API")
        self.logger.debug(f"请求参数: {req.model_dump_json()}")
        
        # 注意：这里不应该包含实际的请求逻辑
        # 这个方法只是定义了接口，实际的请求应由适配器或客户端实现
        raise NotImplementedError("此方法需要由实际的API客户端实现")

# region api/
# region code/

