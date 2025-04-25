# -*- coding: utf-8 -*- 
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/226658975e0
@llms.txt: https://napcat.apifox.cn/226658975e0.md
@last_update: 2025-04-25 23:00:49

@description: 获取机器人账号范围

summary: 获取机器人账号范围

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "get_robot_uin_range"
__id__ = "226658975e0"
__method__ = "POST"

# region METADATA/


# region code
from pydantic import BaseModel, Field
import logging

logger = logging.getLogger(__name__)

# region component_models
class UinRange(BaseModel):
    """Uin范围数据模型"""
    minUin: str = Field(..., description="最小Uin")
    maxUin: str = Field(..., description="最大Uin")


class ResultData(BaseModel):
    """结果数据模型"""
    __root__: list[UinRange]


class Result(BaseModel):
    """结果模型"""
    status: str = Field("ok", description="状态")
    retcode: float = Field(0, description="返回码")
    data: list[UinRange] = Field(default_factory=list, description="数据")
    message: str = Field("", description="消息")
    wording: str = Field("", description="提示语")
    echo: str | None = Field(None, description="回显")

# region component_models/

# region req
class GetRobotUinRangeReq(BaseModel):
    """获取机器人账号范围请求模型"""
    pass  # 没有请求参数

# region req/


# region res
class GetRobotUinRangeRes(BaseModel):
    """获取机器人账号范围响应模型"""
    status: str = Field("ok", description="status字段")
    retcode: float = Field(0, description="retcode字段")
    data: list[UinRange] = Field(default_factory=list, description="data字段")
    message: str = Field("", description="message字段")
    wording: str = Field("", description="wording字段")
    echo: str | None = Field(None, description="echo字段")

# region res/

# region api
class GetRobotUinRangeAPI(BaseModel):
    """get_robot_uin_range接口数据模型"""
    endpoint: str = "get_robot_uin_range"
    method: str = "POST"
    Req: type[BaseModel] = GetRobotUinRangeReq
    Res: type[BaseModel] = GetRobotUinRangeRes
    logger = logging.getLogger(__name__)

    def __init__(self) -> None:
        super().__init__()
        self.logger.debug("初始化 GetRobotUinRangeAPI")

    def __call__(self, req: GetRobotUinRangeReq) -> GetRobotUinRangeRes:
        """
        调用API的方法（仅作为接口定义，不包含实际请求逻辑）
        
        Args:
            req: 请求参数对象
            
        Returns:
            响应对象
        """
        # 调试日志
        self.logger.debug(f"调用 GetRobotUinRangeAPI API")
        self.logger.debug(f"请求参数: {req.model_dump_json()}")
        
        # 注意：这里不应该包含实际的请求逻辑
        # 这个方法只是定义了接口，实际的请求应由适配器或客户端实现
        raise NotImplementedError("此方法需要由实际的API客户端实现")

# region api/
# region code/