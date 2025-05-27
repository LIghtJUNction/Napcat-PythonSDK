# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: 群聊相关
@homepage: https://napcat.apifox.cn/226658678e0
@llms.txt: https://napcat.apifox.cn/226658678e0.md
@last_update: 2025-05-28 01:34:09

@description:

summary:删除群精华消息

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.43"
__endpoint__ = "delete_essence_msg"
__id__ = "226658678e0"
__method__ = "POST"

# endregion METADATA


# region code
from pydantic import BaseModel, Field
from typing import Any, Literal

# region component_models
# 根据 OpenAPI 规范，message_id 是一个简单的标量类型（number 或 string），不是一个对象。
# result 组件在响应中被具体定义为内联对象，而非单独的共享组件。
# 因此，此处不需单独定义组件模型。
# endregion component_models/

# region req
class DeleteEssenceMsgReq(BaseModel):
    """删除群精华消息请求"""
    # OpenAPI spec: message_id 可以是数字或字符串。
    message_id: int | str = Field(description="要删除的群精华消息ID")

    model_config = {
        "extra": "allow",
    }
# endregion req/


# region res
class DeleteEssenceMsgRes(BaseModel):
    """删除群精华消息响应"""
    class ResultData(BaseModel):
        """data.result 字段的响应数据类型"""
        wording: str = Field(default="", description="正常为空，异常有文本提示")
        digestUin: str = Field(default="0", description="消息摘要的Uin") # OpenAPI 类型为 string，示例为 '0'
        digestTime: str = Field(default="0", description="消息摘要的时间戳") # OpenAPI 类型为 string，示例为 0
        msg: dict[str, Any] = Field(default_factory=dict, description="消息详情，空对象或包含详细消息内容")

        model_config = {
            "extra": "allow",
        }

    class Data(BaseModel):
        """data 字段的响应数据类型"""
        errCode: str = Field(default="0", description="错误码，0表示成功") # 示例为 '0'
        errMsg: str = Field(default="success", description="错误信息，success表示成功") # 示例为 'success'
        result: ResultData = Field(default_factory=ResultData, description="操作结果详情")

        model_config = {
            "extra": "allow",
        }

    status: Literal["ok"] = Field(default="ok", description="状态码，固定为 'ok'")
    retcode: float = Field(default=0.0, description="返回码，0表示成功")
    data: Data = Field(default_factory=Data, description="响应数据")
    message: str = Field(default="", description="消息提示")
    wording: str = Field(default="", description="文本提示")
    echo: str | None = Field(default=None, description="回显字段")

    model_config = {
        "extra": "allow",
    }
# endregion res/

# region api
class DeleteEssenceMsgAPI(BaseModel):
    """delete_essence_msg接口数据模型"""
    endpoint: str = "delete_essence_msg"
    method: str = "POST"
    Req: type[BaseModel] = DeleteEssenceMsgReq
    Res: type[BaseModel] = DeleteEssenceMsgRes

# endregion api/
# endregion code
