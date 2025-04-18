"""
客户端基础模块

提供NapcatClient的基本结构和功能实现
"""

import logging
from pydantic import BaseModel


logger = logging.getLogger(__name__)

class ClientBase(BaseModel):
    """
    Napcat客户端基类
    
    提供与API服务通信的基本功能，包括事件处理系统
    """
    pass