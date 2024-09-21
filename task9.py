#Timofey
start = 1
for count in [1, 2, 3, 4]:
    print(" ".join(str(start + i)for i in reversed(range(count))))
    start += count