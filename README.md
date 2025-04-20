# Napcat Python SDK
## 介绍
本项目原为AIVK项目前置 功能抽离出来供其他项目使用
目前正在开发中
设计为MCP服务 采用 pydanticV2 进行验证 以下类型标注规范均基于pydanticV2 python3.10+ 规范



# 贡献指南

## 序言
推荐使用vscode + pyright
然后打开插件设置，进行基础设置

## 类型标注
启用严格模式
使用list代替List 而无需额外导入：from typing import List
使用dict代替Dict 而无需额外导入：from typing import Dict
使用tuple代替Tuple 而无需额外导入：from typing import Tuple
使用set代替Set 而无需额外导入：from typing import Set
使用deque代替Deque 而无需额外导入：from collections import deque
使用type代替Type 而无需额外导入：from typing import Type

使用 | None 代替 Optional
使用 | 代替 Union

## AI使用规范
请准备好合适的提示词
例如：llms.txt

## 不接受的PR
pyright检查不通过的PR
大量使用Any类型标注的PR
注释不清楚的PR

## 代码规范
pyright 检查通过即为规范
推荐使用 # region 区域划分代码 方便阅读
欢迎使用script/pyupgrade.py脚本 来自动化部分升级代码到python3.13规范
