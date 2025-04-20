"""
设置群组专属头衔 API
用于设置群成员专属头衔
接口地址: https://napcat.apifox.cn/227425649e0.md

参数：
- group_id: 群号
- user_id: 用户QQ号
- special_title: 专属头衔，不填或空字符串表示删除专属头衔
- duration: 有效期，单位秒，-1表示永久，不过此项似乎没有效果

返回：
- 操作结果

# NapCat 开发中
"""

from pydantic import BaseModel
from napcat.api.base.models import BaseHttpResponse

class SetGroupSpecialTitleReq(BaseModel):
    """
    设置群组专属头衔 API 请求参数
    """
    group_id: int       # 群号
    user_id: int        # 用户QQ号
    special_title: str  # 专属头衔，不填或空字符串表示删除专属头衔
    duration: int       # 有效期，单位秒，-1表示永久，不过此项似乎没有效果

class SetGroupSpecialTitleRes(BaseHttpResponse[dict[str, bool]]):
    """
    设置群组专属头衔 API 响应参数
    """
    pass