# -*- coding: utf-8 -*-
from __future__ import annotations

# region METADATA
"""
@tags: 个人操作
@homepage: https://napcat.apifox.cn/226658234e0
@llms.txt: https://napcat.apifox.cn/226658234e0.md
@last_update: 2025-04-27 00:53:40

@description: 
功能：OCR图片识别
1. 支持本地文件路径和网络URL
2. 返回识别结果，包含每行文本、位置坐标和单个字符识别信息
3. 每个识别结果包含文本内容、四个顶点坐标和识别分数
"""
__author__ = "LIghtJUNction"
__version__ = "4.7.43"
__endpoint__ = ".ocr_image"
__id__ = "226658234e0"
__method__ = "POST"
# endregion METADATA

# region code
import logging
from pydantic import BaseModel, Field
from typing import Literal 

logger = logging.getLogger(__name__)
logger.debug("加载 OcrImageAPI 模型")

# region req
class OcrImageReq(BaseModel):
    """OCR图片识别请求模型"""
    image: str = Field(..., description="图片路径或URL (支持file://本地路径和http://网络图片)")
# endregion req

# region res
class OcrImageRes(BaseModel):
    """OCR图片识别响应模型"""
    class Point(BaseModel):
        """坐标点模型"""
        x: str = Field(..., description="X坐标")
        y: str = Field(..., description="Y坐标")

    class LineData(BaseModel):
        """一行文本的识别结果模型"""
        class CharBoxDetail(BaseModel):
            """单个字符的识别结果模型"""
            class CharBoxPoints(BaseModel):
                """字符包围框的四个顶点坐标模型"""
                pt1: OcrImageRes.Point = Field(..., description="左上角顶点坐标")
                pt2: OcrImageRes.Point = Field(..., description="右上角顶点坐标")
                pt3: OcrImageRes.Point = Field(..., description="右下角顶点坐标")
                pt4: OcrImageRes.Point = Field(..., description="左下角顶点坐标")
            
            charText: str = Field(..., description="字符文本")
            charBox: CharBoxPoints = Field(..., description="字符包围框的四个顶点坐标")
        
        text: str = Field(..., description="该行文本总和")
        pt1: OcrImageRes.Point = Field(..., description="左上角顶点坐标")
        pt2: OcrImageRes.Point = Field(..., description="右上角顶点坐标")
        pt3: OcrImageRes.Point = Field(..., description="右下角顶点坐标")
        pt4: OcrImageRes.Point = Field(..., description="左下角顶点坐标")
        charBox: list[CharBoxDetail] = Field(..., description="拆分后的字符识别结果列表")
        score: str = Field(..., description="识别分数")
    
    status: Literal["ok"] = Field("ok", description="状态码，固定为 'ok'")
    retcode: int = Field(0, description="返回码")
    data: list[LineData] = Field(..., description="OCR识别结果列表，每个元素代表一行文本")
    message: str = Field("", description="消息")
    wording: str = Field("", description="提示")
    echo: str | None = Field(None, description="回显信息")
# endregion res

# region api
class OcrImageAPI(BaseModel):
    """.ocr_image接口数据模型"""
    endpoint: str = ".ocr_image"
    method: str = "POST"
    Req: type[BaseModel] = OcrImageReq
    Res: type[BaseModel] = OcrImageRes
# endregion api
# endregion code
