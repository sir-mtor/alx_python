def is_same_class(obj, a_class):
    return type(obj) == a_class

obj_instance = a()
result = is_same_class(obj_instance, ExampleClass)
print(result)  # Output: True

another_instance = "Not a class instance"
result = is_same_class(another_instance, ExampleClass)
print(result)  # Output: False
