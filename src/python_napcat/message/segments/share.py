from pydantic import BaseModel

# # 分享链接消息段
# def share(url: str, title: str, 
#          content: Optional[str] = None, 
#          image: Optional[str] = None) -> MessageSegmentDict:
#     """
#     创建分享链接消息段
#     
#     :param url: 链接URL
#     :param title: 链接标题
#     :param content: 链接内容描述，可选
#     :param image: 图片URL，可选
#     :return: 分享链接消息段
#     """
#     data: Dict[str, str] = {
#         "url": url,
#         "title": title
#     }
#     if content:
#         data["content"] = content
#     if image:
#         data["image"] = image
#         
#     return {
#         "type": "share",
#         "data": data
#     }

class Share(BaseModel):
    """分享链接消息段模型"""
    
    pass