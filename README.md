# Napcat Python SDK

## ***介绍***

> 本项目原为AIVK项目前置 功能抽离出来供其他项目使用
> 目前正在开发中
> 设计为MCP服务

**客户端实现**

* [X] [HTTP客户端](https://github.com/LIghtJUNction/Napcat-PythonSDK/blob/main/src/napcat/clients/http) - 支持同步和异步请求
* [X] [SSE客户端](https://github.com/LIghtJUNction/Napcat-PythonSDK/blob/main/src/napcat/clients/sse/) - 支持事件流接收
* [X] [WebSocket客户端](https://github.com/LIghtJUNction/Napcat-PythonSDK/blob/main/src/napcat/clients/websocket/) - 支持双向实时通信

**服务端实现**

* [ ] [HTTP](https://github.com/LIghtJUNction/Napcat-PythonSDK/blob/main/src/napcat/severs/http/)Napcat服务器
* [ ] WebSocket 服务器

# FastNapcat

综合上述所有客户端，并优化使用体验

**全部端点**

* [] [API](https://github.com/LIghtJUNction/Napcat-PythonSDK/blob/main/data/api_tree.json)

# 贡献指南

* uv pip install -e .[dev]

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

## 代码注释规范

* 所有类、方法和函数都应该有文档字符串
* API类需包含完整的功能描述、接口地址、参数和返回值说明
* 复杂逻辑应添加行内注释
* 推荐使用 # region 和 # endregion 区域划分代码，方便阅读

## API开发规范

* 参考 `src/napcat/api/memo.md` 中的规范进行开发
* 所有API实现都应遵循标准API类结构
* 使用pydantic进行数据验证和序列化
* 每个API文件末尾应包含测试代码

## AI使用规范

请准备好合适的提示词
例如：llms.txt

## 不接受的PR

pyright检查不通过的PR
大量使用Any类型标注的PR
注释不清楚的PR
不符合项目编码风格的PR
缺少测试代码的PR

## 代码规范

pyright 检查通过即为规范
推荐使用 # region 区域划分代码 方便阅读
欢迎使用script/pyupgrade.py脚本 来自动化部分升级代码到python3.13规范
