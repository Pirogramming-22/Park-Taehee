num=0
i=0
while(True):
    num = input("부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) : ")
    if num.isdigit():
        num=int(num)
        if 1<=num<=3:
            break
        else:
            print("1, 2, 3 중 하나를 입력하세요")
    else:
        print("정수를 입력하세요")
for i in range(num):
    i+=1
    print("player: ",format(i))