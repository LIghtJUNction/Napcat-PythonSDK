# -*- coding: utf-8 -*- 

"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/226659280e0
@llms.txt: https://napcat.apifox.cn/226659280e0.md
@last_update: 2025-04-25 23:00:50

@description: 

summary:获取packet状态

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "nc_get_packet_status"
__id__ = "226659280e0"
__method__ = "POST"

# region component_models
from pydantic import BaseModel, Field

# region component_models/

# region req
class NcGetPacketStatusReq(BaseModel):
    """获取packet状态"""
    pass  # 没有请求参数

    model_config = {
        "extra": "allow",
    }
# region req/


# region res
class NcGetPacketStatusRes(BaseModel):
    """获取packet状态"""

    status: str = Field(default='ok', description="status字段")
    retcode: float = Field(default=0.0, description="retcode字段")
    data: dict[str, any] | None = Field(default=None, description="data字段")
    message: str = Field(default="", description="message字段")
    wording: str = Field(default="", description="wording字段")
    echo: str | None = Field(default=None, description="echo字段")

    model_config = {
        "extra": "allow",
    }

class result(BaseModel):
    status: str = Field(default='ok', description="status字段")
    retcode: float = Field(default=0.0, description="retcode字段")
    data: dict[str, any] | None = Field(default=None, description="data字段")
    message: str = Field(default="", description="message字段")
    wording: str = Field(default="", description="wording字段")
    echo: str | None = Field(default=None, description="echo字段")

    model_config = {
        "extra": "allow",
    }
# region res/

# region api
class NcGetPacketStatusAPI(BaseModel):
    """nc_get_packet_status接口数据模型"""
    endpoint: str = "nc_get_packet_status"
    method: str = "POST"
    Req: type[BaseModel] = NcGetPacketStatusReq
    Res: type[BaseModel] = result

    def __call__(self, req: NcGetPacketStatusReq) -> result:
        """
        调用API的方法（仅作为接口定义，不包含实际请求逻辑）
        
        Args:
            req: 请求参数对象
            
        Returns:
            响应对象
        """
        # 注意：这里不应该包含实际的请求逻辑
        # 这个方法只是定义了接口，实际的请求应由适配器或客户端实现
        # raise NotImplementedError("此方法需要由实际的API客户端实现")
        return result()

# region api/
