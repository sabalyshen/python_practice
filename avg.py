def run_times():
    count = 0
    times = 0
    while t := input('請輸入跑10公里所需時間: '):
        try:
            t = float(t)
            times += t
            count += 1
        except Exception as e:
            print('產生錯誤: ', e)
    if count > 0:
        time_avg = times / count
        print(time_avg)
    else:
        print('0.0')

run_times()

#try:
    # 嘗試執行一些程式碼
#except:
    # 當程式出現異常時執行這邊的程式碼