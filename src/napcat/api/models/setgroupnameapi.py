# -*- coding: utf-8 -*- 
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/226656919e0
@llms.txt: https://napcat.apifox.cn/226656919e0.md
@last_update: 2025-04-25 23:00:49

@description: 

summary:设置群名

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "set_group_name"
__id__ = "226656919e0"
__method__ = "POST"

# region METADATA/


# region code
from pydantic import BaseModel, Field


# region req
class SetGroupNameReq(BaseModel):
    """设置群名"""
    group_id: str | int = Field(description="群组ID")
    group_name: str = Field(description="群组名称")

    model_config = {
        "extra": "allow",
    }
# region req/


# region res
class SetGroupNameRes(BaseModel):
    """设置群名"""

    status: str = Field(default="ok", description="status字段")
    retcode: float = Field(default=0, description="retcode字段")
    data: dict = Field(default={}, description="data字段, 默认为空对象")
    message: str = Field(default="", description="message字段")
    wording: str = Field(default="", description="wording字段")
    echo: str | None = Field(default=None, description="echo字段")

    model_config = {
        "extra": "allow",
    }
# region res/

# region api
class SetGroupNameAPI(BaseModel):
    """set_group_name接口数据模型"""
    endpoint: str = "set_group_name"
    method: str = "POST"
    Req: type[BaseModel] = SetGroupNameReq
    Res: type[BaseModel] = SetGroupNameRes

    def __call__(self, req: SetGroupNameReq) -> SetGroupNameRes:
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