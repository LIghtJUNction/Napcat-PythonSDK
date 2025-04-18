from pydantic import BaseModel

# # 回复消息段
# def reply(message_id: Union[int, str]) -> MessageSegmentDict:
#     """
#     创建回复消息段
#     
#     :param message_id: 被回复消息的ID
#     :return: 回复消息段
#     """
#     return {
#         "type": "reply",
#         "data": {
#             "id": str(message_id)
#         }
#     }
# 

class Reply(BaseModel):
    """回复消息段模型"""
    
    pass
