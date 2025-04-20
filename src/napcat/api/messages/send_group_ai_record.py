"""
发送群语音合成消息 API
用于向群发送AI合成语音
接口地址: https://napcat.apifox.cn/227229136e0.md

参数：
- group_id: 群号
- speaker: 语音合成发言人，ID格式为name-number
- text: 要合成的文本内容
- only_voice: 是否仅返回语音链接，不发送消息

返回：
- 发送结果或语音链接

# NapCat 开发中
"""

from pydantic import BaseModel
from napcat.api.base.models import BaseHttpResponse

class SendGroupAiRecordReq(BaseModel):
    """
    发送群语音合成消息 API 请求参数
    """
    group_id: int    # 群号
    speaker: str     # 语音合成发言人
    text: str        # 要合成的文本内容
    only_voice: bool # 是否仅返回语音链接

class AiRecordResult(BaseModel):
    """
    语音合成结果
    """
    voice_file: str  # 语音文件ID
    voice_url: str   # 语音下载链接
    message_id: int | None = None  # 消息ID，仅当only_voice=False时返回

class SendGroupAiRecordRes(BaseHttpResponse[AiRecordResult]):
    """
    发送群语音合成消息 API 响应参数
    """
    pass