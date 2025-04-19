"""
发送戳一戳 API
用于向指定好友或群成员发送戳一戳(窗口抖动)消息
接口地址: https://napcat.apifox.cn/250286923e0.md

参数：
- user_id: 接收戳一戳的用户QQ号
- group_id: 群号(可选，如果在群内戳一戳则需要提供)
- poke_type: 戳一戳类型ID
- poke_id: 具体戳一戳表情的ID
- strength: 戳一戳强度(可选)

返回：
- 发送戳一戳的结果状态信息

# NapCat 开发中
"""