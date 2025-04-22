# -*- coding: utf-8 -*-
"""
@author: LIghtJUNction
@builder: AI

@build_id: 214
@api_id: 226658883e0
@endpoint: upload_private_file
@tags: 文件相关
@homepage: https://napcat.apifox.cn/226658883e0
@llms.txt: https://napcat.apifox.cn/226658883e0.md
@version: 4.7.17
@last_update: 2025-04-23 04:39:51

@description: upload_private_file API
@usage: 使用 `client.upload_private_file()` 调用此API

"""
# region METADATA

__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "upload_private_file"
__method__ = "POST"


# region code
from typing import Literal, Any

from pydantic import BaseModel, Field
from napcat.base.models import BaseHttpAPI, BaseHttpResponse, BaseHttpRequest



# region req
class UploadPrivateFileReq(BaseHttpRequest):
    """
    upload_private_file 请求参数
    """

    pass
# region req/

# region data
class UploadPrivateFileData(BaseModel):
    """
    upload_private_file 数据结构
    """
    # 定义可选数据字段
    # 例如：
    # param1: str = Field(..., description="参数1的描述")
    # param2: int = Field(..., description="参数2的描述")
    
    pass
# region data/

# region res
class UploadPrivateFileRes(BaseHttpResponse[None]):
    """
    upload_private_file 响应参数
    """
    # 定义响应参数
    # 例如：
    # param1: str = Field(..., description="参数1的描述")
    # param2: int = Field(..., description="参数2的描述")
    
    pass
# region res/

# region api
class UploadPrivateFileAPI(BaseHttpAPI[UploadPrivateFileReq, UploadPrivateFileRes]):
    """
    上传私聊文件
    """
    api: str = "/upload_private_file"
    method: Literal["POST", "GET"] = "POST"

    Request = UploadPrivateFileReq
    Response = UploadPrivateFileRes

    request: UploadPrivateFileReq
    response: UploadPrivateFileRes
# region api/


if __name__ == "__main__":

    from napcat.base.utils import test_model
    test_model(UploadPrivateFileAPI)

# region code/

