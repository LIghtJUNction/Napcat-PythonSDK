# -*- coding: utf-8 -*- 
# region METADATA
"""
@tags: 文件相关
@homepage: https://napcat.apifox.cn/226658865e0
@llms.txt: https://napcat.apifox.cn/226658865e0.md
@last_update: 2025-04-25 23:00:49

@description: 

summary:获取群子目录文件列表

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "get_group_files_by_folder"
__id__ = "226658865e0"
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
    retcode: float = Field(description="retcode字段")
    data: dict[str, Any] = Field(description="data字段")
    message: str = Field(description="message字段")
    wording: str = Field(description="wording字段")
    echo: str | None = Field(default=None, description="echo字段")

    model_config = {
        "extra": "allow",
    }
# region component_models/

# region req
class GetGroupFilesByFolderReq(BaseModel):
    """获取群子目录文件列表"""
    group_id: str = Field(description="标识ID")
    folder_id: str | None = Field(default=None, description="和 folder 二选一")
    folder: str | None = Field(default=None, description="和 folder_id 二选一")
    file_count: float | None = Field(default=50.0, description="一次性获取的文件数量")

    model_config = {
        "extra": "allow",
    }
# region req/


# region res
class GetGroupFilesByFolderRes(BaseModel):
    """获取群子目录文件列表"""

    class FilesItem(BaseModel):
        group_id: int = Field(description="群ID")
        file_id: str = Field(description="文件ID")
        file_name: str = Field(description="文件名")
        busid: int = Field(description="busid")
        size: int = Field(description="文件大小")
        upload_time: int = Field(description="上传时间")
        dead_time: int = Field(description="过期时间")
        modify_time: int = Field(description="修改时间")
        download_times: int = Field(description="下载次数")
        uploader: int = Field(description="上传者ID")
        uploader_name: str = Field(description="上传者名称")


    class FoldersItem(BaseModel):
        group_id: int = Field(description="群ID")
        folder_id: str = Field(description="文件夹ID")
        folder: str = Field(description="文件夹路径")
        folder_name: str = Field(description="文件夹名称")
        create_time: str = Field(description="创建时间")
        creator: str = Field(description="创建人账号")
        creator_name: str = Field(description="创建人昵称")
        total_file_count: str = Field(description="文件数量")

    class ResponseData(BaseModel):
        """响应数据类型"""
        files: list[FilesItem] = Field(default_factory=list, description="文件列表")
        folders: list[FoldersItem] = Field(default_factory=list, description="文件夹列表")

    status: str = Field(default="ok", description="status字段")
    retcode: float = Field(default=0.0, description="retcode字段")
    data: ResponseData = Field(default_factory=ResponseData, description="data字段")
    message: str = Field(default="", description="message字段")
    wording: str = Field(default="", description="wording字段")
    echo: str | None = Field(default=None, description="echo字段")

# region res/

# region api
class GetGroupFilesByFolderAPI(BaseModel):
    """get_group_files_by_folder接口数据模型"""
    endpoint: str = Field(default="get_group_files_by_folder", description="Endpoint")
    method: str = Field(default="POST", description="HTTP 方法")
    Req: type[BaseModel] = Field(default=GetGroupFilesByFolderReq, description="请求模型")
    Res: type[BaseModel] = Field(default=GetGroupFilesByFolderRes, description="响应模型")
    logger: logging.Logger = Field(default_factory=lambda: logging.getLogger(__name__), description="日志记录器")

    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self.logger.debug("初始化 GetGroupFilesByFolderAPI")

    def __call__(self, req: GetGroupFilesByFolderReq) -> GetGroupFilesByFolderRes:
        """
        调用API的方法（仅作为接口定义，不包含实际请求逻辑）
        
        Args:
            req: 请求参数对象
            
        Returns:
            响应对象
        """
        # 调试日志
        self.logger.debug(f"调用 GetGroupFilesByFolderAPI API")
        self.logger.debug(f"请求参数: {req.model_dump_json()}")
        
        # 注意：这里不应该包含实际的请求逻辑
        # 这个方法只是定义了接口，实际的请求应由适配器或客户端实现
        raise NotImplementedError("此方法需要由实际的API客户端实现")

# region api/
# region code/