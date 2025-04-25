# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: 个人操作
@homepage: https://napcat.apifox.cn/226658234e0
@llms.txt: https://napcat.apifox.cn/226658234e0.md
@last_update: 2025-04-26 01:17:44

@description: 

summary:.OCR 图片识别

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = ".ocr_image"
__id__ = "226658234e0"
__method__ = "POST"

# endregion METADATA


# region code
import logging
from pydantic import BaseModel, Field

logger = logging.getLogger(__name__)

# region req
class OcrImageReq(BaseModel):
    """
    .OCR 图片识别 请求模型
    """
    image: str = Field(..., description="图片路径或URL (支持file://和http://)")
# endregion req


# region res

class Point(BaseModel):
    """
    顶点坐标模型
    """
    x: str = Field(..., description="X坐标")
    y: str = Field(..., description="Y坐标")

class CharBoxData(BaseModel):
    """
    单个字符及包围框模型
    """
The user requested a fix for a Pydantic v2 model based on an OpenAPI spec.

The plan is to:
1. Define the request model `OcrImageReq` based on the requestBody in the OpenAPI spec.
2. Define the response models based on the response schema for `200`:
    - Create nested models for `Point` (x, y coordinates).
    - Create a nested model for the character box details, which includes `charText` and another nested `charBox` containing `Point`s.
    - Create a nested model for a single line of text, including `text`, `pt1` through `pt4` (using the `Point` model), `charBox` (array of character box models), and `score`.
    - Create the main response model `OcrImageRes` which includes `status`, `retcode`, `data` (array of line models), `message`, `wording`, and `echo` (nullable).
3. Update the `OcrImageAPI` class to reference the new models.
4. Ensure all models follow the coding guidelines: use built-in types for list/dict/etc., use `| None` for nullable fields, use `pydantic.Field` for descriptions and required flags.
5. Remove unnecessary imports.
6. Format the output as the required JSON structure.
    charText: str = Field(..., description="字符文本")
    charBox: Point = Field(..., description="字符包围框，实际为4个点，简化为Point列表或者单独定义模型") # NOTE: The OpenAPI defines this as an object with pt1, pt2, pt3, pt4, not a single Point. Needs correction.

class OcrImageRes(BaseModel):
    # 定义响应参数
    # 例如：
    # param1: str = Field(..., description="参数1的描述")
    # param2: int = Field(..., description="参数2的描述")
    
    pass
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

# Analysis of the OpenAPI Spec for Response Model:
# - Top level: status (str, const 'ok'), retcode (number), data (array), message (str), wording (str), echo (str | null)
# - data items (LineData): text (str), pt1, pt2, pt3, pt4 (Point), charBox (array of CharBoxDetail), score (str)
# - Point: x (str), y (str)
# - CharBoxDetail: charText (str), charBox (object with pt1, pt2, pt3, pt4 - using Point)

# Let's redefine the response models properly.

# region code
import logging
from pydantic import BaseModel, Field

logger = logging.getLogger(__name__)

# region req
class OcrImageReq(BaseModel):
    """
    .OCR 图片识别 请求模型
    """
    image: str = Field(..., description="图片路径或URL (支持file://和http://)")
# endregion req


# region res

class Point(BaseModel):
    """
    顶点坐标模型
    """
    x: str = Field(..., description="X坐标")
    y: str = Field(..., description="Y坐标")

class CharBoxPoints(BaseModel):
    """
    单个字符的包围框顶点坐标模型
    """\n    pt1: Point = Field(..., description="左上角顶点坐标")
    pt2: Point = Field(..., description="右上角顶点坐标")
    pt3: Point = Field(..., description="右下角顶点坐标")
    pt4: Point = Field(..., description="左下角顶点坐标")

class CharBoxDetail(BaseModel):
    """
    单个字符的识别结果模型
    """
    charText: str = Field(..., description="字符文本")
    charBox: CharBoxPoints = Field(..., description="字符包围框顶点坐标")

class LineData(BaseModel):
    """
    一行文本的识别结果模型
    """
    text: str = Field(..., description="该行文本总和")
    pt1: Point = Field(..., description="左上角顶点坐标")
    pt2: Point = Field(..., description="右上角顶点坐标")
    pt3: Point = Field(..., description="右下角顶点坐标")
    pt4: Point = Field(..., description="左下角顶点坐标")
    charBox: list[CharBoxDetail] = Field(..., description="拆分后的字符识别结果列表")
    score: str = Field(..., description="识别分数") # NOTE: OpenAPI says string, example is empty string. Keep as string.

class OcrImageRes(BaseModel):
    """
    .OCR 图片识别 响应模型
    """
    status: str = Field(..., description="状态码，应为 'ok'") # OpenAPI specifies const 'ok'
    retcode: int = Field(..., description="返回码") # OpenAPI specifies number, example is 0 (int)
    data: list[LineData] = Field(..., description="OCR识别结果列表，一个元素代表一行")
    message: str = Field(..., description="消息")
    wording: str = Field(..., description="提示")
    echo: str | None = Field(None, description="回显信息") # OpenAPI specifies nullable string

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
