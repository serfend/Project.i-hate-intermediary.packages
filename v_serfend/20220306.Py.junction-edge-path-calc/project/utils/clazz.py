# 将class转dict,以_开头的属性不要
def dict2props(obj):
    pr = {}
    for name in dir(obj):
        value = getattr(obj, name)
        if not name.startswith('__') and not callable(value) and not name.startswith('_'):
            pr[name] = value
    return pr


# 将class转dict,以_开头的也要
def class2props_with_(obj):
    pr = {}
    for name in dir(obj):
        value = getattr(obj, name)
        if not name.startswith('__') and not callable(value):
            pr[name] = value
    return pr

# dict转obj，先初始化一个obj
def dict2obj(obj,dict):
    obj.__dict__.update(dict)
    return obj