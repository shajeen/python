overall = 0
i = int(input())
while i:
    solve = 0
    for j in range(0,3):
        temp = int(input())
        solve += temp
    
    if solve >= 2:
        overall += 1
    i -= 1
print(overall)
