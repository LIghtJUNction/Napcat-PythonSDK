"""
贴表情 API
用于在消息上添加表情回应(类似Discord的消息反应功能)
接口地址: https://napcat.apifox.cn/226659104e0.md

参数：
- message_id: 目标消息ID
- emoji_id: 表情ID
- op: 操作类型，1=添加，2=移除

返回：
- 操作结果

注意：
- 部分群聊可能未开启此功能
- 表情ID需要使用系统支持的特定表情

# NapCat 开发中
"""