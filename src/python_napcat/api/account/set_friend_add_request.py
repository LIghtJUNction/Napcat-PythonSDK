"""
处理好友请求 API
用于处理收到的好友添加请求，可以选择同意或拒绝
接口地址: https://napcat.apifox.cn/226656932e0.md

参数：
- flag: 请求的唯一标识，用来区分不同的好友请求
- approve: 是否同意请求，True为同意，False为拒绝
- remark: 同意时设置的好友备注(可选)
- block: 拒绝时是否加入黑名单(可选)

返回：
- 处理好友请求的结果信息

# NapCat 开发中
"""