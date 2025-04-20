"""
设置账号信息 API
用于设置当前登录账号的个人资料信息，可修改昵称、性别、生日、个性签名等基本信息
接口地址: https://napcat.apifox.cn/226657374e0.md

参数：
- nickname: 要设置的昵称(可选)
- gender: 性别，0为男，1为女，2为保密(可选)
- birthday: 生日，格式为YYYY-MM-DD(可选)
- signature: 个性签名(可选)
- location: 地区信息，如"中国 广东 深圳"(可选)
- description: 个人说明(可选)

返回：
- 设置结果的状态信息
"""

from typing import Literal
from pydantic import BaseModel
from napcat.api.base.models import BaseHttpResponse

# 性别类型
GenderType = Literal[0, 1, 2]  # 0男，1女，2保密

class SetQQProfileReq(BaseModel):
    """
    设置账号信息 API 请求参数
    所有字段均为可选
    """
    nickname: str | None = None         # 要设置的昵称
    gender: GenderType | None = None    # 性别
    birthday: str | None= None         # 生日，格式为YYYY-MM-DD
    signature: str | None= None        # 个性签名
    location: str | None= None         # 地区信息
    description: str | None= None      # 个人说明

class ProfileResult(BaseModel):
    """
    设置账号信息的结果信息
    """
    success: bool         # 是否设置成功
    message: str          # 结果消息

class SetQQProfileRes(BaseHttpResponse[ProfileResult]):
    """
    设置账号信息 API 响应参数
    """
    pass