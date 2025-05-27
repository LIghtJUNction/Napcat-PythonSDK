# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/226658867e0
@llms.txt: https://napcat.apifox.cn/226658867e0.md
@last_update: 2025-05-28 01:34:09

@description: 

summary:获取群文件链接

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.43"
__endpoint__ = "get_group_file_url"
__id__ = "226658867e0"
__method__ = "POST"

# endregion METADATA


# region code
from pydantic import BaseModel, Field
from typing import Literal # 导入 Literal 用于固定值类型
import logging

logger = logging.getLogger(__name__)

# region component_models

# 根据OpenAPI规范，group_id 在请求中应为 int 或 str 类型，
# 而非一个 BaseModel 对象。因此，移除了原有的 group_id BaseModel 定义。
# class group_id(BaseModel):
#     id: str = Field(description="标识ID")
#     name: str | None = Field(None, description="名称")

#     model_config = {
#         "extra": "allow",
#     }

class result(BaseModel):
    status: Literal["ok"] = Field(default="ok", description="状态字段，通常为 'ok'")
    retcode: float = Field(default=0.0, description="返回码")
    data: dict[str, any] = Field(default_factory=dict, description="响应数据字段") # 使用 any 替代 Any
    message: str = Field(default="", description="消息")
    wording: str = Field(default="", description="提示")
    echo: str | None = Field(default=None, description="回显数据")

    model_config = {
        