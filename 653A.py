n = map(int, raw_input().split())
bs = list(map(int, raw_input().split()))


def for_friends(balls):
    for b in balls:
        l = [x1 for x1 in balls if abs(b - x1) <= 2 and b != x1]
        for x1 in l:
            l1 = [x2 for x2 in balls if abs(b - x2) <= 2 and abs(x1 - x2) <= 2 and x2 != x1 and x2 != b]
            if l1:
                return "YES"
    return "NO"


ans = for_friends(bs)
print ans
