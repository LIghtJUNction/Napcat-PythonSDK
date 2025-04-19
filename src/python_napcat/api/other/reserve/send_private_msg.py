"""
发送私聊消息 API (保留版本)
用于向指定好友发送消息，是保留的旧版本接口
接口地址: https://napcat.apifox.cn/226656553e0.md

参数：
- user_id: 对方QQ号
- message: 要发送的消息内容
- auto_escape: 消息内容是否作为纯文本发送，为true则message内容不解析CQ码，默认为false

返回：
- 包含消息ID等信息的对象

注意：
- 此API是保留的旧版本接口，建议使用新版API
- 消息内容支持多种格式，包括纯文本、表情、图片等
- 可能需要好友关系才能发送成功

# NapCat 开发中
"""