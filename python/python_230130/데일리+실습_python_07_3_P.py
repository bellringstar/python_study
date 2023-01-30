# 1 + 2
# 2 – 1
# 3 * 4
# 4 / 0

class Calculator:

    # def __init__(self, a, b):
    #     self.a = a
    #     self.b = b

    def add(self,a,b):
        return a + b
    
    def substract(self,a,b):
        return a - b
    
    def multuply(self,a,b):
        return a * b
    
    def divide(self,a,b):
        if b == 0:
            return '0으로 나눌 수 없습니다.'
        else:
            return a / b
        

p1 = Calculator()
print(p1.divide(1,0))