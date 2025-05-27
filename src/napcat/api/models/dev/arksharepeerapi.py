# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/226658965e0
@llms.txt: https://napcat.apifox.cn/226658965e0.md
@last_update: 2025-05-28 01:34:09

@description: 

summary:获取推荐好友/群聊卡片

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.43"
__endpoint__ = "ArkSharePeer"
__id__ = "226658965e0"
__method__ = "POST"

# endregion METADATA


# region code
from pydantic import BaseModel, Field
from typing import Literal
import logging

logger = logging.getLogger(__name__)

# region component_models
# Original user_id, group_id, and result component models were removed
# as they did not align with the OpenAPI specification's definition.
# region component_models/

# region req
class ArksharepeerReq(BaseModel):
    """获取推荐好友/群聊卡片"""
    # Based on OpenAPI spec, group_id and user_id are oneOf string, number.
    group_id: str | int | None = Field(None, description="和user_id二选一")
    user_id: str | int | None = Field(None, description="和group_id二选一")
    phoneNumber: str | None = Field(None, description="对方手机号")

    model_config = {
        "extra": "allow",
    }
# region req/


# region res
class ArksharepeerRes(BaseModel):
    """获取推荐好友/群聊卡片"""
    class Data(BaseModel):
        """响应数据类型"""
        # Based on OpenAPI spec, these fields are required and not nullable.
        errCode: float = Field(description="errCode字段")
        errMsg: str = Field(description="errMsg字段")
        arkJson: str = Field(description="卡片json")

        model_config = {
            "extra": "allow",
        }

    # Based on OpenAPI spec, status is a constant 'ok'.
    status: Literal["ok"] = Field(default="ok", description="status字段")
    retcode: float = Field(default=0.0, description="retcode字段")
    data: Data = Field(default_factory=Data, description="data字段")
    message: str = Field(default="", description="message字段")
    wording: str = Field(default="", description="wording字段")
    echo: str | None = Field(default=None, description="echo字段")

    model_config = {
        "extra": "allow",
    }
# region res/

# region api
class ArksharepeerAPI(BaseModel):
    """ArkSharePeer接口数据模型"""
    endpoint: str = "ArkSharePeer"
    method: str = "POST"
    Req: type[BaseModel] = ArksharepeerReq
    Res: type[BaseModel] = ArksharepeerRes

# region api/
# endregion code
