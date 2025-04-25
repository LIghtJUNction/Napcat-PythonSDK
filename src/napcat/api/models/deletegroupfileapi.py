# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: 文件相关
@homepage: https://napcat.apifox.cn/226658755e0
@llms.txt: https://napcat.apifox.cn/226658755e0.md
@last_update: 2025-04-25 23:00:49

@description: 

summary:删除群文件

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "delete_group_file"
__id__ = "226658755e0"
__method__ = "POST"

# region METADATA/


# region code
from pydantic import BaseModel, Field
from typing import Any
import logging

logger = logging.getLogger(__name__)

# region component_models
class GroupId(BaseModel):
    id: str = Field(description="标识ID")
    name: str | None = Field(default=None, description="名称")

    model_config = {
        "extra": "allow",
    }

class Result(BaseModel):
    status: str = Field(default="ok", description="status字段")
    retcode: float = Field(default=0, description="retcode字段")
    data: dict[str, Any] = Field(description="data字段")
    message: str = Field(default="", description="message字段")
    wording: str = Field(default="", description="wording字段")
    echo: str | None = Field(default=None, description="echo字段")

    model_config = {
        "extra": "allow",
    }
# region component_models/

# region req
class DeleteGroupFileReq(BaseModel):
    """删除群文件"""
    group_id: str | int = Field(description="群ID, 可以是字符串或者数字")
    file_id: str = Field(description="文件ID")

    model_config = {
        "extra": "allow",
    }
# region req/


# region res
class DeleteGroupFileRes(BaseModel):
    """删除群文件"""

    class TransGroupFileResultResult(BaseModel):
        retCode: float = Field(description="返回代码")
        retMsg: str = Field(description="返回消息")
        clientWording: str = Field(description="客户端提示语")

    class TransGroupFileResult(BaseModel):
        result: DeleteGroupFileRes.TransGroupFileResultResult = Field(description="处理结果")
        successFileIdList: list[str] = Field(description="成功文件ID列表")
        failFileIdList: list[str] = Field(description="失败文件ID列表")

    class ResponseData(BaseModel):
        result: float = Field(description="结果")
        errMsg: str = Field(description="错误消息")
        transGroupFileResult: DeleteGroupFileRes.TransGroupFileResult = Field(description="文件处理结果")

    status: str = Field(default="ok", description="状态", const=True)
    retcode: float = Field(default=0, description="返回码")
    data: ResponseData = Field(description="数据")
    message: str = Field(default="", description="消息")
    wording: str = Field(default="", description="提示语")
    echo: str | None = Field(default=None, description="回声")

    model_config = {
        "extra": "allow",
    }

# region res/

# region api
class DeleteGroupFileAPI(BaseModel):
    """delete_group_file接口数据模型"""
    endpoint: str = Field(default="delete_group_file", description="Endpoint", const=True)
    method: str = Field(default="POST", description="Method", const=True)
    Req: type[BaseModel] = Field(default=DeleteGroupFileReq, description="Request Model", const=True)
    Res: type[BaseModel] = Field(default=DeleteGroupFileRes, description="Response Model", const=True)
    logger: logging.Logger = Field(default_factory=lambda: logging.getLogger(__name__), description="Logger", const=True)

    def __init__(self) -> None:
        super().__init__()
        self.logger.debug("初始化 DeleteGroupFileAPI")

    def __call__(self, req: DeleteGroupFileReq) -> DeleteGroupFileRes:
        """
        调用API的方法（仅作为接口定义，不包含实际请求逻辑）
        
        Args:
            req: 请求参数对象
            
        Returns:
            响应对象
        """
        # 调试日志
        self.logger.debug(f"调用 DeleteGroupFileAPI API")
        self.logger.debug(f"请求参数: {req.model_dump_json()}")
        
        # 注意：这里不应该包含实际的请求逻辑
        # 这个方法只是定义了接口，实际的请求应由适配器或客户端实现
        raise NotImplementedError("此方法需要由实际的API客户端实现")

# region api/
# region code/