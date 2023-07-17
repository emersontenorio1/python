n = int(input())
s = set(map(int, input().split()))

s.pop()
s.remove(9)
s.discard(9)
s.discard(8)
s.remove(7)
s.pop()
s.discard(6)
s.remove(5)
s.pop()
s.discard(5)

for inteiros in s:
    if inteiros > 0:
        print(inteiros, end="")