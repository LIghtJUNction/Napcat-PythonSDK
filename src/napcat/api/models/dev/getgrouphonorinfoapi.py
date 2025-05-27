from pydantic import BaseModel, Field
from typing import Literal

# region component_models
class GroupHonorInfo(BaseModel):
    user_id: float = Field(description="用户ID")
    nickname: str = Field(description="用户昵称")
    avatar: float = Field(description="用户头像")
    description: str = Field(description="说明")

    model_config = {
        "extra": "allow",
    }
# endregion component_models/

# region req
class GetGroupHonorInfoReq(BaseModel):
    """获取群荣誉请求"""
    group_id: int | str = Field(description="群ID，可以是数字或字符串")
    type: Literal["all", "talkative", "performer", "legend", "strong_newbie", "emotion"] | None = Field(
        default=None,
        description="荣誉类型，默认为all（所有），可选值：all, talkative, performer, legend, strong_newbie, emotion"
    )

    model_config = {
        "extra": "allow",
    }
# endregion req/


# region res
class GetGroupHonorInfoRes(BaseModel):
    """获取群荣誉响应"""
    class Data(BaseModel):
        """响应数据类型"""
        group_id: str = Field(description="群ID")
        current_talkative: GroupHonorInfo = Field(description="当前龙王")
        talkative_list: list[GroupHonorInfo] = Field(description="群聊之火列表")
        performer_list: list[GroupHonorInfo] = Field(description="群聊炽焰列表")
        legend_list: list[GroupHonorInfo] = Field(description="龙王列表")
        emotion_list: list[GroupHonorInfo] = Field(description="快乐源泉列表")
        strong_newbie_list: list[GroupHonorInfo] = Field(description="冒尖小春笋列表")

        model_config = {
            "extra": "allow",
        }

    status: Literal["ok"] = Field(default="ok", description="状态码")
    retcode: float = Field(default=0.0, description="返回码")
    data: Data = Field(default_factory=Data, description="响应数据")
    message: str = Field(default="", description="消息")
    wording: str = Field(default="", description="提示词")
    echo: str | None = Field(default=None, description="回显信息")

    model_config = {
        "extra": "allow",
    }
# endregion res/

# region api
class GetGroupHonorInfoAPI(BaseModel):
    """get_group_honor_info接口数据模型"""
    endpoint: str = "get_group_honor_info"
    method: str = "POST"
    Req: type[BaseModel] = GetGroupHonorInfoReq
    Res: type[BaseModel] = GetGroupHonorInfoRes

# endregion api/