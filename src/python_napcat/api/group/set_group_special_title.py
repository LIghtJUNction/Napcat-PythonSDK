"""
设置群头衔 API
用于设置群成员的专属头衔
接口地址: https://napcat.apifox.cn/226656931e0.md

参数:
- group_id: int - 群号
- user_id: int - 要设置的QQ号
- special_title: str - 专属头衔，不填或空字符串表示删除专属头衔
- duration: int - 专属头衔有效期，单位秒，-1 表示永久，不过此项似乎没有效果，可能是只有某些特殊的时间长度有效

返回:
- 操作结果

# NapCat 开发中
"""