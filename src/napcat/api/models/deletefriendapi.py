# -*- coding: utf-8 -*- 
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/227237873e0
@llms.txt: https://napcat.apifox.cn/227237873e0.md
@last_update: 2025-04-25 23:00:50

@description: 

summary:删除好友

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "delete_friend"
__id__ = "227237873e0"
__method__ = "POST"

# region METADATA/


# region code
from pydantic import BaseModel, Field


# region component_models

# region component_models/

# region req
class DeleteFriendReq(BaseModel):
    """删除好友"""
    user_id: str | int | None = Field(default=None, description="标识ID")
    friend_id: str | int | None = Field(default=None, description="好友ID")
    temp_block: bool = Field(..., description="拉黑")
    temp_both_del: bool = Field(..., description="双向删除")

    model_config = {
        "extra": "allow",
    }
# region req/


# region res
class DeleteFriendRes(BaseModel):
    """删除好友"""
    class ResponseData(BaseModel):
        """响应数据类型"""
        result: float = Field(..., description="result字段")
        errMsg: str = Field(..., description="errMsg字段")

        model_config = {
            "extra": "allow",
        }

    status: str = Field(default="ok", description="status字段")
    retcode: float = Field(default=0, description="retcode字段")
    data: ResponseData = Field(..., description="data字段")
    message: str = Field(default="", description="message字段")
    wording: str = Field(default="", description="wording字段")
    echo: str | None = Field(default=None, description="echo字段")

    model_config = {
        "extra": "allow",
    }
# region res/

# region api
class DeleteFriendAPI(BaseModel):
    """delete_friend接口数据模型"""
    endpoint: str = "delete_friend"
    method: str = "POST"
    Req: type[BaseModel] = DeleteFriendReq
    Res: type[BaseModel] = DeleteFriendRes

    def __call__(self, req: DeleteFriendReq) -> DeleteFriendRes:
        """
        调用API的方法（仅作为接口定义，不包含实际请求逻辑）
        
        Args:
            req: 请求参数对象
            
        Returns:
            响应对象
        """
        # 注意：这里不应该包含实际的请求逻辑
        # 这个方法只是定义了接口，实际的请求应由适配器或客户端实现
        raise NotImplementedError("此方法需要由实际的API客户端实现")

# region api/
# region code/