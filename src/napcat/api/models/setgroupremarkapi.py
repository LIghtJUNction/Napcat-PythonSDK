# -*- coding: utf-8 -*- 

"""
@tags: 群聊相关
@homepage: https://napcat.apifox.cn/283136268e0
@llms.txt: https://napcat.apifox.cn/283136268e0.md
@last_update: 2025-04-25 23:00:50

@description: 

summary:设置群备注

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "set_group_remark"
__id__ = "283136268e0"
__method__ = "POST"


from pydantic import BaseModel, Field
import logging

logger = logging.getLogger(__name__)


class Result(BaseModel):
    """返回结果"""
    status: str = Field(default="ok", description="status字段")
    retcode: float = Field(default=0.0, description="retcode字段")
    data: dict[str, any] | None = Field(default=None, description="data字段")
    message: str = Field(default="", description="message字段")
    wording: str = Field(default="", description="wording字段")
    echo: str | None = Field(default=None, description="echo字段")

    model_config = {
        "extra": "allow",
    }


class SetGroupRemarkReq(BaseModel):
    """设置群备注请求参数"""
    group_id: str = Field(..., description="群ID")
    remark: str = Field(..., description="群备注")

    model_config = {
        "extra": "allow",
    }


class SetGroupRemarkRes(BaseModel):
    """设置群备注响应"""

    class ResponseData(BaseModel):
        """响应数据类型"""
        yes: bool = Field(default=True, description="是否可用")
        reason: str | None = Field(default=None, description="原因")

        model_config = {
            "extra": "allow",
        }

    status: str = Field(default="ok", description="status字段")
    retcode: float = Field(default=0.0, description="retcode字段")
    data: ResponseData | None = Field(default_factory=lambda: SetGroupRemarkRes.ResponseData(), description="data字段")
    message: str = Field(default="", description="message字段")
    wording: str = Field(default="", description="wording字段")
    echo: str | None = Field(default=None, description="echo字段")

    model_config = {
        "extra": "allow",
    }


class SetGroupRemarkAPI(BaseModel):
    """set_group_remark接口数据模型"""
    endpoint: str = "set_group_remark"
    method: str = "POST"
    Req: type[BaseModel] = SetGroupRemarkReq
    Res: type[BaseModel] = SetGroupRemarkRes
    logger = logging.getLogger(__name__)

    def __init__(self) -> None:
        super().__init__()
        self.logger.debug("初始化 SetGroupRemarkAPI")

    def __call__(self, req: SetGroupRemarkReq) -> SetGroupRemarkRes:
        """
        调用API的方法（仅作为接口定义，不包含实际请求逻辑）
        
        Args:
            req: 请求参数对象
            
        Returns:
            响应对象
        """
        # 调试日志
        self.logger.debug(f"调用 SetGroupRemarkAPI API")
        self.logger.debug(f"请求参数: {req.model_dump_json()}")
        
        # 注意：这里不应该包含实际的请求逻辑
        # 这个方法只是定义了接口，实际的请求应由适配器或客户端实现
        raise NotImplementedError("此方法需要由实际的API客户端实现")
