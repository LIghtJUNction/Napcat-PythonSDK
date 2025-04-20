# -*- coding: utf-8 -*-
"""
HTTP Client
开发完毕
@作者：LIghtJUNction
@日期：2025/04/20
"""

from typing import Literal

from pydantic import ConfigDict, Field
from ..base.models import BaseHttpAPI, BaseHttpRequest, BaseHttpResponse, BaseModel



class Request(BaseHttpRequest):
    """
    获取好友列表请求参数
    """
    no_cache: bool = False  # 是否不使用缓存，默认为False


class RichBuffer(BaseModel):
    """
    好友列表数据模型
    """
    # 使用ConfigDict来定义模型的配置
    model_config = ConfigDict(
        extra="allow",  # 额外字段
        frozen=False,   
    )
    
   

class ResponseData(BaseModel):
    """
    好友列表数据模型
    """
    qid : str = Field(default="", description="QIO")
    longNick : str = Field(default="", description="个性签名")
    birthday_year : int = Field(default=0, description="出生年份")
    birthday_month : int = Field(default=0, description="出生月份")
    birthday_day : int = Field(default=0, description="出生日期")
    age : int = Field(default=0, description="年龄")
    sex: str = Field(default="", description="性别")
    eMail : str = Field(default="", description="电子邮件")
    phoneNum : str = Field(default="", description="电话号码")
    categoryId : int = Field(default=0, description="分类ID")
    richTime : int = Field(default=0, description="富文本时间")
    richBuffer : RichBuffer = Field(default=RichBuffer(), description="富文本缓冲区")
    uid : str = Field(default="", description="qq号")
    nin : str = Field(default="", description="昵称")
    nick : str = Field(default="", description="昵称")
    remark : str = Field(default="", description="备注")
    user_id : int | str = Field(default="", description="用户ID")  # 修改为同时支持整数和字符串类型
    nickName : str = Field(default="", description="昵称")
    level : int = Field(default=0, description="等级")
    model_config = ConfigDict(
        extra="allow",  # 允许额外字段
        frozen=False,    # 不冻结模型
        populate_by_name=True,  # 通过名称填充字段
        arbitrary_types_allowed=True,  # 允许任意类型
    )


class Response(BaseHttpResponse[list[ResponseData]]):
    """
    获取好友列表响应参数
    """
    
    pass


class GetFriendListAPI(BaseHttpAPI):
    """
    获取好友列表 API
    用于获取当前登录账号的好友列表信息
    接口地址: https://napcat.apifox.cn/226656976e0.md

    参数：
    {
      "no_cache": false
    }

    返回：
    - 好友列表，包含好友的QQ号、昵称等信息

    """

    api : str = "/get_friend_list"
    method : Literal['POST', 'GET'] = "POST"
    request: BaseHttpRequest = Request()
    response: BaseHttpResponse[list[ResponseData]] = Response()

if __name__ == "__main__":
    from ..base.utils import test_model
    # uv pip install -e . 
    # python -m napcat.api.account.get_friend_list
    test_model(Request)
    test_model(ResponseData)
    test_model(Response)

