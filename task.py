sp1 = ['ggg', 'bbb', 'fff']
sp2 = [123 , 321 , 213]

def merge_list_to_dict(a=sp1, b=sp2):
    q = zip(a, b)
    d = dict(q)
    return d
print(merge_list_to_dict())
print(merge_list_to_dict(['asdas'], b=[312]))