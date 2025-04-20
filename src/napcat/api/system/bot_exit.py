"""
账号退出 API
用于使当前登录的账号安全退出
接口地址: https://napcat.apifox.cn/283136399e0.md

参数：
无需参数

返回：
- 退出操作的结果状态，包含退出是否成功等信息

注意：
- 调用此API将导致当前账号立即退出登录
- 退出后，所有依赖登录状态的API将无法使用
- 建议在退出前保存必要的状态信息
- 如需重新使用，需要重新登录账号

# NapCat 开发中
"""

from napcat.api.base.models import BaseHttpResponse
from pydantic import BaseModel

class BotExitReq(BaseModel):
    """
    账号退出 API 请求参数
    """
    pass  # 无需参数

class ExitResult(BaseModel):
    """
    退出操作结果信息
    """
    success: bool     # 是否成功退出
    message: str      # 退出操作的相关消息

class BotExitRes(BaseHttpResponse[ExitResult]):
    """
    账号退出 API 响应参数
    """
    pass