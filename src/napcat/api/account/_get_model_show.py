# region GetModelShow
from typing import Literal
from pydantic import BaseModel, Field
from ..base.models import BaseHttpAPI, BaseHttpRequest, BaseHttpResponse




# region Request

class Request(BaseHttpRequest):
    """
    请求参数模型
    无需请求参数
    """
    model : str = Field(default="", description="机型名称")



# region Response
class Variant(BaseModel):
    """
    机型变体模型
    包含机型ID、机型名称和显示信息等
    """
    model_show : str = Field(default="", description="机型显示信息")
    need_pay : bool = Field(default=False, description="是否需要pay")


class ResponseData(BaseModel):
    """
    响应数据模型
    包含当前在线机型信息
    """
    # 使用List[Variant]确保它是Variant对象的列表
    variants: list[Variant] = Field(default_factory=list, description="机型变体列表")


class Response(BaseHttpResponse[ResponseData]):
    """
    响应模型
    包含响应状态、返回码、数据和消息等
    """
    pass

# region API

class GetModelShow(BaseHttpAPI):
    """
    获取在线机型 API
    用于获取当前账号设置的在线机型信息
    接口地址: https://napcat.apifox.cn/227233981e0.md

    参数：
    无需参数

    返回：
    - 当前在线机型信息，包含机型ID、机型名称和显示信息等
    """
    api : str = "/_get_model_show"  # API名称
    method : Literal["POST" , "GET"] = "POST"  # HTTP请求方法

    # 修正类属性的定义方式
    Request = Request  # 请求参数模型
    Response = Response  # 响应模型
    



__all__ = [
    "GetModelShow",
]


# region TEST
if __name__ == "__main__":
    from ..base.utils import test_model

    test_model(GetModelShow.Request)
    test_model(GetModelShow.Response)


