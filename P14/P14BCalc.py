def solve(a,b,x,y):
    s0 = set()
    s1 = set()
    for m in range(1,1001):
        s0.add(a+m*x)
        s1.add(b+m*y)
    return s0.intersection(s1)

print(solve(27,76,103,101))