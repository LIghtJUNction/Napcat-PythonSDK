# -*- coding: utf-8 -*- 
# region METADATA
"""
@tags: 文件相关
@homepage: https://napcat.apifox.cn/226658773e0
@llms.txt: https://napcat.apifox.cn/226658773e0.md
@last_update: 2025-04-25 23:00:49

@description: 创建群文件文件夹

summary:创建群文件文件夹

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "create_group_file_folder"
__id__ = "226658773e0"
__method__ = "POST"

# region METADATA/


# region code
from pydantic import BaseModel, Field
from typing import Any
import logging

logger = logging.getLogger(__name__)

# region component_models
class GroupId(BaseModel):
    id: str | int = Field(description="标识ID")
    name: str | None = Field(None, description="名称")

    model_config = {
        "extra": "allow",
    }

class Result(BaseModel):
    status: str = Field(default="ok", description="status字段")
    retcode: float = Field(description="retcode字段")
    data: dict[str, Any] = Field(default_factory=dict, description="data字段")
    message: str = Field(description="message字段")
    wording: str = Field(description="wording字段")
    echo: str | None = Field(None, description="echo字段")

    model_config = {
        "extra": "allow",
    }
# region component_models/

# region req
class CreateGroupFileFolderReq(BaseModel):
    """创建群文件文件夹"""
    group_id: str | int = Field(description="群组ID")
    folder_name: str = Field(description="文件夹名称")

    model_config = {
        "extra": "allow",
    }
# region req/


# region res
class CreateGroupFileFolderRes(BaseModel):
    """创建群文件文件夹"""
    class ResultData(BaseModel):
        """响应结果数据类型"""
        ret_code: float = Field(description="返回码")
        ret_msg: str = Field(description="返回消息")
        client_wording: str = Field(description="客户端提示语")

        model_config = {
            "extra": "allow",
        }

    class FolderInfo(BaseModel):
        """文件夹信息"""
        folder_id: str = Field(description="文件夹ID")
        parent_folder_id: str = Field(description="父文件夹ID")
        folder_name: str = Field(description="文件夹名称")
        create_time: int = Field(description="创建时间")
        modify_time: int = Field(description="修改时间")
        create_uin: str = Field(description="创建者UIN")
        creator_name: str = Field(description="创建者名称")
        total_file_count: str = Field(description="文件总数")
        modify_uin: str = Field(description="修改者UIN")
        modify_name: str = Field(description="修改者名称")
        used_space: str = Field(description="已用空间")

        model_config = {
            "extra": "allow",
        }

    class GroupItem(BaseModel):
        """群组项目"""
        peer_id: str = Field(description="群ID")
        type: str = Field(description="类型")
        folder_info: 'CreateGroupFileFolderRes.FolderInfo' = Field(description="文件夹信息")

        model_config = {
            "extra": "allow",
        }

    class ResponseData(BaseModel):
        """响应数据类型"""
        result: 'CreateGroupFileFolderRes.ResultData' = Field(description="result字段")
        group_item: 'CreateGroupFileFolderRes.GroupItem' = Field(description="groupItem字段")

        model_config = {
            "extra": "allow",
        }

    status: str = Field(default="ok", description="status字段")
    retcode: float = Field(default=0, description="retcode字段")
    data: 'CreateGroupFileFolderRes.ResponseData' = Field(description="data字段")
    message: str = Field(default="", description="message字段")
    wording: str = Field(default="", description="wording字段")
    echo: str | None = Field(default=None, description="echo字段")

    model_config = {
        "extra": "allow",
    }
# region res/

# region api
class CreateGroupFileFolderAPI(BaseModel):
    """create_group_file_folder接口数据模型"""
    endpoint: str = Field(default="create_group_file_folder", description="Endpoint")
    method: str = Field(default="POST", description="HTTP方法")
    Req: type[BaseModel] = Field(default=CreateGroupFileFolderReq, description="请求模型")
    Res: type[BaseModel] = Field(default=CreateGroupFileFolderRes, description="响应模型")
    logger: logging.Logger = Field(default_factory=lambda: logging.getLogger(__name__), description="Logger")

    def __init__(self) -> None:
        super().__init__()
        self.logger.debug("初始化 CreateGroupFileFolderAPI")

    def __call__(self, req: CreateGroupFileFolderReq) -> CreateGroupFileFolderRes:
        """
        调用API的方法（仅作为接口定义，不包含实际请求逻辑）
        
        Args:
            req: 请求参数对象
            
        Returns:
            响应对象
        """
        # 调试日志
        self.logger.debug(f"调用 CreateGroupFileFolderAPI API")
        self.logger.debug(f"请求参数: {req.model_dump_json()}")
        
        # 注意：这里不应该包含实际的请求逻辑
        # 这个方法只是定义了接口，实际的请求应由适配器或客户端实现
        raise NotImplementedError("此方法需要由实际的API客户端实现")

# region api/
# region code/
