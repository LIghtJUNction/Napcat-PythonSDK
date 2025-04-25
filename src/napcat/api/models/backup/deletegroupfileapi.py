# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: 文件相关
@homepage: https://napcat.apifox.cn/226658755e0
@llms.txt: https://napcat.apifox.cn/226658755e0.md
@last_update: 2025-04-26 01:17:44

@description: 

summary:删除群文件

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "delete_group_file"
__id__ = "226658755e0"
__method__ = "POST"

# endregion METADATA


# region code
import logging
from pydantic import BaseModel, Field

logger = logging.getLogger(__name__)

# region req
class DeleteGroupFileReq(BaseModel):
    """
    删除群文件请求模型
    """

    group_id: int | str = Field(
        ..., description="群号 (oneOf number/string)"
    )
    file_id: str = Field(..., description="群文件ID")

# endregion req



# region res
class TransGroupFileResultResult(BaseModel):
    """
    群文件操作结果详情
    """
    retCode: int = Field(..., description="返回码")
    retMsg: str = Field(..., description="返回信息")
    clientWording: str = Field(..., description="客户端提示")


class TransGroupFileResult(BaseModel):
    """
    群文件批量操作结果
    """
    result: TransGroupFileResultResult = Field(..., description="操作结果")
    successFileIdList: list[str] = Field(..., description="成功删除的文件ID列表")
    failFileIdList: list[str] = Field(..., description="失败删除的文件ID列表")


class DeleteGroupFileData(BaseModel):
    """
    删除群文件响应数据
    """
    result: int = Field(..., description="结果码")
    errMsg: str = Field(..., description="错误信息")
    transGroupFileResult: TransGroupFileResult = Field(..., description="批量操作结果")


class DeleteGroupFileRes(BaseModel):
    """
    删除群文件响应模型
    """

    status: str = Field(
        ..., description="响应状态", pattern="^ok$"
    ) # Assuming 'ok' is the only valid status
    retcode: int = Field(..., description="响应码")
    data: DeleteGroupFileData = Field(..., description="响应数据")
    message: str = Field(..., description="响应消息")
    wording: str = Field(..., description="响应提示")
    echo: str | None = Field(None, description="回显数据")

# endregion res

# region api
class DeleteGroupFileAPI(BaseModel):
    """delete_group_file接口数据模型"""
    endpoint: str = "delete_group_file"
    method: str = "POST"
    Req: type[BaseModel] = DeleteGroupFileReq
    Res: type[BaseModel] = DeleteGroupFileRes
# endregion api




# endregion code
