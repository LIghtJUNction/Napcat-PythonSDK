# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/226658755e0
@llms.txt: https://napcat.apifox.cn/226658755e0.md
@last_update: 2025-05-28 01:34:09

@description: 

summary:删除群文件

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.43"
__endpoint__ = "delete_group_file"
__id__ = "226658755e0"
__method__ = "POST"

# endregion METADATA


# region code
from pydantic import BaseModel, Field
from typing import Literal

# region req
class DeleteGroupFileReq(BaseModel):
    """删除群文件请求"""
    group_id: int | str = Field(..., description="群ID，可以是数字或字符串")
    file_id: str = Field(..., description="文件ID")

    model_config = {
        "extra": "allow",
    }
# region req/


# region res
class DeleteGroupFileRes(BaseModel):
    """删除群文件响应"""

    class Data(BaseModel):
        """响应数据类型"""

        class TransGroupFileResult(BaseModel):
            """文件传输结果"""

            class Result(BaseModel):
                """文件传输结果详情"""
                retCode: float = Field(..., description="返回码")
                retMsg: str = Field(..., description="返回消息")
                clientWording: str = Field(..., description="客户端提示信息")

                model_config = {
                    "extra": "allow",
                }

            result: Result = Field(..., description="文件传输结果详情")
            successFileIdList: list[str] = Field([], description="成功删除的文件ID列表")
            failFileIdList: list[str] = Field([], description="删除失败的文件ID列表")

            model_config = {
                "extra": "allow",
            }

        result: float = Field(..., description="操作结果")
        errMsg: str = Field(..., description="错误信息")
        transGroupFileResult: TransGroupFileResult = Field(..., description="群文件传输结果")

        model_config = {
            "extra": "allow",
        }

    status: Literal["ok"] = Field("ok", description="状态码")
    retcode: float = Field(0.0, description="返回码")
    data: Data = Field(default_factory=Data, description="响应数据")
    message: str = Field("", description="消息")
    wording: str = Field("", description="提示")
    echo: str | None = Field(None, description="echo字段")

    model_config = {
        "extra": "allow",
    }
# region res/

# region api
class DeleteGroupFileAPI(BaseModel):
    """delete_group_file接口数据模型"""
    endpoint: Literal["delete_group_file"] = "delete_group_file"
    method: Literal["POST"] = "POST"
    Req: type[BaseModel] = DeleteGroupFileReq
    Res: type[BaseModel] = DeleteGroupFileRes

    model_config = {
        "extra": "allow",
    }
# region api/
# endregion code
