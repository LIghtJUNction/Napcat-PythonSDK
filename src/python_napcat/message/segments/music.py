from pydantic import BaseModel

# # 音乐消息段
# def music(type: str, id: Union[int, str]) -> MessageSegmentDict:
#     """
#     创建音乐消息段
#     
#     :param type: 音乐平台类型，如"qq"、"163"、"xm"
#     :param id: 音乐ID
#     :return: 音乐消息段
#     """
#     return {
#         "type": "music",
#         "data": {
#             "type": type,
#             "id": str(id)
#         }
#     }
#     

class Music(BaseModel):
    """音乐消息段模型"""
    
    pass