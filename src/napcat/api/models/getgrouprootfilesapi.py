# -*- coding: utf-8 -*- 
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/226658823e0
@llms.txt: https://napcat.apifox.cn/226658823e0.md
@last_update: 2025-04-25 23:00:49

@description: 

summary:获取群根目录文件列表

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "get_group_root_files"
__id__ = "226658823e0"
__method__ = "POST"

# region METADATA/


# region code
from pydantic import BaseModel, Field
import logging

logger = logging.getLogger(__name__)

# region component_models
class GroupId(BaseModel):
    id: str = Field(description="标识ID")
    name: str | None = Field(None, description="名称")

    model_config = {
        "extra": "allow",
    }


class Result(BaseModel):
    status: str = Field(description="status字段", default="ok")
    retcode: float = Field(description="retcode字段", default=0)
    data: dict[str, any] = Field(description="data字段", default_factory=dict)
    message: str = Field(description="message字段", default="")
    wording: str = Field(description="wording字段", default="")
    echo: str | None = Field(description="echo字段", default=None)

    model_config = {
        "extra": "allow",
    }
# region component_models/

# region req
class GetGroupRootFilesReq(BaseModel):
    """获取群根目录文件列表"""
    group_id: GroupId = Field(description="群组ID")
    file_count: float = Field(description="文件数量", default=50)

    model_config = {
        "extra": "allow",
    }
# region req/


# region res
class GetGroupRootFilesRes(BaseModel):
    """获取群根目录文件列表"""

    class FilesItem(BaseModel):
        group_id: int = Field(description="群组ID")
        file_id: str = Field(description="文件ID")
        file_name: str = Field(description="文件名")
        busid: int = Field(description="总线ID")
        size: int = Field(description="文件大小")
        upload_time: int = Field(description="上传时间")
        dead_time: int = Field(description="过期时间")
        modify_time: int = Field(description="修改时间")
        download_times: int = Field(description="下载次数")
        uploader: int = Field(description="上传者ID")
        uploader_name: str = Field(description="上传者名称")
        file_size: int = Field(description="文件大小")

        model_config = {
            "extra": "allow",
        }

    class FoldersItem(BaseModel):
        group_id: int = Field(description="群组ID")
        folder_id: str = Field(description="文件夹ID")
        folder: str = Field(description="文件夹路径")
        folder_name: str = Field(description="文件夹名称")
        create_time: int = Field(description="创建时间")
        creator: int = Field(description="创建人账号")
        creator_name: str = Field(description="创建人昵称")
        total_file_count: int = Field(description="文件数量")

        model_config = {
            "extra": "allow",
        }

    class ResponseData(BaseModel):
        """响应数据类型"""
        files: list[FilesItem] | None = Field(default=None, description="文件列表")
        folders: list[FoldersItem] | None = Field(default=None, description="文件夹列表")

        model_config = {
            "extra": "allow",
        }

    status: str = Field(default="ok", description="status字段")
    retcode: float = Field(default=0, description="retcode字段")
    data: ResponseData = Field(default_factory=ResponseData, description="data字段")
    message: str = Field(default="", description="message字段")
    wording: str = Field(default="", description="wording字段")
    echo: str | None = Field(default=None, description="echo字段")

    model_config = {
        "extra": "allow",
    }
# region res/

# region api
class GetGroupRootFilesAPI(BaseModel):
    """get_group_root_files接口数据模型"""
    endpoint: str = "get_group_root_files"
    method: str = "POST"
    Req: type[BaseModel] = GetGroupRootFilesReq
    Res: type[BaseModel] = GetGroupRootFilesRes
    logger = logging.getLogger(__name__)

    def __init__(self) -> None:
        super().__init__()
        self.logger.debug("初始化 GetGroupRootFilesAPI")

    def __call__(self, req: GetGroupRootFilesReq) -> GetGroupRootFilesRes:
        """
        调用API的方法（仅作为接口定义，不包含实际请求逻辑）
        
        Args:
            req: 请求参数对象
            
        Returns:
            响应对象
        """
        # 调试日志
        self.logger.debug(f"调用 GetGroupRootFilesAPI API")
        self.logger.debug(f"请求参数: {req.model_dump_json()}")
        
        # 注意：这里不应该包含实际的请求逻辑
        # 这个方法只是定义了接口，实际的请求应由适配器或客户端实现
        raise NotImplementedError("此方法需要由实际的API客户端实现")

# region api/
# region code/