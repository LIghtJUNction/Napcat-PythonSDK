# -*- coding: utf-8 -*-
"""
获取账号信息 API
开发完毕
@作者：GitHub Copilot
@日期：2025/04/20
"""

from typing import Literal

from pydantic import ConfigDict, Field
from ..base.models import BaseHttpAPI, BaseHttpRequest, BaseHttpResponse, BaseModel


class Request(BaseHttpRequest):
    """
    获取账号信息请求参数
    """
    # 此API不需要请求参数
    pass


class ResponseData(BaseModel):
    """
    账号信息数据模型
    """
    user_id: int = Field(default=0, description="QQ号")
    nickname: str = Field(default="", description="昵称")
    sex: str = Field(default="", description="性别")
    age: int = Field(default=0, description="年龄")
    qid: str = Field(default="", description="QID")
    level: int = Field(default=0, description="等级")
    login_days: int = Field(default=0, description="登录天数")
    signature: str = Field(default="", description="个性签名")
    mobile: str = Field(default="", description="绑定手机号")
    email: str = Field(default="", description="绑定邮箱")
    birthday: str = Field(default="", description="生日")
    
    model_config = ConfigDict(
        extra="allow",  # 允许额外字段
        frozen=False,   # 不冻结模型
        populate_by_name=True,  # 通过名称填充字段
        arbitrary_types_allowed=True,  # 允许任意类型
    )


class Response(BaseHttpResponse[ResponseData]):
    """
    获取账号信息响应参数
    """
    pass


class GetAccountInfoAPI(BaseHttpAPI):
    """
    获取账号信息 API
    用于获取当前登录QQ的详细账号信息
    接口地址: https://napcat.apifox.cn/226657369e0.md

    参数：
    无需参数

    返回：
    - 当前登录账号的详细信息，包括QQ号、昵称、性别、生日等
    """

    api: str = "/get_account_info"
    method: Literal['POST', 'GET'] = "GET"
    request: BaseHttpRequest = Request()
    response: BaseHttpResponse[ResponseData] = Response()

if __name__ == "__main__":
    from ..base.utils import test_model
    # uv pip install -e . 
    # python -m napcat.api.account.get_account_info
    test_model(Request)
    test_model(ResponseData)
    test_model(Response)