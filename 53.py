
l = [-1, 2, 3, -4, 6]
avg = sum(l) / len(l)
for i in range(len(l)):
    if l[i] < 0:
        l[i] = avg
print(l)
