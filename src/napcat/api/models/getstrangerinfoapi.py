# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: 账号相关
@homepage: https://napcat.apifox.cn/226656970e0
@llms.txt: https://napcat.apifox.cn/226656970e0.md
@last_update: 2025-04-27 00:53:40

@description:

summary:获取账号信息

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.43"
__endpoint__ = "get_stranger_info"
__id__ = "226656970e0"
__method__ = "POST"

# endregion METADATA


# region code
from pydantic import BaseModel, Field
from typing import Literal # Required for Literal type

# region req
class GetStrangerInfoReq(BaseModel):
    """
    {{DESC_EndPointReq}}
    """
    user_id: int | str = Field(..., description="用户ID")
# endregion req



# region res
class GetStrangerInfoRes(BaseModel):
    """
    {{DESC_EndPointRes}}
    """

    class Data(BaseModel):
        """
        响应数据
        """
        user_id: int = Field(..., description="用户ID")
        uid: str = Field(..., description="用户UID")
        uin: str = Field(..., description="用户UIN")
        nickname: str = Field(..., description="昵称")
        age: int = Field(..., description="年龄")
        qid: str = Field(..., description="QID")
        qqLevel: int = Field(..., description="账号等级")
        sex: str = Field(..., description="性别")
        long_nick: str = Field(..., description="个性签名")
        reg_time: int = Field(..., description="注册时间 (Unix timestamp)")
        is_vip: bool = Field(..., description="是否会员")
        is_years_vip: bool = Field(..., description="是否年费会员")
        vip_level: int = Field(..., description="会员等级")
        remark: str = Field(..., description="备注")
        status: int = Field(..., description="状态") # Note: This status is within data, different from top-level status
        login_days: int = Field(..., description="连续登录天数")

    status: Literal["ok"] = Field("ok", description="状态码，固定为 'ok'")
    retcode: int = Field(..., description="返回码")
    data: Data = Field(..., description="响应数据")
    message: str = Field(..., description="消息")
    wording: str = Field(..., description="提示")
    echo: str | None = Field(None, description="回显")

# endregion res

# region api
class GetStrangerInfoAPI(BaseModel):
    """get_stranger_info接口数据模型"""
    endpoint: str = "get_stranger_info"
    method: str = "POST"
    Req: type[BaseModel] = GetStrangerInfoReq
    Res: type[BaseModel] = GetStrangerInfoRes
# endregion api




# endregion code