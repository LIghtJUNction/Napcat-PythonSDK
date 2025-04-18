from pydantic import BaseModel
# # 文本消息段
# def text(content: str) -> MessageSegmentDict:
#     """
#     创建文本消息段
#     
#     :param content: 文本内容
#     :return: 文本消息段
#     """
#     return {
#         "type": "text",
#         "data": {
#             "text": content
#         }
#     }
# 
# 
class Text(BaseModel):
    pass