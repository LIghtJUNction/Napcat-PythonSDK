# -*- coding: utf-8 -*-
from typing import Generic, TypedDict , TypeVar

T = TypeVar('T')  # 定义一个类型变量，用于表示响应数据的具体类型

class BaseHttpResponse(TypedDict, Generic[T]):
    """
    API响应基类
    
    所有API响应的通用基类结构，包含标准字段
    具体API响应类型只需继承此类并定义特定的data字段类型
    """
    status: str     # "ok" 或 "error"
    retcode: int    # 0表示成功，其他值表示失败
    data: T         # 具体响应数据，类型由子类指定
    message: str    # 响应消息
    wording: str    # 响应文本
    echo: str       # 请求回显