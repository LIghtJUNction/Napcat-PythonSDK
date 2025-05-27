# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/226659240e0
@llms.txt: https://napcat.apifox.cn/226659240e0.md
@last_update: 2025-05-28 01:34:10

@description:

summary:_删除群公告

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.43"
__endpoint__ = "_del_group_notice"
__id__ = "226659240e0"
__method__ = "POST"

# endregion METADATA


# region code
from pydantic import BaseModel, Field
from typing import Literal # Import Literal for 'ok' constant

# The original 'group_id' and 'result' component classes are not used or are
# incorrectly defined based on the OpenAPI specification for this endpoint.
# The 'group_id' in the request body is a simple 'number | string' type.
# The 'result' schema's 'data' structure is specifically overridden in the response.

# region req
class DelGroupNoticeReq(BaseModel):
    """_删除群公告请求模型"""
    group_id: int | str = Field(description="群聊ID，可以是数字或字符串类型")
    notice_id: str = Field(description="要删除的群公告ID")

    model_config = {
        "extra": "allow",
    }
# region req/


# region res
class DelGroupNoticeRes(BaseModel):
    """_删除群公告响应模型"""
    class Data(BaseModel):
        """响应数据详情"""
        result: float = Field(description="操作结果，成功为0，失败为非0")
        errMsg: str = Field(description="错误信息描述")

        model_config = {
            "extra": "allow",
        }

    status: Literal["ok"] = Field("ok", description="响应状态，固定为 'ok'")
    retcode: float = Field(0.0, description="响应码，通常为0表示成功")
    data: Data = Field(description="响应数据体")
    message: str = Field("", description="响应消息")
    wording: str = Field("", description="响应提示语")
    echo: str | None = Field(None, description="echo字段，可能为空")

    model_config = {
        "extra": "allow",
    }
# region res/

# region api
class DelGroupNoticeAPI(BaseModel):
    """_del_group_notice接口数据模型"""
    endpoint: str = Field("_del_group_notice", description="API接口路径")
    method: str = Field("POST", description="HTTP请求方法")
    Req: type[BaseModel] = Field(DelGroupNoticeReq, description="请求数据模型")
    Res: type[BaseModel] = Field(DelGroupNoticeRes, description="响应数据模型")

# region api/
# endregion code
