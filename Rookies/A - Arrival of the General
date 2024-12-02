n = int(input())
h = list(map(int,input().split()))

max_h = max(h)
min_h = min(h)

mx_indx = h.index(max_h)
mn_indx = n - 1 - h[::-1].index(min_h)

swap_min = n - 1 - mn_indx

total = mx_indx + swap_min
if mx_indx > mn_indx:
    total = total -1
print(total)
