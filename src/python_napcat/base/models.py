"""
BaseModels
"""

import logging
from pydantic import BaseModel


logger = logging.getLogger(__name__)
# region ClientBase
class ClientBase(BaseModel):
    """
    Napcat客户端基类
    
    提供与API服务通信的基本功能，包括事件处理系统
    """
    pass