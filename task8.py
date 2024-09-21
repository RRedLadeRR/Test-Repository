#Timofey
h = 1
for a in [1, 3, 5]:
    print(" ".join(str(x) for x in range(h, h + a)))
    h += a