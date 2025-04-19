"""
发送消息 API (保留版本)
用于向指定好友或群聊发送消息，是一个通用的消息发送接口，保留的旧版本接口
接口地址: https://napcat.apifox.cn/226656652e0.md

参数：
- message_type: 消息类型，支持 private、group，分别对应私聊、群组
- user_id: 对方QQ号 (当message_type=private时需要)
- group_id: 群号 (当message_type=group时需要)
- message: 要发送的消息内容
- auto_escape: 消息内容是否作为纯文本发送，为true则message内容不解析CQ码，默认为false

返回：
- 包含消息ID等信息的对象

注意：
- 此API是保留的旧版本接口，建议使用新版API
- user_id 和 group_id 必须至少提供一个，否则无法确定消息发送目标
- 当同时提供 user_id 和 group_id 时，将优先使用 message_type 参数判断

# NapCat 开发中
"""