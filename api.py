# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: {{homepage}}
@llms.txt: {{llms.txt}}
@last_update: {{last_update}}

@description: {{description}}

"""
__author__ = "LIghtJUNction"
__version__ = "{{version}}"
__endpoint__ = "{{endpoint}}"
__id__ = "{{api_id}}"
__method__ = "POST"

# region METADATA/


# region code
import logging
from typing import Any
from pydantic import BaseModel, Field

logger = logging.getLogger(__name__)

# region req
class {{EndPointReq}}(BaseModel): # type: ignore
    """
    {{DESC_EndPointReq}}
    """

    pass
# region req/



# region res
class {{EndPointRes}}(BaseModel): # type: ignore
    # 定义响应参数
    # 例如：
    # param1: str = Field(..., description="参数1的描述")
    # param2: int = Field(..., description="参数2的描述")
    
    pass
# region res/

# region api
class {{EndPointAPI}}(BaseModel):
    """{{endpoint}}接口数据模型"""
    endpoint: str = "{{endpoint}}"
    method: str = "{{method}}"
    Req: type[BaseModel] = {{EndPointReq}}
    Res: type[BaseModel] = {{EndPointRes}}
    logger = logging.getLogger(__name__)

    def __init__(self) -> None:
        super().__init__()
        self.logger.debug("初始化 {{EndPointAPI}}")

    def __call__(self, req: {{EndPointReq}}) -> {{EndPointRes}}:
        """
        调用API的方法（仅作为接口定义，不包含实际请求逻辑）
        
        Args:
            req: 请求参数对象
            
        Returns:
            响应对象
        """
        # 调试日志
        self.logger.debug(f"调用 {{EndPointAPI}} API")
        self.logger.debug(f"请求参数: {req.model_dump_json()}")
        
        # 注意：这里不应该包含实际的请求逻辑
        # 这个方法只是定义了接口，实际的请求应由适配器或客户端实现
        raise NotImplementedError("此方法需要由实际的API客户端实现")
# region api/




# region code/

