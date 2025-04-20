# region model test
from pydantic import BaseModel

def test_model(PydanticModel: type[BaseModel]) -> None:
    """
    全面测试Pydantic模型的有效性
    
    Args:
        PydanticModel: 要测试的Pydantic模型类
    """
    print(f"\n测试模型: {PydanticModel.__name__}")
    
    # 测试1: 使用空字典测试默认值
    print("\n1. 测试默认值:")
    try:
        instance1 = PydanticModel.model_validate({})
        print(f"  ✓ 默认值测试成功: {instance1.model_dump()}")
    except Exception as e:
        print(f"  ✗ 默认值测试失败: {str(e)}")
    


    
    # 测试3: 测试序列化
    print("\n3. 测试序列化:")
    try:
        instance = PydanticModel()
        json_data = instance.model_dump_json(indent=2, exclude_defaults=True)
        print("  ✓ 序列化测试成功:")
        print(f"  JSON输出: \n{json_data}")
    except Exception as e:
        print(f"  ✗ 序列化测试失败: {str(e)}")
    
    # 测试4: 模型结构和字段信息
    print("\n4. 模型结构:")
    print("  字段列表:")
    for field_name, field in PydanticModel.model_fields.items():
        field_type = getattr(field, "annotation", "未知")
        default = getattr(field, "default", "无默认值")
        print(f"  - {field_name}: {field_type} (默认值: {default})")
        
    print("\n测试完成")