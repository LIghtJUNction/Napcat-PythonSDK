# region GetModelShow
from typing import Any, Literal
from pydantic import BaseModel, Field
from ..base.models import BaseHttpAPI, BaseHttpRequest, BaseHttpResponse




# region Request

class Request(BaseHttpRequest):
    """
    请求参数模型
    无需请求参数
    """
    pass


class ResponseData(BaseModel):
    """
    响应数据模型
    包含当前在线机型信息
    """
    # 使用List[Variant]确保它是Variant对象的列表
    online : bool = Field(default=False, description="是否在线")
    good : bool = Field(default=False, description="是否良好")
    stat : dict[str, Any ] = Field(default_factory=dict, description="状态信息")

class Response(BaseHttpResponse[ResponseData]):
    """
    响应模型
    包含响应状态、返回码、数据和消息等
    """
    pass

# region API

class GetStatus(BaseHttpAPI):
    """
    获取账号状态 API
    用于查询当前账号的在线状态
    接口地址: https://napcat.apifox.cn/227233981e0.md

    参数：
    无需参数

    返回：
    - 在线状态、设备类型、最后在线时间等信息
    """

    api : str = "/get_status"  # API名称
    method : Literal["POST" , "GET"] = "POST"  # HTTP请求方法

    # 修正类属性的定义方式
    Request = Request  # 请求参数模型
    Response = Response  # 响应模型
    
    # 为了兼容性添加类方法获取request和response
    @classmethod
    def request(cls):
        return cls.Request
        
    @classmethod
    def response(cls):
        return cls.Response


__all__ = [
    "GetStatus",
]


# region TEST
if __name__ == "__main__":
    from ..base.utils import test_model

    test_model(GetStatus.Request)
    test_model(GetStatus.Response)

