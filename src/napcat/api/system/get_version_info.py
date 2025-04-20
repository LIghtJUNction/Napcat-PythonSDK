"""
获取版本信息 API
用于获取当前NapCat的版本信息
接口地址: https://napcat.apifox.cn/226657087e0.md

参数：
无需参数

返回：
- 包含版本信息的对象，通常包括版本号、构建日期、运行环境等
- 可能包含框架版本、插件版本以及兼容性信息

注意：
- 版本信息对于排查兼容性问题和获取更新非常重要
- 在提交问题报告时，建议附上此API返回的版本信息
- 版本信息可用于判断是否需要更新到最新版本

# NapCat 开发中
"""

from pydantic import BaseModel
from napcat.api.base.models import BaseHttpResponse

class GetVersionInfoReq(BaseModel):
    """
    获取版本信息 API 请求参数
    """
    pass  # 无需参数

class EnvironmentInfo(BaseModel):
    """
    运行环境信息
    """
    os: str                   # 操作系统信息
    python_version: str       # Python版本
    runtime_env: str          # 运行时环境信息
    system_arch: str          # 系统架构

class PluginVersion(BaseModel):
    """
    插件版本信息
    """
    name: str                 # 插件名称
    version: str              # 插件版本
    enabled: bool             # 是否启用
    compatible: bool          # 是否兼容当前版本

class DetailedVersionInfo(BaseModel):
    """
    详细版本信息
    """
    app_name: str             # 应用名称
    app_version: str          # 应用版本号
    build_number: str         # 构建编号
    build_date: str           # 构建日期
    protocol_version: str     # 协议版本号
    environment: EnvironmentInfo  # 环境信息
    plugins: list[PluginVersion]  # 插件版本列表
    update_available: bool    # 是否有可用更新
    latest_version: str       # 最新可用版本

class GetVersionInfoRes(BaseHttpResponse[DetailedVersionInfo]):
    """
    获取版本信息 API 响应参数
    """
    pass

class VersionInfo(BaseModel):
    """
    版本信息
    """
    app_name: str       # 应用名称
    app_version: str    # 应用版本
    protocol_version: str # 协议版本
    go_cqhttp_version: str # go-cqhttp 版本 (如果基于)
    # 可以根据实际API响应添加更多字段

class GetVersionInfoRes(BaseHttpResponse[VersionInfo]):
    """
    获取版本信息 API 响应参数
    """
    pass