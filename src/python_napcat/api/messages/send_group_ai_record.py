"""
发送群AI语音 API
用于在群聊中发送由AI生成的语音消息
接口地址: https://napcat.apifox.cn/229486774e0.md

参数：
- group_id: 目标群号
- text: 要转换为语音的文本内容
- speaker_id: 语音角色ID，用于指定AI语音的声线
- audio_type: 音频类型，可选参数

返回：
- 包含语音消息发送结果的对象

注意：
- 不同的speaker_id对应不同的AI声线角色
- 文本内容长度可能有限制
- 语音生成可能需要一定时间，响应速度受服务器性能影响

# NapCat 开发中
"""