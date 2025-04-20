"""
OCR 图片识别 API
用于识别图片中的文字内容
接口地址: https://napcat.apifox.cn/251016800e0.md

参数：
- image: 图片数据，可以是图片URL或base64编码的图片数据
- type: 识别类型，指定图片类型或识别模式

返回：
- OCR识别结果，包含识别出的文本和位置信息

注意：
- 支持多种图片格式，如JPG、PNG等
- 大型图片可能需要较长处理时间
- 识别准确率受图片质量影响

# NapCat 开发中
"""

from pydantic import BaseModel
from napcat.api.base.models import BaseHttpResponse

class OcrImageReq(BaseModel):
    """
    OCR 图片识别 API 请求参数
    """
    image: str                # 图片URL或base64编码的图片数据
    type: str | None = None  # 识别类型(可选)，如"general", "handwriting", "receipt"等

class TextPosition(BaseModel):
    """
    识别文本的位置信息
    """
    x: int                    # 左上角x坐标
    y: int                    # 左上角y坐标
    width: int                # 宽度
    height: int               # 高度

class TextBlock(BaseModel):
    """
    识别出的文本块信息
    """
    text: str                 # 识别出的文本内容
    confidence: float         # 识别置信度(0-1)
    position: TextPosition    # 文本块位置信息

class OcrResult(BaseModel):
    """
    OCR识别结果
    """
    text_blocks: list[TextBlock]  # 识别出的文本块列表
    full_text: str            # 完整识别文本
    language: str             # 识别出的主要语言
    orientation: str          # 文本方向

class OcrImageRes(BaseHttpResponse[OcrResult]):
    """
    OCR 图片识别 API 响应参数
    """
    pass