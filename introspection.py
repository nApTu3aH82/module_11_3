def summ(first, second):
    summa = first + second
    return summa


def introspection_info(obj):
    info_list = {}
    info_list['type'] = str(type(obj))[8:-2]
    obj_type = type(obj).__name__
    attrib = dir(obj)
    methods = [method for method in attrib if callable(getattr(obj, method))]
    module = obj.__class__.__module__
    info_list = {'type': obj_type, 'attributes': attrib, 'methods': methods, 'module': module}
    return info_list


number_info = introspection_info(42)
print(number_info)

number_info = introspection_info(summ('AD', 'CD'))
print(number_info)

