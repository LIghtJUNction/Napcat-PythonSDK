"""
删除精华消息 API
用于删除群精华消息
接口地址: https://napcat.apifox.cn/227425397e0.md

参数：
- message_id: 消息ID

返回：
- 删除操作结果

# NapCat 开发中
"""

from pydantic import BaseModel
from napcat.api.base.models import BaseHttpResponse

class DeleteEssenceMsgReq(BaseModel):
    """
    删除精华消息 API 请求参数
    """
    message_id: int  # 消息ID

class DeleteEssenceMsgRes(BaseHttpResponse[dict[str, bool]]):
    """
    删除精华消息 API 响应参数
    """
    pass