def faktorial(n,m):
    s=1
    for i in range(n,m+1):
        s=s*i
    return len(str(s)) - len(str(s).rstrip("0"))

print(faktorial(2,5))


