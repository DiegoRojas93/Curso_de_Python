set1 = {1,2,3,4,5}
set2 = {4,5,6,7,8}
set3 = {5,6,7}

symetric_diference_set = set1.symmetric_difference(set2)    # Toma los elementos que no esten en la intersección de dos conjuntos
issubset_set = set3.issubset(set2)                          # Un conjunto es sub-conjunto de otro conjunto
issuperset_set =  set2.issuperset(set3)                     # Un conjunto es super-conjunto de otro conjunto

print(f"""
symetric_diference_set: {symetric_diference_set}
issubset_set: {issubset_set}
issuperset_set: {issuperset_set}
""")