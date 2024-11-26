# 创建列表
lst = [1, 2, 3, 4, 5]
# 增加元素
def add(a = None, b = None, c = None):
    """增加元素"""
    if a is not None:
        lst.append(a)

    if b is not None:
        lst.remove(b)

    if c is not None:
        if c in lst:
            print(f"查找的值索引为{c}值为:{lst[c]}")

    return lst

Add = add(a=9)
Add = add(b=2)
Add = add(c=3)
print(lst)


        # lst.append(6)          # [1, 2, 3, 4, 5, 6]
        # lst.extend([7, 8])     # [1, 2, 3, 4, 5, 6, 7, 8]
        # # 删除元素
        # lst.remove(3)          # [1, 2, 4, 5, 6, 7, 8]
        # element = lst.pop(0)   # element = 1, lst = [2, 4, 5, 6, 7, 8]
        # # 查找元素
        # index = lst.index(5)   # index = 2
        # # 排序
        # lst.sort(reverse=True) # [8, 7, 6, 5, 4, 2]
