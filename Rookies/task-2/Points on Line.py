import bisect
n,d = map(int,input().split())
a = list(map(int,input().split()))
total = 0
for i in range(n):
    k = bisect.bisect_right(a,a[i] + d)
    points = k - i - 1
    if points >= 2:
        total += points * (points - 1) // 2
print(total)
