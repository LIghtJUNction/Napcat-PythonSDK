# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: 群聊相关
@homepage: https://napcat.apifox.cn/226657036e0
@llms.txt: https://napcat.apifox.cn/226657036e0.md
@last_update: 2025-04-27 00:53:40

@description: |
|  type                   |         类型                    |
|  ----------------- | ------------------------ |
| all                       |  所有（默认）             |
| talkative              | 群聊之火                     |
| performer           | 群聊炽焰                     |
| legend                | 龙王                             |
| strong_newbie   | 冒尖小春笋（R.I.P）     |
| emotion              | 快乐源泉                      |

summary:获取群荣誉

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.43"
__endpoint__ = "get_group_honor_info"
__id__ = "226657036e0"
__method__ = "POST"

# endregion METADATA


# region code
from pydantic import BaseModel, Field
from typing import Literal

# region req
class GetGroupHonorInfoReq(BaseModel):
    """
    获取群荣誉请求模型
    """

    group_id: int | str = Field(..., description="群号")
    type: str = Field("all", description="荣誉类型，可选值见description")
# endregion req



# region res
class GroupHonorInfo(BaseModel):
    """群荣誉信息"""

    user_id: int = Field(..., description="用户ID")
    nickname: str = Field(..., description="昵称")
    avatar: int = Field(..., description="头像ID")
    description: str = Field(..., description="说明")


class GetGroupHonorInfoRes(BaseModel):
    """
    获取群荣誉响应模型
    """

    class Data(BaseModel):
        """响应数据"""

        group_id: str = Field(..., description="群号")
        current_talkative: GroupHonorInfo = Field(..., description="当前龙王")
        talkative_list: list[GroupHonorInfo] = Field(..., description="群聊之火")
        performer_list: list[GroupHonorInfo] = Field(..., description="群聊炽焰")
        legend_list: list[GroupHonorInfo] = Field(..., description="龙王")
        emotion_list: list[GroupHonorInfo] = Field(..., description="快乐源泉")
        strong_newbie_list: list[GroupHonorInfo] = Field(..., description="冒尖小春笋")

    # 修正status字段的默认值和描述
    status: Literal["ok"] = Field("ok", description="状态码，固定为 'ok'")
    retcode: int = Field(..., description="响应码")
    data: Data = Field(..., description="响应数据")
    message: str = Field(..., description="响应消息")
    wording: str = Field(..., description="响应提示")
    echo: str | None = Field(default=None, description="echo")
# endregion res

# region api
class GetGroupHonorInfoAPI(BaseModel):
    """get_group_honor_info接口数据模型"""
    endpoint: str = "get_group_honor_info"
    method: str = "POST"
    Req: type[BaseModel] = GetGroupHonorInfoReq
    Res: type[BaseModel] = GetGroupHonorInfoRes
# endregion api




# endregion code