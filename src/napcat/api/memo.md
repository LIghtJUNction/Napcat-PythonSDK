# Napcat Python SDK API 开发备忘录

## 开发环境要求
- Python 版本：3.13
- 使用 pydantic 进行数据验证和序列化

## 类型注解规范
- 禁止使用大写开头的已弃用类型，如 `List`、`Dict`、`Optional` 等
- 使用内置类型：`list` 替代 `List`，`dict` 替代 `Dict`
- 使用 `| None` 替代 `Optional`，如：`str | None` 而不是 `Optional[str]`

## 标准 API 类结构

所有 API 类应遵循以下结构：

```python
class SomeAPI(BaseHttpAPI):
    """
    API 名称和功能描述
    用于...功能
    接口地址: https://napcat.apifox.cn/xxx.md

    参数：
    {
      "param1": value1,
      "param2": value2
    }

    返回：
    - 返回数据描述...
    """

    api: str = "/endpoint_path"
    method: Literal['POST', 'GET'] = "POST"  # 或 "GET"
    request: BaseHttpRequest = Request()
    response: BaseHttpResponse[ResponseData] = Response()  # 或 BaseHttpResponse[list[ResponseData]]
```

## 数据模型结构

### 请求模型
```python
class Request(BaseHttpRequest):
    """
    请求参数说明
    """
    param1: type = Field(default=default_value, description="参数1描述")
    param2: type = Field(default=default_value, description="参数2描述")
```

### 响应数据模型
```python
class ResponseData(BaseModel):
    """
    响应数据模型描述
    """
    field1: type = Field(default=default_value, description="字段1描述")
    field2: type = Field(default=default_value, description="字段2描述")
    
    model_config = ConfigDict(
        extra="allow",  # 允许额外字段
        frozen=False,   # 不冻结模型
        populate_by_name=True,  # 通过名称填充字段
        arbitrary_types_allowed=True,  # 允许任意类型
    )
```

### 响应模型
```python
class Response(BaseHttpResponse[DataType]):
    """
    响应参数说明
    """
    pass  # 或添加特定于此响应的字段
```

## 测试方法

所有 API 模块应在文件末尾包含测试代码：

```python
if __name__ == "__main__":
    from ..base.utils import test_model
    # uv pip install -e . 
    # python -m napcat.api.模块路径
    test_model(Request)
    test_model(ResponseData)
    test_model(Response)
```

## API 文件命名规范
- 文件名使用小写，单词间用下划线连接
- 文件名应反映 API 的主要功能，如 `get_friend_list.py`、`send_message.py` 等

## 测试规范
测试文件保存在项目根目录的 test 目录下，文件名格式为：`test_功能名称_客户端类型_版本.py`

测试连接信息：
| 客户端类型 | 连接地址 | 端口 | 默认 token |
|------------|----------|------|------------|
| HTTP 客户端 | 127.0.0.1 | 10144 | 10144 |
| SSE 客户端 | 127.0.0.1 | 10143 | 10143 |
| WebSocket 客户端 | 127.0.0.1 | 10142 | 10142 |wj1

## 代码示例
请参考 `src/napcat/api/account/get_friend_list.py` 作为标准实现范例。

## 已完成的API模块

### 账号相关 (account)
- [x] `get_friend_list.py` - 获取好友列表 API (作者：LIghtJUNction)
- [x] `mark_group_msg_as_read.py` - 标记群消息已读 API (作者：GitHub Copilot)
- [x] `mark_private_msg_as_read.py` - 标记私聊消息已读 API (作者：GitHub Copilot)
- [x] `mark_msg_as_read.py` - 标记消息已读 API (作者：GitHub Copilot)
- [x] `get_login_info.py` - 获取登录号信息 API (作者：GitHub Copilot)
- [x] `get_account_info.py` - 获取账号信息 API (作者：GitHub Copilot)
- [x] `get_friend_group_list.py` - 获取好友分组列表 API (作者：GitHub Copilot)
- [x] `set_signature.py` - 设置个性签名 API (作者：GitHub Copilot)
- [x] `set_online_status.py` - 设置在线状态 API (作者：GitHub Copilot)
- [x] `set_friend_add_request.py` - 处理好友请求 API (作者：GitHub Copilot)
- [x] `send_like.py` - 点赞 API (作者：GitHub Copilot)

### 群聊相关 (group)
- [x] `get_group_list.py` - 获取群列表 API (作者：GitHub Copilot)
- [x] `get_group_info.py` - 获取群信息 API (作者：GitHub Copilot)
- [x] `set_group_ban.py` - 群禁言 API (作者：GitHub Copilot)
- [x] `set_group_whole_ban.py` - 全体禁言 API (作者：GitHub Copilot)
- [x] `set_group_card.py` - 设置群成员名片 API (作者：GitHub Copilot)
- [x] `set_group_add_request.py` - 处理加群请求 API (作者：GitHub Copilot)
- [x] `set_group_special_title.py` - 设置群头衔 API (作者：GitHub Copilot)
- [x] `set_group_portrait.py` - 设置群头像 API (作者：GitHub Copilot)
- [x] `get_essence_msg_list.py` - 获取群精华消息 API (作者：GitHub Copilot)
- [x] `get_group_system_msg.py` - 获取群系统消息 API (作者：GitHub Copilot)
- [x] `set_essence_msg.py` - 设置群精华消息 API (作者：GitHub Copilot)
- [x] `set_group_kick.py` - 群踢人 API (作者：GitHub Copilot)
- [x] `set_group_admin.py` - 设置群管理 API (作者：GitHub Copilot)
- [x] `set_group_leave.py` - 退群 API (作者：GitHub Copilot)
- [x] `set_group_name.py` - 设置群名 API (作者：GitHub Copilot)

### 消息相关 (messages)
- [x] `send_private_msg.py` - 发送私聊消息 API (作者：GitHub Copilot)
- [x] `send_group_msg.py` - 发送群聊消息 API (作者：GitHub Copilot)
- [x] `get_msg.py` - 获取消息详情 API (作者：GitHub Copilot)
- [x] `recall_msg.py` - 撤回消息 API (作者：GitHub Copilot)
- [x] `get_group_msg_history.py` - 获取群历史消息 API (作者：GitHub Copilot)
- [x] `delete_msg.py` - 撤回消息 API (作者：GitHub Copilot)
- [x] `send_forward_msg.py` - 发送合并转发消息 API (作者：GitHub Copilot)

### 系统相关 (system)
- [x] `get_version_info.py` - 获取版本信息 API (作者：GitHub Copilot)
- [x] `account_logout.py` - 账号退出 API (作者：GitHub Copilot)

### 文件相关 (file)
- [x] `upload_group_file.py` - 上传群文件 API (作者：GitHub Copilot)
- [x] `save_to_permanent.py` - 转存为永久文件 API (作者：GitHub Copilot)

### 个人操作 (personal)
- [x] `ocr_image.py` - OCR图片识别 API (作者：GitHub Copilot)

### 密钥相关 (key)
- [x] `get_client_key.py` - 获取Client Key API (作者：GitHub Copilot)
- [x] `get_cookies.py` - 获取Cookies API (作者：GitHub Copilot)