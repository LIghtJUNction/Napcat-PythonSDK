from pydantic import BaseModel

# # 表情消息段
# def face(face_id: int) -> MessageSegmentDict:
#     """
#     创建表情消息段
#     
#     :param face_id: 表情ID
#     :return: 表情消息段
#     """
#     return {
#         "type": "face",
#         "data": {
#             "id": str(face_id)
#         }
#     }
#     

class Face(BaseModel):
    """表情消息段模型"""
    
    pass