from pydantic import BaseModel

# # 图片消息段
# def image(file: Union[str, bytes], 
#          type: Optional[str] = None, 
#          url: Optional[str] = None, 
#          cache: bool = True, 
#          proxy: bool = True, 
#          timeout: Optional[int] = None) -> MessageSegmentDict:
#     """
#     创建图片消息段
#     
#     :param file: 图片文件路径、URL或base64编码的图片数据
#     :param type: 图片类型，"flash"表示闪照
#     :param url: 图片URL，可选
#     :param cache: 是否使用缓存，默认True
#     :param proxy: 是否通过代理下载，默认True
#     :param timeout: 下载超时时间(秒)，可选
#     :return: 图片消息段
#     """
#     data: Dict[str, Any] = {"file": file}
#     if type:
#         data["type"] = type
#     if url:
#         data["url"] = url
#     if timeout is not None:
#         data["timeout"] = timeout
#         
#     data["cache"] = int(cache)
#     data["proxy"] = int(proxy)
#     
#     return {
#         "type": "image",
#         "data": data
#     }
# 

class Image(BaseModel):
    """图片消息段模型"""
    
    pass