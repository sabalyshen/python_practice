sumlist = []
while True:
    a = input('請輸入數字: ')
    if a == 'q':
        break
    a = int(a)
    sumlist.append(a)
    if a == 'q':
        break

print(sumlist)
print(sum(sumlist))