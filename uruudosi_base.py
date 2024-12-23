

def checkUruu(birth):

    if birth < 1582: # 定義されていない年代
        print(f'{birth}年は閏年という概念が存在しません')
    elif birth % 400 == 0:
        print(f'{birth}年は閏年です')
    elif birth % 100 == 0:# 平年
        print(f'{birth}年は閏年ではありません')
    elif birth % 4 == 0:
        print(f'{birth}年は閏年です')
    # その他すべて平年
    else: 
        print(f'{birth}年は平年です')



birth = int(input("西暦を入力してください: "))
checkUruu(birth)
