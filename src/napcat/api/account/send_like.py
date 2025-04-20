"""
点赞API
用于向指定QQ用户发送点赞，每天每个用户最多赞10次
接口地址: https://napcat.apifox.cn/226656933e0.md

参数：
- user_id: 被点赞的用户QQ号
- times: 点赞次数，默认为1，最大为10

返回：
- 点赞结果的状态信息

# NapCat 开发中
"""

from pydantic import BaseModel
from napcat.api.base.models import BaseHttpResponse

class SendLikeReq(BaseModel):
    """
    点赞API请求参数
    """
    user_id: int                # 被点赞的用户QQ号
    times: int | None = None        # 点赞次数，默认为1，最大为10

class LikeResult(BaseModel):
    """
    点赞结果的状态信息
    """
    success: bool               # 是否点赞成功
    message: str                # 结果消息

class SendLikeRes(BaseHttpResponse[LikeResult]):
    """
    点赞API响应参数
    """
    pass
