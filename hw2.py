
def exchange(don):
    n500 = don // 500 #500원 지불 개수
    don %= 500 #500원으로 바꾸고 남은 잔돈

    n100 = don // 100 #100원 수
    don %= 100 #100원까지 바꾸고 남은 돈

    n50 = don // 50 # 50원 수
    don %- 50 #50원까지 바꾸고 남은 돈

    n10 = don // 10 #10원 수

    print("500원 동전의 개수:", n500)
    print("100원 동전의 개수:", n100)
    print("50원 동전의 개수:", n50)
    print("10원 동전의 개수:", n10)

def integer(prompt):
    res = int(input(prompt))
    return res

#주 프로그램부
don = int(input("동전으로 교환하고자 하는 금액은?"))
exchange(don)


