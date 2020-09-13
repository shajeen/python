i = 0
i = int(input())
while(i):
    stri = input()
    if (len(stri) > 10):
        first = stri[0]
        end = stri[-1]
        stri = first + str(len(stri)-2) + end
    i = i - 1
    print(stri)