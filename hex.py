
def hex_trans(hex_num):
    ten_hex = 0
    for index, char in enumerate(reversed(hex_num)):
        if char.isdigit():
            num = int(char)
        else:
            num = ord(char.upper()) - ord('A') + 10
        ten_hex += (16 ** index) * num
    print(ten_hex)
    
#ASCII碼
print(ord('A'))
print(ord('F'))
hex_trans('205F')

h = '251'
dexnum = int(h, 8) #10進位轉8進位
print(dexnum)
dexnum = int(h, 16) #10進位轉16進位
print(dexnum)