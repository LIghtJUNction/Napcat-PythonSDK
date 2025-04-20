# region SetOnlineStatus
from typing import Literal

from pydantic import Field
from ..base.models import BaseHttpAPI, BaseHttpRequest, BaseHttpResponse





class Request(BaseHttpRequest):
    """
    请求参数模型
    包含设置在线状态的参数
    """
    status: int = Field(default=10, description="在线状态代码")
    exit_status: int = Field(default=0, description="机型名称")
    battery_status: int = Field(default=0, description="电池状态")

class Response(BaseHttpResponse[None]):
    """
    响应模型
    包含响应状态、返回码、数据和消息等
    """
    pass

class SetOnlineStatus(BaseHttpAPI):
    """
    设置在线状态 API
    用于设置当前QQ账号的在线状态，如在线、离开、忙碌等
    接口地址: https://napcat.apifox.cn/226659187e0.md

    参数：
    - status: 在线状态代码，可选值包括 0(离线)、1(在线)、2(离开)、3(忙碌)、4(请勿打扰)、5(隐身)等

    返回：
    - 设置在线状态的结果信息
    """

    api : str = "/set_online_status"  # API名称
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
    
if __name__ == "__main__":
    from ..base.utils import test_model

    test_model(SetOnlineStatus.Request)
    test_model(SetOnlineStatus.Response)