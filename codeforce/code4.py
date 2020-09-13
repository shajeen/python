n, k = input().split(" ")
a = input().split(" ")
rank = a[int(k) - 1]
result = 0
for i in a:
    if ((int(i) >= int(rank)) and (int(i) != 0)):
        result += 1

print(result)
