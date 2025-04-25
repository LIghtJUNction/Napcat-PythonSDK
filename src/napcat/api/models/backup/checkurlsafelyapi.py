from pydantic import BaseModel, Field

# region req
class CheckUrlSafelyReq(BaseModel):
    """
    检查链接安全性 - 请求模型
    """
    # OpenAPI spec shows no request parameters.
    pass
# endregion req

# region res
class CheckUrlSafelyRes(BaseModel):
    """
    检查链接安全性 - 响应模型
    """
    # OpenAPI spec shows an empty response object {}.
    pass
# endregion res

# region api
class CheckUrlSafelyAPI(BaseModel):
    """check_url_safely接口数据模型"""
    endpoint: str = "check_url_safely"
    method: str = "POST"
    Req: type[BaseModel] = CheckUrlSafelyReq
    Res: type[BaseModel] = CheckUrlSafelyRes
# endregion api