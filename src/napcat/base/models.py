from typing import Literal, TypeVar, Generic, Any, Type
from pydantic import BaseModel, Field, ConfigDict


# region HTTP API
Tdata = TypeVar('Tdata', bound=BaseModel)

class BaseHttpRequest(BaseModel):
    """所有HTTP请求模型的基类"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)
    

class BaseHttpResponse(BaseModel, Generic[Tdata]):
    """
    所有HTTP响应模型的基类，支持泛型数据字段
    
    支持将数据字段定义为任意类型，包括列表和自定义模型
    """
    status: str = Field(default="ok", description="响应状态，'ok'或'error'")
    retcode: int = Field(default=0, description="返回码，0表示成功，非0表示失败")
    data: Tdata | dict[str, Any] = Field(default_factory=dict, description="响应数据")
    message: str = Field(default="", description="响应消息")
    wording: str = Field(default="", description="响应提示文本")
    echo: str | None = Field(default=None, description="请求回显")
    
    model_config = ConfigDict(
        populate_by_name=True,
        extra="ignore",  # 忽略额外字段
    )
    

# 定义请求和响应类型的泛型参数，添加协变性
TReq = TypeVar('TReq', bound=BaseHttpRequest, covariant=True)
TRes = TypeVar('TRes', bound='BaseHttpResponse[Any]', covariant=True)

class BaseHttpAPI(Generic[TReq, TRes]):
    """
    HTTP API基类
    定义API的基本属性和行为
    """
    api: str = ""  # API路径
    method: Literal["POST", "GET"] = "GET"  # HTTP请求方法
    
    # 使用 Type 而不是 type，并提供正确的泛型参数
    Request: Type[TReq]  # 必须由子类提供
    Response: Type[TRes]  # 必须由子类提供

    request: TReq
    response: TRes
    
    def __init__(self) -> None:
        """初始化 API 实例"""
        self.request = self.Request()  # 创建请求实例
        self.response = self.Response()  # 创建响应实例


