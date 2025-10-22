set1 = {1,2,3,4,5}
set2 = {4,5,6,7,8}

union_set = set1.union(set2)                    # Une todos los elementos
intersection_set = set1.intersection(set2)      # Trae solo los elementos que comparten entreellos: 4,5
difference_set =  set1.difference(set2)         # Trae solo los elementos que no pertenescan o se intesecten con el otro conjunto: 1,2,3

print(f"""
union_set: {union_set}
intersection_set: {intersection_set}
difference_set: {difference_set}
""")