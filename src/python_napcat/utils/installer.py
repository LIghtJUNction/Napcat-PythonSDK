from requests.models import Response

from logging import Logger

from functools import wraps
import json
from pathlib import Path
import requests
import logging
import zipfile
import shutil
from tqdm import tqdm
from typing import Literal, TypeAlias, cast

from collections.abc import Callable

from aivk.api import AivkIO

logger: Logger = logging.getLogger(name=__name__)

JSONType: TypeAlias = dict[str, object]

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
    
    @classmethod
    def update_proxy_list(cls) -> None:
        """
        更新代理列表。
        从api.akams.cn/github获取速度最快的GitHub代理站点，按速度排序更新GITHUB_PROXIES列表。
        """
        cls.GITHUB_PROXIES = []
        
        # 尝试从所有代理源获取数据
        for source in cls._GITHUB_PROXIES_SOURCES:
            try:
                logger.info(msg=f"正在从 {source} 获取GitHub代理列表...")
                response: Response = requests.get(source, timeout=10)
                response.raise_for_status()
                data: dict[str, object] = cast(dict[str, object], response.json())
                if isinstance(data.get("code"), int) and data.get("code") == 200 and "data" in data:
                    data_list: object = data["data"]
                    if not isinstance(data_list, list):
                        continue
                    valid_proxies: list[str] = []

                    for item in data_list: 
                        item = cast(dict[str, object], item)
                        url: object | None = item.get("url")
                        speed: object = item.get("speed", 0)
                        if isinstance(url, str) and isinstance(speed, (int, float)) and speed > 0.5:
                            valid_proxies.append(url)
                    normalized_proxies: list[str] = []
                    for proxy in valid_proxies:
                        if proxy and not proxy.endswith('/'):
                            proxy: str = proxy + '/'
                        normalized_proxies.append(proxy)
                    top_proxies: list[str] = normalized_proxies[:10]
                    if top_proxies:
                        cls.GITHUB_PROXIES = top_proxies
                        logger.info(msg=f"成功更新GitHub代理列表，获取到 {len(top_proxies)} 个有效代理")
                        backup_proxies: list[str] = [
                            "https://ghproxy.com/",
                            "https://github.moeyy.xyz/",
                            "https://ghfast.top/",
                            "https://mirror.ghproxy.com/"
                        ]
                        for proxy in backup_proxies:
                            if proxy not in cls.GITHUB_PROXIES:
                                cls.GITHUB_PROXIES.append(proxy)
                        logger.debug(msg=f"当前代理列表: {cls.GITHUB_PROXIES}")
                        return
                logger.warning(msg=f"从 {source} 获取到的数据无效或不包含有效代理")
            except Exception as e:
                logger.warning(msg=f"从 {source} 获取GitHub代理列表失败: {str(e)}")
        default_proxies: list[str] = [
            "https://ghfast.top/",
            "https://ghproxy.com/",
            "https://github.moeyy.xyz/",
            "https://mirror.ghproxy.com/",
            "https://gh.api.99988866.xyz/",
            "https://gh.ddlc.top/"
        ]
        cls.GITHUB_PROXIES = default_proxies
        logger.warning(f"无法从代理源获取数据，使用默认代理列表: {default_proxies}")



    @staticmethod
    def retry_with_proxy(func: Callable[..., object]) -> Callable[..., object | Literal[False]]:
        """
        装饰器：使用不同的代理地址重试函数。
        当一个代理失败时，会自动尝试下一个代理，直到所有代理都尝试过。
        
        :param func: 要重试的函数
        :return: 包装后的函数
        """
        @wraps(wrapped=func)
        def wrapper(cls: type, *args: object, **kwargs: object) -> object | Literal[False]:
            # 获取用户指定的代理参数
            proxy_param: str | None = cast(str | None, kwargs.pop('proxy', None) if 'proxy' in kwargs else None)
            
            # 如果用户指定了代理，则将其作为第一个尝试的代理
            proxies_to_try: list[str] = []
            if isinstance(proxy_param, str):
                proxies_to_try.append(proxy_param)
            
            # 添加默认代理列表
            proxies_to_try.extend(list(cast(list[str], cls.GITHUB_PROXIES)))
            
            # 记录尝试过的代理和错误
            errors: list[str] = []
            
            # 依次尝试所有代理
            for proxy in proxies_to_try:
                try:
                    result: object = func(cls, *args, **kwargs, proxy=proxy)
                    # 只在结果不是False时输出成功日志（即实际执行了操作时）
                    if result is not False:
                        logger.info(msg=f"使用代理 {proxy} 成功")
                    return result
                except Exception as e:
                    error_msg: str = f"使用代理 {proxy} 失败: {str(e)}"
                    logger.warning(msg=error_msg)
                    errors.append(error_msg)
            
            # 所有代理均失败
            error_details: str = "\n".join(errors)
            logger.error(msg=f"所有代理均失败:\n{error_details}")
            raise RuntimeError(f"所有代理均失败，无法完成操作。详情:\n{error_details}")
        
        return wrapper
    

    @classmethod
    @retry_with_proxy
    def get_last_version(cls, proxy: str | None = None) -> str:
        """
        获取最新版本号。
        
        :return: 最新版本号
        """
        # 修复URL拼接问题：确保代理URL正确拼接GitHub URL
        if not proxy:
            url = cls.PACKAGE_JSON
        else:
            # 从URL中提取域名之后的部分
            github_path = cls.PACKAGE_JSON.split("://", 1)[1]
            # 确保代理URL以/结尾
            if not proxy.endswith("/"):
                proxy += "/"
            url = f"{proxy}https://{github_path}"

        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = cast(dict[str, object], response.json())
        version = data.get("version")
        if not isinstance(version, str):
            raise RuntimeError("无法解析版本号")
        return version
    

    @classmethod
    def get_local_version(cls) -> str | None:
        """
        获取本地版本号。
        
        :return: 本地版本号
        """
        version_file = AivkIO.get_aivk_root() / "data" / "qq" / "napcat" / "package.json"
        
        if not version_file.exists():
            return None
        
        data: dict[str, object] = cast(dict[str, object], json.load(fp=version_file.open("r", encoding="utf-8")))
        version: object | None = data.get("version")
        return version if isinstance(version, str) else None
    

    @classmethod
    def need_update(cls) -> bool:
        """
        检查是否需要更新。
        
        :return: 是否需要更新
        """
        local_version: str | None = cls.get_local_version()
        if not local_version:
            return True
        logger.info(msg=f"本地版本: {local_version}")
        
        last_version = cast(str, cls.get_last_version())
        logger.info(msg=f"最新版本: {last_version}")
        return local_version != last_version

    # region WINDOWS

    @classmethod
    @retry_with_proxy
    def download_for_windows(cls, version: str | None = None, proxy: str | None = None, force: bool = False, progress_callback: Callable[[float], None] | None = None) -> bool:
        """
        下载Windows版本的Napcat Shell。
        
        :param version: 版本号
        :param proxy: 代理地址（可选）
        :param force: 强制下载，即使文件已存在
        :param progress_callback: 进度回调函数，接收一个0-100的浮点数表示下载进度百分比
        :return: 下载的文件路径
        """
        # https://github.com/NapNeko/NapCatQQ/releases/download/v4.7.23/NapCat.Shell.zip
        if not version:
            version = cast(str | None, cls.get_last_version(proxy=proxy))
            if not isinstance(version, str):
                raise RuntimeError("获取最新版本号失败")

        unzip_path: Path = AivkIO.get_aivk_root() / "data" / "qq" / "napcat" 

        # 检查是否需要下载
        if not force and unzip_path.exists() and any(unzip_path.iterdir()):
            logger.info(msg="No update needed, skipping download.")
            return False
        
        # 修复URL拼接问题
        if not proxy:
            download_url: str = f"{cls.GITHUB_REPO}/releases/download/v{version}/NapCat.Shell.zip"
        else:
            # 从URL中提取域名之后的部分
            github_path: str = cls.GITHUB_REPO.split("://", 1)[1]
            if not proxy.endswith("/"):
                proxy  = str(proxy) + "/"
            download_url = f"{proxy}https://{github_path}/releases/download/v{version}/NapCat.Shell.zip"
            
        logger.info(msg=f"Downloading Napcat Shell for Windows from {download_url}...")
        
        # 创建临时目录存放下载文件
        tmp_dir: Path = AivkIO.get_aivk_root() / "tmp" / "qq" / "download"

        tmp_dir.mkdir(parents=True, exist_ok=True)
        
        download_path: Path = tmp_dir / f"NapCat.Shell_{version}.zip"
        
        if force and unzip_path.exists():
            shutil.rmtree(unzip_path, ignore_errors=True)
            logger.info(msg=f"Removed existing directory: {unzip_path}")

        # 使用流式下载以支持进度条
        with requests.get(url=download_url, stream=True, timeout=30) as response:
            response.raise_for_status()
            total_size: int = int(response.headers.get('content-length', 0))
            
            # 使用更简单可靠的进度条样式，避免自定义格式导致的错误
            with tqdm(
                total=total_size,
                unit='B',
                unit_scale=True,
                desc="下载进度",
                dynamic_ncols=True,
                ascii=False
            ) as pbar:
                with open(file=download_path, mode='wb') as f:
                    chunk : bytes | None = None
                    for chunk in response.iter_content(chunk_size=8192):
                        chunk = cast(bytes, chunk)
                        if chunk:
                            _ = f.write(chunk)
                            downloaded_size: int = len(chunk)
                            _ = pbar.update(n=downloaded_size)
                            
                            # 计算进度百分比并回调
                            if total_size > 0 and progress_callback:
                                percent: int = int(cast(int, pbar.n) * 100 / total_size)
                                progress_callback(percent)

        # 解压到 -> AivkIO.get_aivk_root() / "data" / "qq" / "napcat" /
        logger.info(msg=f"解压文件到 {unzip_path}...")
        
        # 使用标准进度条显示解压进度
        with zipfile.ZipFile(download_path, 'r') as zip_ref:
            # 获取zip文件中的所有文件
            file_list: list[str] = zip_ref.namelist()
            with tqdm(
                total=len(file_list),
                desc="解压进度",
                dynamic_ncols=True
            ) as extract_pbar:
                # 逐个解压文件
                for file in file_list:
                    _ = zip_ref.extract(file, unzip_path)
                    _ = extract_pbar.update(1)
                
            logger.info(f"文件解压完成: {unzip_path}")

        # 清理临时文件
        try:
            logger.info(msg="清理临时文件...")
            shutil.rmtree(tmp_dir, ignore_errors=True)
            logger.info(msg="临时文件清理完成")
        except Exception as e:
            logger.warning(msg=f"清理临时文件时发生错误: {str(e)}")
            
        logger.info(msg=f"下载与安装完成: Napcat Shell v{version}")
        return True




