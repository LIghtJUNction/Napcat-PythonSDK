# -*- coding: utf-8 -*-
"""
@author: LIghtJUNction
@builder: AI

@build_id: 214
@api_id: 226658753e0
@endpoint: upload_group_file
@tags: 文件相关
@homepage: https://napcat.apifox.cn/226658753e0
@llms.txt: https://napcat.apifox.cn/226658753e0.md
@version: 4.7.17
@last_update: 2025-04-23 04:39:51

@description: upload_group_file API
@usage: 使用 `client.upload_group_file()` 调用此API

"""
# region METADATA

__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "upload_group_file"
__method__ = "POST"


# region code
from typing import Literal, Any

from pydantic import BaseModel, Field
from napcat.base.models import BaseHttpAPI, BaseHttpResponse, BaseHttpRequest



# region req
class UploadGroupFileReq(BaseHttpRequest):
    """
    upload_group_file 请求参数
    """

    pass
# region req/

# region data
class UploadGroupFileData(BaseModel):
    """
    upload_group_file 数据结构
    """
    # 定义可选数据字段
    # 例如：
    # param1: str = Field(..., description="参数1的描述")
    # param2: int = Field(..., description="参数2的描述")
    
    pass
# region data/

# region res
class UploadGroupFileRes(BaseHttpResponse[None]):
    """
    upload_group_file 响应参数
    """
    # 定义响应参数
    # 例如：
    # param1: str = Field(..., description="参数1的描述")
    # param2: int = Field(..., description="参数2的描述")
    
    pass
# region res/

# region api
class UploadGroupFileAPI(BaseHttpAPI[UploadGroupFileReq, UploadGroupFileRes]):
    """
    上传群文件
    """
    api: str = "/upload_group_file"
    method: Literal["POST", "GET"] = "POST"

    Request = UploadGroupFileReq
    Response = UploadGroupFileRes

    request: UploadGroupFileReq
    response: UploadGroupFileRes
# region api/


if __name__ == "__main__":

    from napcat.base.utils import test_model
    test_model(UploadGroupFileAPI)

# region code/

