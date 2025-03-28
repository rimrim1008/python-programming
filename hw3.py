# 사용자 정의 함수수
def get_fixed_price(rate, dis_price):
    price = dis_price / (1-(rate/100))
    return(price)
    

# 주 프로그램부
rate_dis = int(input('할인율은? '))
a_dis = int(input('A 상품의 할인된 가격은? '))
b_dis = int(input('B 상품의 할인된 가격은? '))

a_price = int(get_fixed_price(rate_dis, a_dis))
b_price = int(get_fixed_price(rate_dis, b_dis))

print(f'A 상품의 정가는 {a_price}원')
print(f'B 상품의 정가는 {b_price}원')