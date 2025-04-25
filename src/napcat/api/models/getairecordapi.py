# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/229486818e0
@llms.txt: https://napcat.apifox.cn/229486818e0.md
@last_update: 2025-04-25 23:00:50

@description: 获取AI语音

summary:获取AI语音

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "get_ai_record"
__id__ = "229486818e0"
__method__ = "POST"

# region METADATA/


# region code
from pydantic import BaseModel, Field
import logging

logger = logging.getLogger(__name__)

# region component_models
class GroupId(BaseModel):
    """标识ID和名称"""
    id: str = Field(description="标识ID")
    name: str | None = Field(default=None, description="名称")

    model_config = {
        "extra": "allow",
    }


# region component_models/

# region req
class GetAiRecordReq(BaseModel):
    """获取AI语音请求参数"""
    group_id: str | int = Field(description="标识ID")
    character: str = Field(description="character_id")
    text: str = Field(description="文本")

    model_config = {
        "extra": "allow",
    }


# region req/


# region res
class GetAiRecordRes(BaseModel):
    """获取AI语音响应"""
    status: str = Field(default="ok", description="status字段")
    retcode: float = Field(default=0, description="retcode字段")
    data: str = Field(description="链接")
    message: str = Field(default="", description="message字段")
    wording: str = Field(default="", description="wording字段")
    echo: str | None = Field(default=None, description="echo字段")

    model_config = {
        "extra": "allow",
    }

# region res/

# region api
class GetAiRecordAPI(BaseModel):
    """get_ai_record接口数据模型"""
    endpoint: str = "get_ai_record"
    method: str = "POST"
    Req: type[BaseModel] = GetAiRecordReq
    Res: type[BaseModel] = GetAiRecordRes
    logger = logging.getLogger(__name__)

    def __init__(self) -> None:
        super().__init__()
        self.logger.debug("初始化 GetAiRecordAPI")

    def __call__(self, req: GetAiRecordReq) -> GetAiRecordRes:
        """
        调用API的方法（仅作为接口定义，不包含实际请求逻辑）

        Args:
            req: 请求参数对象

        Returns:
            响应对象
        """
        # 调试日志
        self.logger.debug(f"调用 GetAiRecordAPI API")
        self.logger.debug(f"请求参数: {req.model_dump_json()}")

        # 注意：这里不应该包含实际的请求逻辑
        # 这个方法只是定义了接口，实际的请求应由适配器或客户端实现
        raise NotImplementedError("此方法需要由实际的API客户端实现")

# region api/
# region code/