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
请参考 `api.py` 作为标准实现范例。

