# # 自定义音乐消息段
# def music_custom(url: str, audio: str, title: str, 
#                 content: Optional[str] = None, 
#                 image: Optional[str] = None) -> MessageSegmentDict:
#     """
#     创建自定义音乐消息段
#     
#     :param url: 点击后跳转的链接URL
#     :param audio: 音频文件URL
#     :param title: 标题
#     :param content: 内容描述，可选
#     :param image: 图片URL，可选
#     :return: 自定义音乐消息段
#     """
#     data: Dict[str, str] = {
#         "type": "custom",
#         "url": url,
#         "audio": audio,
#         "title": title
#     }
#     if content:
#         data["content"] = content
#     if image:
#         data["image"] = image
#         
#     return {
#         "type": "music",
#         "data": data
#     }
# 
