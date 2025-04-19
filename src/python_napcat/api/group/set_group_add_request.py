"""
处理加群请求 API
用于处理入群请求/邀请
接口地址: https://napcat.apifox.cn/226656947e0.md

参数:
- flag: str - 加群请求的flag（需从上报的数据中获得）
- sub_type: str - add或invite，请求类型（需从上报的数据中获得）
- approve: bool - 是否同意请求/邀请
- reason: str - 拒绝理由（仅在拒绝时有效）

返回:
- 操作结果

# NapCat 开发中
"""