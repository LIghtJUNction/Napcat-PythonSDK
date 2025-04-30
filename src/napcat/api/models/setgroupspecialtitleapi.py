# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/226656931e0
@llms.txt: https://napcat.apifox.cn/226656931e0.md
@last_update: 2025-04-27 00:53:40

@description: 

summary:设置群头衔

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.43"
__endpoint__ = "set_group_special_title"
__id__ = "226656931e0"
__method__ = "POST"

# endregion METADATA


# region code
from typing import Literal
from pydantic import BaseModel, Field

# region req
class SetGroupSpecialTitleReq(BaseModel):
    """
    设置群头衔请求模型
    """

    group_id: int | str = Field(..., description="群号")
    user_id: int | str = Field(..., description="用户号")
    special_title: str | None = Field(None, description="群头衔，为空则取消头衔")
# endregion req



# region res
class SetGroupSpecialTitleRes(BaseModel):
    """
    设置群头衔响应模型
    """

    status: Literal["ok"] = Field("ok", description="状态码，固定为 'ok'")
    retcode: int = Field(..., description="响应码")
    data: None = Field(..., description="响应数据")
    message: str = Field(..., description="消息")
    wording: str = Field(..., description="额外提示")
    echo: str | None = Field(..., description="回声")

# endregion res

# region api
class SetGroupSpecialTitleAPI(BaseModel):
    """set_group_special_title接口数据模型"""
    endpoint: str = "set_group_special_title"
    method: str = "POST"
    Req: type[BaseModel] = SetGroupSpecialTitleReq
    Res: type[BaseModel] = SetGroupSpecialTitleRes
# endregion api




# endregion code
