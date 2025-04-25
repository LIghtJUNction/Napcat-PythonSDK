# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: 群聊相关
@homepage: https://napcat.apifox.cn/226656802e0
@llms.txt: https://napcat.apifox.cn/226656802e0.md
@last_update: 2025-04-26 01:17:44

@description: 

summary:全体禁言

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "set_group_whole_ban"
__id__ = "226656802e0"
__method__ = "POST"

# endregion METADATA


# region code
import logging
from typing import Literal
from pydantic import BaseModel, Field

logger = logging.getLogger(__name__)

# region req
class SetGroupWholeBanReq(BaseModel):
    """
    SetGroupWholeBan Endpoint Request Model
    """

    group_id: int | str = Field(..., description="群号")
    enable: bool = Field(..., description="是否设置，true 为设置，false 为取消")
# endregion req



# region res
class SetGroupWholeBanRes(BaseModel):
    """
    SetGroupWholeBan Endpoint Response Model
    """

    status: Literal["ok"] = Field("ok", description="状态")
    retcode: int = Field(..., description="返回码")
    data: None = Field(..., description="数据 (总是 null)")
    message: str = Field(..., description="消息")
    wording: str = Field(..., description="文案")
    echo: str | None = Field(None, description="Echo值")
# endregion res

# region api
class SetGroupWholeBanAPI(BaseModel):
    """set_group_whole_ban接口数据模型"""
    endpoint: str = "set_group_whole_ban"
    method: str = "POST"
    Req: type[BaseModel] = SetGroupWholeBanReq
    Res: type[BaseModel] = SetGroupWholeBanRes
# endregion api




# endregion code
