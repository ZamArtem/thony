
t = [12, 4, 3, 67, 8, 9]
n = len(t)
for i in range(n-1,0,-1):
    for j in range(0,i):
        if t[j] > t[j+1]:
            x = t[j+1]
            t[j+1] = t[j]
            t[j] = x
print(t)
