# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: 个人操作
@homepage: https://napcat.apifox.cn/226658234e0
@llms.txt: https://napcat.apifox.cn/226658234e0.md
@last_update: 2025-04-27 00:53:40

@description: 

summary:.OCR 图片识别

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.43"
__endpoint__ = ".ocr_image"
__id__ = "226658234e0"
__method__ = "POST"

# endregion METADATA


# region code
from pydantic import BaseModel, Field
from typing import Literal # Keep Literal for fixed string values

# region req
class OcrImageReq(BaseModel):
    """
    .OCR 图片识别接口请求模型
    """

    image: str = Field(..., description="图片URL或本地路径 (e.g., 'https://...' or 'file://...')")
# endregion req



# region res
class Point(BaseModel):
    """
    顶点坐标模型
    """
    x: str = Field(..., description="X坐标")
    y: str = Field(..., description="Y坐标")

class CharBoxInner(BaseModel):
    """
    字符边界框坐标模型
    """
    pt1: Point = Field(..., description="左上角顶点坐标")
    pt2: Point = Field(..., description="右上角顶点坐标")
    pt3: Point = Field(..., description="右下角顶点坐标")
    pt4: Point = Field(..., description="左下角顶点坐标")

class CharBoxItem(BaseModel):
    """
    字符拆分信息模型
    """
    charText: str = Field(..., description="字符文本")
    charBox: CharBoxInner = Field(..., description="字符边界框")

class OcrResultItem(BaseModel):
    """
    单个OCR识别结果项模型 (代表一行文本)
    """
    text: str = Field(..., description="该行文本总和")
    pt1: Point = Field(..., description="左上角顶点坐标")
    pt2: Point = Field(..., description="右上角顶点坐标")
    pt3: Point = Field(..., description="右下角顶点坐标")
    pt4: Point = Field(..., description="左下角顶点坐标")
    charBox: list[CharBoxItem] = Field(..., description="字符拆分")
    score: str = Field(..., description="置信度") # OpenAPI spec lists as string, example is empty string, keep as str

class OcrImageRes(BaseModel):
    """
    .OCR 图片识别接口响应模型
    """
    status: Literal["ok"] = Field(..., description="状态")
    retcode: int = Field(..., description="返回码")
    data: list[OcrResultItem] = Field(..., description="OCR结果列表，一个项代表一行")
    message: str = Field(..., description="消息")
    wording: str = Field(..., description="词语")
    echo: str | None = Field(..., description="回显信息")

# endregion res

# region api
class OcrImageAPI(BaseModel):
    ".ocr_image接口数据模型"
    endpoint: str = ".ocr_image"
    method: str = "POST"
    Req: type[BaseModel] = OcrImageReq
    Res: type[BaseModel] = OcrImageRes
# endregion api




# endregion code
