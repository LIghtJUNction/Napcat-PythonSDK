from pydantic import BaseModel, Field
from typing import Literal

# region req
class GetGuildListReq(BaseModel):
    """get_guild_list"""
    # 没有请求参数

    model_config = {
        "extra": "allow",
    }
# endregion req


# region res
class GetGuildListRes(BaseModel):
    """get_guild_list"""
    class Data(BaseModel):
        """响应数据类型"""
        yes: bool = Field(default=True, description="是否可用")
        reason: str | None = Field(default=None, description="原因")

        model_config = {
            "extra": "allow",
        }

    status: Literal["ok"] = Field(default="ok", description="状态，如 'ok'")
    retcode: float = Field(default=0.0, description="返回码，0表示成功")
    data: Data = Field(default_factory=Data, description="响应数据")
    message: str = Field(default="", description="消息")
    wording: str = Field(default="", description="文字描述")
    echo: str | None = Field(default=None, description="回显内容")

    model_config = {
        "extra": "allow",
    }
# endregion res

# region api
class GetGuildListAPI(BaseModel):
    """get_guild_list接口数据模型"""
    endpoint: str = "get_guild_list"
    method: str = "POST"
    Req: type[BaseModel] = GetGuildListReq
    Res: type[BaseModel] = GetGuildListRes
# endregion api