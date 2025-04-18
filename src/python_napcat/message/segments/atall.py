from pydantic import BaseModel
# # @全体成员
# def at_all() -> MessageSegmentDict:
#     """
#     创建@全体成员消息段
#     
#     :return: @全体成员消息段
#     """
#     return at("all")
#     


class AtAll(BaseModel):
    """@全体成员消息段模型"""
    pass