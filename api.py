# -*- coding: utf-8 -*-
"""
@author: LIghtJUNction
@builder: {{builder}} # 构建者名称 如果启用AI 则为传入参数 如空，默认为AI

@build_id: {{build_id}} # 构建id 
@api_id: {{api_id}} # API api_id 结尾应当为e0
@endpoint: {{endpoint}} # 终结点名称 读取对应json文件时的键名
@tags: {{tags}} # 标签 也就是相对路径 
@homepage: {{homepage}} # base_url/api_id 其中base_url固定为https://api.napcat.com/
@llms.txt: {{llms.txt}} # base_url/api_id.md
@version: {{version}} # 版本号 由根目录的.version 正则匹配得到
@last_update: {{last_update}} # 最后更新时间 构建时的时间

@description: {{description}} # 描述  特殊元数据 AI可修改
@usage: {{usage}} # 使用说明 特殊元数据 AI可修改     

"""
# region METADATA

__author__ = "LIghtJUNction"
__version__ = "{{version}}" # API版本 # type: ignore
__endpoint__ = "{{endpoint}}" # 终结点名称
__method__ = "POST" # HTTP请求方法


# region {
from typing import Literal, Any # 使用现代导入方式，禁止导入List, Dict等过时类型

from pydantic import BaseModel, Field # 固定导入 # type: ignore
from napcat.base.models import BaseHttpAPI, BaseHttpResponse, BaseHttpRequest # 固定导入 # type: ignore

    # 示例 endpoint : send_group_message  特殊 endpoint : _开头 .开头 给类命名时 .忽略即可(如 _get_model_show -> GetModelShowAPI)
    # 示例 class : SendGroupMessageAPI
    # 示例 request : SendGroupMessageReq
    # 示例 response : SendGroupMessageRes
    # 示例 data : SendGroupMessageData
    # 请将你需要展示给用户的注释符："#"放置于行首
    # 否则将被清理掉


# request model
class {{EndPointReq}}(BaseHttpRequest): # type: ignore
    """
    {{DESC_EndPointReq}}
    """

    pass


class {{EndPointData}}(BaseModel): # type: ignore
    """
    {{DESC_EndPointData}}
    """
    # 定义可选数据字段
    # 例如：
    # param1: str = Field(..., description="参数1的描述")
    # param2: int = Field(..., description="参数2的描述")
    
    pass


# response model
class {{EndPointRes}}(BaseHttpResponse[{{*[EndPointData]}}]): # type: ignore
    """
    {{DESC_EndPointRes}}
    """
    # 定义响应参数
    # 例如：
    # param1: str = Field(..., description="参数1的描述")
    # param2: int = Field(..., description="参数2的描述")
    
    pass


# API class
class {{EndPointAPI}}(BaseHttpAPI[{{EndPointReq}}, {{EndPointRes}}]):
    """
    {{DESC_EndPointAPI}}
    """
    api: str = "/{{endpoint}}"
    method: Literal["POST", "GET"] = "{{METHOD}}"  # HTTP请求方法

    Request = {{EndPointReq}}
    Response = {{EndPointRes}}

    request: {{EndPointReq}}
    response: {{EndPointRes}}
    

if __name__ == "__main__": # type: ignore

    from napcat.base.utils import test_model
    test_model({{EndPointAPI}})

# region }

