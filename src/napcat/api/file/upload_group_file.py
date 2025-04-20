# -*- coding: utf-8 -*-
"""
上传群文件 API
开发完毕
@作者：GitHub Copilot
@日期：2025/04/20
"""

from typing import Literal

from pydantic import ConfigDict, Field
from ..base.models import BaseHttpAPI, BaseHttpRequest, BaseHttpResponse, BaseModel


class Request(BaseHttpRequest):
    """
    上传群文件请求参数
    """
    group_id: int = Field(description="群号")
    file: str = Field(description="本地文件路径")
    name: str = Field(description="文件名称")
    folder: str = Field(default="", description="上传目录，默认为根目录")


class ResponseData(BaseModel):
    """
    上传群文件响应数据模型
    """
    file_id: str = Field(default="", description="文件ID")
    file_name: str = Field(default="", description="文件名称")
    file_size: int = Field(default=0, description="文件大小(字节)")
    busid: int = Field(default=0, description="文件总线ID")
    success: bool = Field(default=False, description="是否上传成功")
    message: str = Field(default="", description="结果消息")
    
    model_config = ConfigDict(
        extra="allow",  # 允许额外字段
        frozen=False,   # 不冻结模型
        populate_by_name=True,  # 通过名称填充字段
        arbitrary_types_allowed=True,  # 允许任意类型
    )


class Response(BaseHttpResponse[ResponseData]):
    """
    上传群文件响应参数
    """
    pass


class UploadGroupFileAPI(BaseHttpAPI):
    """
    上传群文件 API
    用于向群聊中上传文件
    接口地址: https://napcat.apifox.cn/226659182e0.md

    参数：
    {
      "group_id": 123456789,
      "file": "/path/to/local/file.txt",
      "name": "file.txt",
      "folder": "my_folder"  // 可选参数，默认为根目录
    }

    返回：
    - 上传群文件的结果，包含文件ID、名称、大小等信息
    """

    api: str = "/upload_group_file"
    method: Literal['POST', 'GET'] = "POST"
    request: BaseHttpRequest = Request()
    response: BaseHttpResponse[ResponseData] = Response()

if __name__ == "__main__":
    from ..base.utils import test_model
    # uv pip install -e . 
    # python -m napcat.api.file.upload_group_file
    test_model(Request)
    test_model(ResponseData)
    test_model(Response)