list1 = [1,2,3,4,5,6,7,8,9,10,6,4,5,8,9]
tuple1 = tuple(list1)
set1 = set(tuple1)

tuple_list = [('a',1), ('b',2), ('c',2)]
dict1 = dict(tuple_list)

print(f"""
list1: {list1},
tuple1: {tuple1},
set1: {set1},
tuple_list: {tuple_list},
dict1: {dict1}
""")