"""
转存为永久文件API
用于将临时文件转存为永久文件，常用于将接收到的文件保存到自己的文件系统中
接口地址: https://napcat.apifox.cn/283136366e0.md

参数：
- group_id: 源文件所在群号
- file_id: 源文件ID
- target_group_id: 目标群号
- target_dir_id: 目标文件夹ID，存放到根目录请传入/

返回：
- 文件转存操作的结果信息，包括是否成功的状态及新文件信息

# NapCat 开发中
"""

# 具体实现内容将根据API规范添加