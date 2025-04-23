# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/228534368e0
@llms.txt: https://napcat.apifox.cn/228534368e0.md
@last_update: 2025-04-23 20:23:18

@description: 

summary:获取中文分词

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = ".get_word_slices"
__id__ = "228534368e0"
__method__ = "POST"

# region METADATA/


# region code
from typing import Any
from pydantic import BaseModel, Field

# region req

# region req/


# region res
class .getWordSlicesRes(BaseModel):
    """
    响应参数
    """

    pass
# region res/

# region api
class .getWordSlicesAPI(BaseModel):
    
    Request : type[.getWordSlicesReq] = .getWordSlicesReq
    Response  : type[.getWordSlicesRes] = .getWordSlicesRes


# region api/
# region code/

