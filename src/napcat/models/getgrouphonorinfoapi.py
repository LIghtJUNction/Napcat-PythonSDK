# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/226657036e0
@llms.txt: https://napcat.apifox.cn/226657036e0.md
@last_update: 2025-04-25 22:54:08

@description: 

summary:获取群荣誉

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "get_group_honor_info"
__id__ = "226657036e0"
__method__ = "POST"

# region METADATA/


# region code
from pydantic import BaseModel, Field
from typing import Any
import logging

logger = logging.getLogger(__name__)

# region component_models
class group_id(BaseModel):
    id: str = Field(description="标识ID")
    name: str | None = Field(None, description="名称")

    model_config = {
        "extra": "allow",
    }

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

class 龙王信息(BaseModel):
    user_id: float | None = Field(None, description="user_id字段")
    avatar: str | None = Field(None, description="头像")
    nickname: str | None = Field(None, description="nickname字段")
    day_count: float | None = Field(None, description="连续天数")
    description: str | None = Field(None, description="说明")

    model_config = {
        "extra": "allow",
    }
# region component_models/

# region req
class GetGroupHonorInfoReq(BaseModel):
    """获取群荣誉"""
    group_id: group_id

    model_config = {
        "extra": "allow",
    }
# region req/


# region res
class GetGroupHonorInfoRes(BaseModel):
    """获取群荣誉"""
    class ResponseData(BaseModel):
        """响应数据类型"""
        group_id: str = Field(default=None, description="group_id字段")
        current_talkative: 龙王信息 = Field(default=None, description="当前龙王")
        talkative_list: list[龙王信息] = Field(default=None, description="历史龙王列表")
        performer_list: list[PerformerListItem] = Field(default=None, description="群聊之火")
        legend_list: list[str] = Field(default=None, description="群聊炽焰")
        emotion_list: list[str] = Field(default=None, description="快乐之源")
        strong_newbie_list: list[str] = Field(default=None, description="冒尖小春笋")

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
class GetGroupHonorInfoAPI(BaseModel):
    """get_group_honor_info接口数据模型"""
    endpoint: str = "get_group_honor_info"
    method: str = "POST"
    Req: type[BaseModel] = GetGroupHonorInfoReq
    Res: type[BaseModel] = GetGroupHonorInfoRes
    logger = logging.getLogger(__name__)

    def __init__(self) -> None:
        super().__init__()
        self.logger.debug("初始化 GetGroupHonorInfoAPI")

    def __call__(self, req: GetGroupHonorInfoReq) -> GetGroupHonorInfoRes:
        """
        调用API的方法（仅作为接口定义，不包含实际请求逻辑）
        
        Args:
            req: 请求参数对象
            
        Returns:
            响应对象
        """
        # 调试日志
        self.logger.debug(f"调用 GetGroupHonorInfoAPI API")
        self.logger.debug(f"请求参数: {req.model_dump_json()}")
        
        # 注意：这里不应该包含实际的请求逻辑
        # 这个方法只是定义了接口，实际的请求应由适配器或客户端实现
        raise NotImplementedError("此方法需要由实际的API客户端实现")

# region api/
# region code/

