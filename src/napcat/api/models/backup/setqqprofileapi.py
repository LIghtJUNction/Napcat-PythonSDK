# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: 账号相关
@homepage: https://napcat.apifox.cn/226657374e0
@llms.txt: https://napcat.apifox.cn/226657374e0.md
@last_update: 2025-04-26 01:17:44

@description: 

summary:设置账号信息

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "set_qq_profile"
__id__ = "226657374e0"
__method__ = "POST"

# endregion METADATA


# region code
import logging
from pydantic import BaseModel, Field

logger = logging.getLogger(__name__)

# region req
class SetQqProfileReq(BaseModel):
    """
    设置账号信息请求体
    """
    nickname: str = Field(..., description="昵称")
    personal_note: str = Field(..., description="个性签名")
    sex: str = Field(..., description="性别")
# endregion req



# region res
class SetQqProfileRes(BaseModel):
    """
    设置账号信息响应体
    """
    class Data(BaseModel):
        """
        数据
        """
        result: float = Field(..., description="结果")
        errMsg: str = Field(..., description="错误信息")

    status: str = Field(..., description="状态", pattern="^ok$") # 状态 (ok)
    retcode: float = Field(..., description="返回码") # 返回码
    data: Data = Field(..., description="数据") # 数据
    message: str = Field(..., description="消息") # 消息
    wording: str = Field(..., description="文字说明") # 文字说明
    echo: str | None = Field(None, description="回显") # 回显
# endregion res

# region api
class SetQqProfileAPI(BaseModel):
    """set_qq_profile接口数据模型"""
    endpoint: str = "set_qq_profile"
    method: str = "POST"
    Req: type[BaseModel] = SetQqProfileReq
    Res: type[BaseModel] = SetQqProfileRes
# endregion api




# endregion code