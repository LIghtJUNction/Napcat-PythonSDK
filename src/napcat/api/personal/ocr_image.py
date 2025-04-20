# -*- coding: utf-8 -*-
"""
OCR图片识别 API
开发完毕
@作者：GitHub Copilot
@日期：2025/04/20
"""

from typing import Literal

from pydantic import ConfigDict, Field
from ..base.models import BaseHttpAPI, BaseHttpRequest, BaseHttpResponse, BaseModel


class Request(BaseHttpRequest):
    """
    OCR图片识别请求参数
    """
    image: str = Field(description="图片URL或Base64编码的图片数据")
    type: str = Field(default="general", description="识别类型，默认为general通用文字识别")


class TextLine(BaseModel):
    """
    识别出的文本行
    """
    text: str = Field(default="", description="识别的文本内容")
    confidence: float = Field(default=0.0, description="置信度")
    position: list[dict[str, int]] = Field(default_factory=list, description="文本位置坐标")
    
    model_config = ConfigDict(
        extra="allow",  # 允许额外字段
        frozen=False,   # 不冻结模型
        populate_by_name=True,  # 通过名称填充字段
        arbitrary_types_allowed=True,  # 允许任意类型
    )


class ResponseData(BaseModel):
    """
    OCR图片识别响应数据模型
    """
    text: str = Field(default="", description="识别出的完整文本")
    language: str = Field(default="", description="识别语言")
    lines: list[TextLine] = Field(default_factory=list, description="识别出的文本行列表")
    
    model_config = ConfigDict(
        extra="allow",  # 允许额外字段
        frozen=False,   # 不冻结模型
        populate_by_name=True,  # 通过名称填充字段
        arbitrary_types_allowed=True,  # 允许任意类型
    )


class Response(BaseHttpResponse[ResponseData]):
    """
    OCR图片识别响应参数
    """
    pass


class OcrImageAPI(BaseHttpAPI):
    """
    OCR图片识别 API
    用于识别图片中的文字内容
    接口地址: https://napcat.apifox.cn/226659139e0.md

    参数：
    {
      "image": "https://example.com/image.jpg",  // 或Base64编码图片数据
      "type": "general"  // 识别类型
    }

    返回：
    - 识别出的文字内容，包含完整文本、语言类型和文本行列表等信息
    """

    api: str = "/ocr_image"
    method: Literal['POST', 'GET'] = "POST"
    request: BaseHttpRequest = Request()
    response: BaseHttpResponse[ResponseData] = Response()

if __name__ == "__main__":
    from ..base.utils import test_model
    # uv pip install -e . 
    # python -m napcat.api.personal.ocr_image
    test_model(Request)
    test_model(TextLine)
    test_model(ResponseData)
    test_model(Response)