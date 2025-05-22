# 연습문제 11.3 (개념확인 과제)

class Point:
    def __init__ (self, x=0, y=0): # 두 꼭짓점
        self.x = x
        self.y = y

class Rectangle:
    def __init__(self, x1, y1, x2, y2):
        self.lt = Point(x1, y1)
        self.rb = Point(x2, y2)
    
    def show(self): # 현재 사각형의 좌측 상단과 우측 하단 꼭짓점을 화면에 출력력
        print(f'좌측 상단 꼭지점이 ({self.lt.x},{self.lt.y})이고 우측 하단 꼭지점이 ({self.rb.x},{self.rb.y})인 사각형입니다.')
    
    def getWidth(self): # 너비 반환
        return (self.rb.x - self.lt.x)
    def getHeight(self): # 높이 반환
        return (self.lt.y - self.rb.y)
    def getArea(self):
        return (self.getWidth() * self.getHeight())
    def getPerimeter(self):
        return (self.getWidth() + self.getHeight()) * 2
    
    
# 주 프로그램부
r1 = Rectangle(5, 5, 20, 10)
a = r1.getArea()
p = r1.getPerimeter()

r1.show()
print(f'\n넓이는 {a}, 둘레는 {p}')5