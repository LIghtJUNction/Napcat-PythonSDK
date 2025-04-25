# -*- coding: utf-8 -*- 
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/226658234e0
@llms.txt: https://napcat.apifox.cn/226658234e0.md
@last_update: 2025-04-25 23:00:49

@description: 

summary:.OCR 图片识别

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = ".ocr_image"
__id__ = "226658234e0"
__method__ = "POST"

# region METADATA/


# region code
from pydantic import BaseModel, Field
import logging

logger = logging.getLogger(__name__)

# region component_models
class Result(BaseModel):
    status: str = Field(default="ok", description="status字段")
    retcode: float = Field(default=0.0, description="retcode字段")
    data: list[dict[str, str | list[dict[str, str]]]] = Field(default_factory=list, description="data字段")
    message: str = Field(default="", description="message字段")
    wording: str = Field(default="", description="wording字段")
    echo: str | None = Field(default=None, description="echo字段")

    model_config = {
        "extra": "allow",
    }
# region component_models/

# region req
class OCRImageReq(BaseModel):
    """OCR 图片识别"""
    image: str = Field(..., description="图片URL或本地路径")

    model_config = {
        "extra": "allow",
    }
# region req/


# region res

class OCRImageRes(BaseModel):
    """OCR 图片识别"""

    class ResponseData(BaseModel):
        """响应数据类型"""
        text: str = Field(..., description="该行文本总和")
        pt1: dict[str, str] = Field(..., description="顶点坐标")
        pt2: dict[str, str] = Field(..., description="顶点坐标")
        pt3: dict[str, str] = Field(..., description="顶点坐标")
        pt4: dict[str, str] = Field(..., description="顶点坐标")
        charBox: list[dict[str, str | dict[str, dict[str, str]]]] = Field(..., description="拆分")
        score: str = Field(..., description="得分")

        model_config = {
            "extra": "allow",
        }

    status: str = Field(default="ok", description="status字段")
    retcode: float = Field(default=0.0, description="retcode字段")
    data: list[ResponseData] = Field(default_factory=list, description="data字段")
    message: str = Field(default="", description="message字段")
    wording: str = Field(default="", description="wording字段")
    echo: str | None = Field(default=None, description="echo字段")

    model_config = {
        "extra": "allow",
    }


# region res/

# region api
class OCRImageAPI(BaseModel):
    """.ocr_image接口数据模型"""
    endpoint: str = Field(default=".ocr_image", description="API端点")
    method: str = Field(default="POST", description="HTTP方法")
    Req: type[BaseModel] = Field(default=OCRImageReq, description="请求模型")
    Res: type[BaseModel] = Field(default=OCRImageRes, description="响应模型")
    logger = logging.getLogger(__name__)

    def __init__(self) -> None:
        super().__init__()
        self.logger.debug("初始化 .ocrImageAPI")

    def __call__(self, req: OCRImageReq) -> OCRImageRes:
        """
        调用API的方法（仅作为接口定义，不包含实际请求逻辑）
        
        Args:
            req: 请求参数对象
            
        Returns:
            响应对象
        """
        # 调试日志
        self.logger.debug(f"调用 .ocrImageAPI API")
        self.logger.debug(f"请求参数: {req.model_dump_json()}")
        
        # 注意：这里不应该包含实际的请求逻辑
        # 这个方法只是定义了接口，实际的请求应由适配器或客户端实现
        raise NotImplementedError("此方法需要由实际的API客户端实现")

# region api/
# region code/