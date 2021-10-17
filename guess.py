import random
def guessing_game():
    num = random.randint(0, 100)
    while True:
        g = input('請猜1-99的數字: ')
        if g.isdigit():
            g = int(g)
            if g > num:
                print('小一點喔! ')
            elif g < num:
                print('大一點喔! ')
            elif g == num:
                print('猜對了!!')
                break
            elif g >= 100:
                print('請輸入1-99的數字。')
        else:
            print('請輸入數字喔!!')

guessing_game()