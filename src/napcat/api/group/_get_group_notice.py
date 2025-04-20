"""
获取群公告 API
用于获取指定群的公告列表
接口地址: https://napcat.apifox.cn/227380871e0.md

参数：
- group_id: 群号

返回：
- 群公告列表，包含公告内容、发布者信息等

# NapCat 开发中
"""

from pydantic import BaseModel
from napcat.api.base.models import BaseHttpResponse

class GetGroupNoticeReq(BaseModel):
    """
    获取群公告 API 请求参数
    """
    group_id: int  # 群号

class NoticePublisher(BaseModel):
    """
    公告发布者信息
    """
    user_id: int   # 发布者QQ号
    nickname: str  # 发布者昵称

class GroupNotice(BaseModel):
    """
    群公告信息
    """
    notice_id: str          # 公告ID
    publisher: NoticePublisher  # 发布者信息
    title: str              # 公告标题
    content: str            # 公告内容
    time: int               # 发布时间
    is_top: bool            # 是否置顶
    is_all_confirm: bool    # 是否需要确认

class GetGroupNoticeRes(BaseHttpResponse[list[GroupNotice]]):
    """
    获取群公告 API 响应参数
    """
    pass