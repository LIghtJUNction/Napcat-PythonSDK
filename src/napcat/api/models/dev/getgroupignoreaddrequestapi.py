# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: 其他/bug
@homepage: https://napcat.apifox.cn/226659234e0
@llms.txt: https://napcat.apifox.cn/226659234e0.md
@last_update: 2025-05-28 01:34:10

@description: 

summary:获取被过滤的加群请求

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.43"
__endpoint__ = "get_group_ignore_add_request"
__id__ = "226659234e0"
__method__ = "POST"

# endregion METADATA


# region code
from pydantic import BaseModel, Field
from typing import Literal

# region req
class GetGroupIgnoreAddRequestReq(BaseModel):
    """获取被过滤的加群请求"""
    # 根据 OpenAPI 规范，该请求没有参数
    pass

    model_config = {
        "extra": "allow",
    }
# region req/


# region res
class GetGroupIgnoreAddRequestRes(BaseModel):
    """获取被过滤的加群请求响应"""
    class DataEntry(BaseModel):
        """响应数据列表中的单个条目"""
        request_id: int = Field(description="请求ID")
        invitor_uin: int = Field(description="邀请者UIN")
        invitor_nick: str | None = Field(default=None, description="邀请者昵称")
        group_id: int | None = Field(default=None, description="群ID")
        message: str | None = Field(default=None, description="消息")
        group_name: str | None = Field(default=None, description="群名称")
        checked: bool = Field(description="是否已检查")
        actor: int = Field(description="操作者")
        requester_nick: str | None = Field(default=None, description="请求者昵称")

        model_config = {
            "extra": "allow",
        }

    status: Literal["ok"] = Field(default="ok", description="状态，固定为 'ok'")
    retcode: float = Field(default=0.0, description="返回码")
    data: list[DataEntry] = Field(default_factory=list, description="被过滤的加群请求列表")
    message: str = Field(default="", description="消息")
    wording: str = Field(default="", description="补充说明")
    echo: str | None = Field(default=None, description="echo字段")

    model_config = {
        "extra": "allow",
    }
# region res/

# region api
class GetGroupIgnoreAddRequestAPI(BaseModel):
    """get_group_ignore_add_request接口数据模型"""
    endpoint: str = "get_group_ignore_add_request"
    method: str = "POST"
    Req: type[BaseModel] = GetGroupIgnoreAddRequestReq
    Res: type[BaseModel] = GetGroupIgnoreAddRequestRes

# region api/
# endregion code
