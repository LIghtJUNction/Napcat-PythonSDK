# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: 群聊相关
@homepage: https://napcat.apifox.cn/226658674e0
@llms.txt: https://napcat.apifox.cn/226658674e0.md
@last_update: 2025-04-26 01:17:44

@description: 

summary:设置群精华消息

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "set_essence_msg"
__id__ = "226658674e0"
__method__ = "POST"

# endregion METADATA


# region code
from typing import Any
from pydantic import BaseModel, Field

# region req
class SetEssenceMsgReq(BaseModel):
    """
    设置群精华消息 请求参数
    """
    message_id: int | str = Field(..., description="消息ID")
# endregion req



# region res
class SetEssenceMsgRes(BaseModel):
    """
    设置群精华消息 响应参数
    """


    class Data(BaseModel):
        """
        响应数据
        """
        class Result(BaseModel):
            """
            结果数据
            """
            class Msg(BaseModel):
                groupCode : str = Field(..., description="群号")
                msgSeq : int = Field(..., description="消息序列号")
                msgRandom : int = Field(..., description="消息随机数")
                msgContent : list[Any] = Field(..., description="消息内容")
                textSize : str = Field("0", description="文本大小")
                picSize : str = Field("0", description="图片大小")
                videoSize : str = Field("0", description="视频大小")
                senderUin : str = Field("0", description="发送者QQ号")
                senderTime : int = Field(0, description="发送时间")
                addDigestUin : str = Field("0", description="添加摘要QQ号")
                addDigestTime : int = Field(0, description="添加摘要时间")
                startTime : int = Field(0, description="开始时间")
                latestMsgSeq : int = Field(0, description="最新消息序列号")
                opType : int = Field(0, description="操作类型")


            wording : str = Field(..., description="文字")
            digestUin : str = Field("0", description="摘要QQ号")
            digestTime : int = Field(0, description="摘要时间")
            msg : Msg = Field(..., description="消息")
            errorCode : int = Field(0, description="错误码")

        result: Result = Field(..., description="结果")
        err_msg: str = Field(..., description="错误信息")
        err_code: int = Field(..., description="错误码")
 

    status: str = Field(..., description="状态, 总是 'ok'")
    retcode: int = Field(..., description="返回码")
    data: Data = Field(..., description="响应数据")
    message: str = Field(..., description="信息")
    wording: str = Field(..., description="文字")
    echo: str | None = Field(None, description="回显数据")
# endregion res

# region api
class SetEssenceMsgAPI(BaseModel):
    """set_essence_msg接口数据模型"""
    endpoint: str = "set_essence_msg"
    method: str = "POST"
    Req: type[BaseModel] = SetEssenceMsgReq
    Res: type[BaseModel] = SetEssenceMsgRes
# endregion api




# endregion code
