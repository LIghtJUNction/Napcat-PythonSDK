# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: 个人操作
@homepage: https://napcat.apifox.cn/229486818e0
@llms.txt: https://napcat.apifox.cn/229486818e0.md
@last_update: 2025-04-27 00:53:41

@description: 

summary:获取AI语音

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.43"
__endpoint__ = "get_ai_record"
__id__ = "229486818e0"
__method__ = "POST"

# endregion METADATA


# region code
from typing import Literal
from pydantic import BaseModel, Field

# region req
class GetAiRecordReq(BaseModel):
    """
    获取AI语音 请求模型
    """
    group_id: int | str = Field(..., description="群号")
    character: str = Field(..., description="character_id")
    text: str = Field(..., description="文本")
# endregion req



# region res
class GetAiRecordRes(BaseModel):
    """
    获取AI语音 响应模型
    """
    status: Literal["ok"] = Field(..., description="状态")
    retcode: int = Field(..., description="返回码")
    data: str = Field(..., description="链接")
    message: str = Field(..., description="消息")
    wording: str = Field(..., description="文案")
    echo: str | None = Field(..., description="回显")
# endregion res

# region api
class GetAiRecordAPI(BaseModel):
    """get_ai_record接口数据模型"""
    endpoint: str = "get_ai_record"
    method: str = "POST"
    Req: type[BaseModel] = GetAiRecordReq
    Res: type[BaseModel] = GetAiRecordRes
# endregion api




# endregion code
