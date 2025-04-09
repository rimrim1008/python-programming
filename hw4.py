# hw4

# 사용자 정의 함수
def rep_char(c,n):
    print(c*n)

def draw_line_string(name):
    msg1 = f'Hello {name},'
    msg2 = 'Welcome to Seoul.'
    
    nstr = max(len(msg1),len(msg2))
    rep_char('-',(nstr+2))
    print(f' {msg1} ')
    print(f' {msg2} ')
    rep_char('-',nstr+2)


# 주 프로그램부
name = input('Input his/her name: ')
draw_line_string(name)