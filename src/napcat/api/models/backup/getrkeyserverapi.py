# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: 密钥相关
@homepage: https://napcat.apifox.cn/283136236e0
@llms.txt: https://napcat.apifox.cn/283136236e0.md
@last_update: 2025-04-26 01:17:45

@description: 

summary:获取rkey服务

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "get_rkey_server"
__id__ = "283136236e0"
__method__ = "POST"

# endregion METADATA


# region code
from typing import Literal
from pydantic import BaseModel, Field

# region req
class GetRkeyServerReq(BaseModel):
    """
    获取rkey服务请求模型
    请求体为空
    """

    pass
# endregion req



# region res
class GetRkeyServerRes(BaseModel):
    """
    获取rkey服务响应模型
    """

    class Data(BaseModel):
        """
        响应数据详情
        """
        private_rkey: str = Field(..., description="私人密钥")
        group_rkey: str = Field(..., description="群组密钥")
        expired_time: float = Field(..., description="过期时间戳")
        name: str = Field(..., description="名称")

    status: Literal["ok"] = Field(..., description="响应状态，固定为 'ok'")
    retcode: int = Field(..., description="返回码")
    data: Data = Field(..., description="响应数据详情")
    message: str = Field(..., description="消息")
    wording: str = Field(..., description="提示")
    echo: str | None = Field(None, description="回显信息，可能为null")

# endregion res

# region api
class GetRkeyServerAPI(BaseModel):
    """get_rkey_server接口数据模型"""
    endpoint: str = "get_rkey_server"
    method: str = "POST"
    Req: type[BaseModel] = GetRkeyServerReq
    Res: type[BaseModel] = GetRkeyServerRes
# endregion api




# endregion code
