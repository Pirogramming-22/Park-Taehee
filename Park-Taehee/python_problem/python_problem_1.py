num=0
i=0

def brGame():
    while (True):
        num = input("부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) : ")
        if num.isdigit():
            num = int(num)
            if 1 <= num <= 3:
                return num
            else:
                print("1, 2, 3 중 하나를 입력하세요")
        else:
            print("정수를 입력하세요")

while(True):
    num=brGame()
    out=0
    for out in range(num):
        i += 1
        print("playerA: ", format(i))
        if i==31:
            print("playerB win!")
            exit()
    num=brGame()
    out = 0
    for out in range(num):
        i += 1
        print("playerB: ", format(i))
        if i==31:
            print("playerA win!")
            exit()