# 
# # 合并转发自定义节点消息段
# def node_custom(user_id: int, nickname: str, 
#                content: Union[str, List[MessageSegmentDict]]) -> MessageSegmentDict:
#     """
#     创建合并转发自定义节点
#     
#     :param user_id: 发送者QQ号
#     :param nickname: 发送者昵称
#     :param content: 消息内容，可以是字符串或消息段列表
#     :return: 合并转发节点
#     """
#     from ...utils import safe_cast_message_segments
#     
#     return {
#         "type": "node",
#         "data": {
#             "user_id": user_id,
#             "nickname": nickname,
#             "content": safe_cast_message_segments(content)
#         }
#     }
# 
# # 导出所有消息段构建函数
# # 消息段基类类型
# MessageSegment = Dict[str, Any]
# 
# 