# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/226657036e0
@llms.txt: https://napcat.apifox.cn/226657036e0.md
@last_update: 2025-05-28 01:34:09

@description: |  type                   |         类型                    |
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
from typing import Any
import logging

logger = logging.getLogger(__name__)

# region component_models
class group_id(BaseModel):
    id: str = Field(description="标识ID")
    name: str | None = Field(None, description="名称")

    model_config = {
        "extra": "allow",
    }

class result(BaseModel):
    status: str = Field(description="status字段")
    retcode: float = Field(description="retcode字段")
    data: dict[str, Any] = Field(description="data字段")
    message: str = Field(description="message字段")
    wording: str = Field(description="wording字段")
    echo: str | None = Field(description="echo字段")

    model_config = {
        "extra": "allow",
    }

class 群荣誉信息(BaseModel):
    user_id: float | None = Field(None, description="user_id字段")
    nickname: str | None = Field(None, description="nickname字段")
    avatar: float | None = Field(None, description="avatar字段")
    description: str | None = Field(None, description="说明")

    model_config = {
        "extra": "allow",
    }
# region component_models/

# region req
class GetGroupHonorInfoReq(BaseModel):
    """获取群荣誉"""
    group_id: group_id
    type: str | None = Field(None)

    model_config = {
        "extra": "allow",
    }
# region req/


# region res
class GetGroupHonorInfoRes(BaseModel):
    """获取群荣誉"""
    class Data(BaseModel):
        """响应数据类型"""
        group_id: str = Field(default=None, description="group_id字段")
        current_talkative: 群荣誉信息 = Field(default=None, description="当前龙王")
        talkative_list: list[群荣誉信息] = Field(default=None, description="群聊之火")
        performer_list: list[群荣誉信息] = Field(default=None, description="群聊炽焰")
        legend_list: list[群荣誉信息] = Field(default=None, description="龙王")
        emotion_list: list[群荣誉信息] = Field(default=None, description="快乐源泉")
        strong_newbie_list: list[群荣誉信息] = Field(default=None, description="冒尖小春笋")

        model_config = {
            "extra": "allow",
        }

    status: str = Field(default="ok", description="status字段")
    retcode: float = Field(default=0, description="retcode字段")
    data: Data = Field(default_factory=lambda: Data(), description="data字段")
    message: str = Field(default="", description="message字段")
    wording: str = Field(default="", description="wording字段")
    echo: str | None = Field(default=None, description="echo字段")

    model_config = {
        "extra": "allow",
    }
# region res/

# region api
class GetGroupHonorInfoAPI(BaseModel):
    """get_group_honor_info接口数据模型"""
    endpoint: str = "get_group_honor_info"
    method: str = "POST"
    Req: type[BaseModel] = GetGroupHonorInfoReq
    Res: type[BaseModel] = GetGroupHonorInfoRes

# region api/
# endregion code

