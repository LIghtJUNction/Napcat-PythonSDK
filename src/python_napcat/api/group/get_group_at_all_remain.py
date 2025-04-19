"""
获取群 @全体成员 剩余次数 API
用于获取群组中 @全体成员 的剩余使用次数
接口地址: https://napcat.apifox.cn/227245941e0.md

参数:
- group_id: int - 群号

返回:
- can_at_all: bool - 是否可以 @全体成员
- remain_at_all_count_for_group: int - 群内所有管理当天剩余 @全体成员 次数
- remain_at_all_count_for_uin: int - Bot 当天剩余 @全体成员 次数

# NapCat 开发中
"""