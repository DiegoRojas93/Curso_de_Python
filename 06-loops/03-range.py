range1 = range(0, 10, 10)

print( range1 )          # range(0,10)
print( iter(range1) )    # <range_iterator object at 0x7692f15ff480>

for _ in range(0, 10, 2):
    print("Enviar notificación")