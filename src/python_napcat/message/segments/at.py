from pydantic import BaseModel


# # @消息段
# def at(user_id: Union[int, str], name: Optional[str] = None) -> MessageSegmentDict:
#     """
#     创建@消息段
#     
#     :param user_id: 用户QQ号，或者"all"表示@全体成员
#     :param name: 自定义@的显示内容，可选
#     :return: @消息段
#     """
#     data: Dict[str, Any] = {"qq": str(user_id)}
#     if name:
#         data["name"] = name
#     return {
#         "type": "at",
#         "data": data
#     }

class At(BaseModel):
    """@消息段模型"""
    
    pass