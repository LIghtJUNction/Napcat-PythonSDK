from pydantic import BaseModel

# # 视频消息段
# def video(file: Union[str, bytes],
#          cache: bool = True,
#          proxy: bool = True,
#          timeout: Optional[int] = None) -> MessageSegmentDict:
#     """
#     创建视频消息段
#     
#     :param file: 视频文件路径、URL或base64编码的视频数据
#     :param cache: 是否使用缓存，默认True
#     :param proxy: 是否通过代理下载，默认True
#     :param timeout: 下载超时时间(秒)，可选
#     :return: 视频消息段
#     """
#     data: Dict[str, Any] = {"file": file}
#     if timeout is not None:
#         data["timeout"] = timeout
#         
#     data["cache"] = int(cache)
#     data["proxy"] = int(proxy)
#     
#     return {
#         "type": "video",
#         "data": data
#     }
# 

class Video(BaseModel):
    """视频消息段模型"""
    pass