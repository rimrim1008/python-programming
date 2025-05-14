# hw8
shopping_bag = {}
print('[구입]')
while True:
    item = input('상품명? ')
    if item == '':
        break
    else:
        su = int(input('수량은? '))
        shopping_bag[item] = su
        print(f'장바구니에 {item} {su}개가 담겼습니다.')
print('>>> 장바구니 보기:', shopping_bag)

print('\n[검색]')
a = input('장바구니에서 확인하고자 하는 상품은? ')
if a in shopping_bag:
    print(f'{a}은(는) 장바구니에 {shopping_bag[a]}개 담겨 있습니다.')
else:
    print(f'장바구니에 {a}은(는) 없습니다.')