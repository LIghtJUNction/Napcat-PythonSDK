from pydantic import BaseModel

# # 语音消息段
# def record(file: Union[str, bytes],
#           magic: bool = False,
#           cache: bool = True,
#           proxy: bool = True,
#           timeout: Optional[int] = None) -> MessageSegmentDict:
#     """
#     创建语音消息段
#     
#     :param file: 语音文件路径、URL或base64编码的语音数据
#     :param magic: 是否变声，默认False
#     :param cache: 是否使用缓存，默认True
#     :param proxy: 是否通过代理下载，默认True
#     :param timeout: 下载超时时间(秒)，可选
#     :return: 语音消息段
#     """
#     data: Dict[str, Any] = {"file": file}
#     if magic:
#         data["magic"] = int(magic)
#     if timeout is not None:
#         data["timeout"] = timeout
#         
#     data["cache"] = int(cache)
#     data["proxy"] = int(proxy)
#     
#     return {
#         "type": "record",
#         "data": data
#     }
# 

class Record(BaseModel):
    """语音消息段模型"""
    
    pass