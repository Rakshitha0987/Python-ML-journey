def sum(n):
    s=0
    for i in range(n+1):
        s+=i
    return s
n=int(input("enter n; "))
s=sum(n)
print(s)