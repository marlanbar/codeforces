n, a, b = map(int, raw_input().split())

res = (a + b) % n
if res == 0:
    print n
else:
    print res
