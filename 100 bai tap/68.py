l = list(map(int, input().split()))

gtmax=max(l)
gtmin=min(l)
vtmax = l.index(max(l))
vtmin = l.index(min(l))

l[vtmax]=gtmin
l[vtmin]=gtmax

print(*l)