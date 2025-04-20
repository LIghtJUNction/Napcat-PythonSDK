# -*- coding: utf-8 -*-
"""
转存为永久文件 API
开发完毕
@作者：GitHub Copilot
@日期：2025/04/20
"""

from typing import Literal

from pydantic import ConfigDict, Field
from ..base.models import BaseHttpAPI, BaseHttpRequest, BaseHttpResponse, BaseModel


class Request(BaseHttpRequest):
    """
    转存为永久文件请求参数
    """
    file_id: str = Field(description="要转存的文件ID")
    file_name: str = Field(description="文件名称，包括后缀")


class ResponseData(BaseModel):
    """
    转存为永久文件响应数据模型
    """
    file_id: str = Field(default="", description="永久文件ID")
    file_name: str = Field(default="", description="文件名称")
    file_size: int = Field(default=0, description="文件大小(字节)")
    url: str = Field(default="", description="文件下载链接")
    success: bool = Field(default=False, description="是否转存成功")
    message: str = Field(default="", description="结果消息")
    
    model_config = ConfigDict(
        extra="allow",  # 允许额外字段
        frozen=False,   # 不冻结模型
        populate_by_name=True,  # 通过名称填充字段
        arbitrary_types_allowed=True,  # 允许任意类型
    )


class Response(BaseHttpResponse[ResponseData]):
    """
    转存为永久文件响应参数
    """
    pass


class SaveToPermanentAPI(BaseHttpAPI):
    """
    转存为永久文件 API
    用于将临时文件或其他文件转存为永久保存的文件
    接口地址: https://napcat.apifox.cn/226659183e0.md

    参数：
    {
      "file_id": "abcd-1234-efgh-5678",
      "file_name": "永久保存的文件名.txt"
    }

    返回：
    - 转存为永久文件的结果，包含文件ID、名称、下载链接等信息
    """

    api: str = "/save_to_permanent"
    method: Literal['POST', 'GET'] = "POST"
    request: BaseHttpRequest = Request()
    response: BaseHttpResponse[ResponseData] = Response()

if __name__ == "__main__":
    from ..base.utils import test_model
    # uv pip install -e . 
    # python -m napcat.api.file.save_to_permanent
    test_model(Request)
    test_model(ResponseData)
    test_model(Response)