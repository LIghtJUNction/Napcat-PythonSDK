# -*- coding: utf-8 -*-


import logging
logger = logging.getLogger(name=__name__)

class NapcatInstaller:
    """
    NapcatInstaller类负责处理Napcat Shell的下载、安装和版本管理。
    所有方法都是静态方法，可直接通过类名调用，无需实例化。
    """
    # 默认配置
    GITHUB_REPO: str = "https://github.com/NapNeko/NapCatQQ"
    PACKAGE_JSON: str = "https://raw.githubusercontent.com/NapNeko/NapCatQQ/main/package.json"
    # 代理列表，按优先级排序
    GITHUB_PROXIES: list[str] = [
        "https://ghfast.top/",      # 主要代理
    ]
    _GITHUB_PROXIES_SOURCES: list[str] = [
        "https://api.akams.cn/github",
    ]
    # region public methods
    