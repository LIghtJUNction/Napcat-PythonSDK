from pydantic import BaseModel

# # 位置消息段
# def location(latitude: float, longitude: float, 
#             title: Optional[str] = None, 
#             content: Optional[str] = None) -> MessageSegmentDict:
#     """
#     创建位置消息段
#     
#     :param latitude: 纬度
#     :param longitude: 经度
#     :param title: 位置标题，可选
#     :param content: 位置描述，可选
#     :return: 位置消息段
#     """
#     data: Dict[str, Any] = {
#         "lat": str(latitude),
#         "lon": str(longitude)
#     }
#     if title:
#         data["title"] = title
#     if content:
#         data["content"] = content
#         
#     return {
#         "type": "location",
#         "data": data
#     }
# 

class Location(BaseModel):
    """位置消息段模型"""
    
    pass