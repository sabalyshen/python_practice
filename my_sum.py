def my_sum():
    num_sum = 0
    while True:
        num = input('請輸入數字: ')
        if num.isdigit():
            num = int(num)
            num_sum += num
        elif num == 'q':
            break
        else:
            print('請輸入數字!!')
    print(num_sum)


my_sum()    
