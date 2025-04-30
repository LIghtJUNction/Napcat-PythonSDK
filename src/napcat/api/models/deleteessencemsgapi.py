# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: 群聊相关
@homepage: https://napcat.apifox.cn/226658678e0
@llms.txt: https://napcat.apifox.cn/226658678e0.md
@last_update: 2025-04-27 00:53:40

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
from typing import Any
from pydantic import BaseModel, Field
from typing import Literal

# region req
class DeleteEssenceMsgReq(BaseModel):
    """
    删除群精华消息请求模型
    """

    message_id: int | str = Field(..., description="要删除的精华消息ID")

# endregion req



# region res
class DeleteEssenceMsgRes(BaseModel):
    """
    删除群精华消息响应模型
    """
    status: Literal["ok"] = Field("ok", description="状态码，固定为 'ok'")
    retcode: int = Field(..., description="返回码")
    data: "DeleteEssenceMsgRes.DeleteEssenceMsgResData" = Field(..., description="响应数据")
    message: str = Field(..., description="消息")
    wording: str = Field(..., description="提示信息")
    echo: str | None = Field(..., description="Echo回显")

    class DeleteEssenceMsgResData(BaseModel):
        """
        删除群精华消息响应数据模型
        """
        errCode: str = Field(..., description="错误码")
        errMsg: str = Field(..., description="错误信息")
        result: "DeleteEssenceMsgRes.DeleteEssenceMsgResData.DeleteEssenceMsgResResult" = Field(..., description="结果详情")

        class DeleteEssenceMsgResResult(BaseModel):
            """
            结果详情模型
            """
            wording: str = Field(..., description="正常为空，异常有文本提示")
            digestUin: str = Field(..., description="消化者Uin")
            digestTime: str = Field(..., description="消化时间")
            msg: "DeleteEssenceMsgRes.DeleteEssenceMsgResData.DeleteEssenceMsgResResult.DeleteEssenceMsgResMsg" = Field(..., description="消息详情")

            class DeleteEssenceMsgResMsg(BaseModel):
                """
                消息详情模型
                """
                groupCode: str = Field(..., description="群号")
                msgSeq: int = Field(..., description="消息seq")
                msgRandom: int = Field(..., description="消息random")
                msgContent: list[Any] = Field(..., description="消息内容列表")
                textSize: str = Field(..., description="文本大小")
                picSize: str = Field(..., description="图片大小")
                videoSize: str = Field(..., description="视频大小")
                senderUin: str = Field(..., description="发送者Uin")
                senderTime: int = Field(..., description="发送时间")
                addDigestUin: str = Field(..., description="添加精华消息操作者Uin")
                addDigestTime: int = Field(..., description="添加精华消息操作时间")
                startTime: int = Field(..., description="未知")
                latestMsgSeq: int = Field(..., description="未知")
                opType: int = Field(..., description="未知")

# endregion res

# region api
class DeleteEssenceMsgAPI(BaseModel):
    """delete_essence_msg接口数据模型"""
    endpoint: str = "delete_essence_msg"
    method: str = "POST"
    Req: type[BaseModel] = DeleteEssenceMsgReq
    Res: type[BaseModel] = DeleteEssenceMsgRes
# endregion api

# endregion code