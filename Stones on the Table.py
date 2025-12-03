x = int(input())
y = input().strip()
c = 0
for i in range(1,x) :
    if y[i] == y[i - 1] :
        c +=1
print(c)