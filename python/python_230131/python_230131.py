'''
데코레이터
함수를 어떤 함수로 꾸며서 새로운 기능을 부여 -> 평소처럼 함수 사용해도 추가 기능도 작동
@데코레이터(함수명) 형태로 함수 위에 작성
순서대로 적용 되기 떄문에 작성 순서가 중요
'''
def emoji_decorator(func):
    def wrapper(name): 
        func(name) #전달받은 함수 실행, 파라미텅 있다면 추가
        print("^~^") #원하는 추가 기능

    return wrapper

def ko_hello(name):
    print(f'안녕하세요, {name}님')

@emoji_decorator # ==> en_hello(name) == emoji_decoratort(en_hello)(name)와 동일
def en_hello(name):
    print(f'Hello, {name}!')

# ko_hello('ssafy')
# en_hello('ssafy')
# emoji_decorator(ko_hello)('aiden')

'''
스태틱 메서드
인스턴스 변수, 클래스 변수를 전혀 다루지 않는 메서드 -> 객체 상태나 클래스 상태를 수정할 수 없음
속성을 다루지 않고 단지 기능만을 하는 메서드를 정의할 때 사용
@staticmethod
클래스 안에 있을 뿐인 그냥 함수
'''

class MyClass:

    def method(self):
        return 'instance method', self
    
    @classmethod
    def classmethod(cls):
        return 'class method', cls
    
    @staticmethod
    def staticmethod():
        return 'static method'
    
# my_class = MyClass()
# print(my_class.method())
# print(my_class.classmethod())
# print(my_class.staticmethod())

'''
객체지향의 핵심 개념
1. 추상화
핵심이 되는 부분만 추려서 / 공통적인 부분을 뽑아서 
2. 상속
코드의 재사용성을 상승, 기능을 확장
하위 클래스는 상위 클래스에 정의된 속성,행동,관계 및 제약 조건을 모두 상속받음
부모클래스의 속성, 메서드가 자식 클래스에 상속되므로, 코드 재사용성이 높아짐
super()
자식클래스에서 부모클래스를 사용하고 싶은 경우
파이썬의 모든 클르새는 object로부터 상속됨
메서드 오버라이딩을 통해 자식 클래스에서 재정의 가능함
상속관계에서의 이름 공간은 인스턴스, 자식 클래스, 부모 클래스 순으로 탐색
다중 상속 : 상속으 순서가 중요, 메서드의 이름이 같다 -> 탐색 순서 고려
mro 메서드 : 해당 인스턴스가 어떤 부모 클래스를 가지는지 확인
3. 다형성
각자의 특성에 따라서 다른 결과 도출
서로 다른 클래스에 속해있는 객체들이 동일한 메세지에 대해 다른 방식으로 응답할 수 있다.
메서드 오버라이딩: 부모 클래스에서 저으이한 메서드를 자식 클래스에서 변경
부모클래스의 메서드 이름과 기능을 사용하면서 특정 기능 추가
4. 캡슐화
데이터를 보호
객체의 구현 내용에 대해 외부로부터의 직접적인 액세스를 차단
제어자의 종류
Public Access Modifier: 모두 가능
언더바 없이 시작하는 메서드나 속성/하위 클래스 override 허용
Protected Access Modifier: 상속관계에 있을 때만 가능
_ 1개로 시작. '암묵적'으로 부모 클래스 내부와 자식 클래스에서만 호출 가능/하위 클래스 overrinde 허용
메서드를 통해 데이터를 획득/변경 해야함 self._age 방식을 통해도 얻을수 있지만 암묵적으로 금지
Private Access Modifier: 나만 가능
__(언더바 2개)로 시작. 본 클래스 내부에서만 사용 가능/ 하위,상속,외부 호출 불가능

getter 메서드: 변수의 값을 읽는 메서드
@property 데코레이터 사용
setter 메서드: 변수의 값을 설정하는 성격의 메서드
@변수.setter 사용
'''
class Person:
    def __init__(self):
        self._age = 0

    @property
    def age(self): #getter
        print('getter 호출')
        return self._age
    
    @age.setter
    def age(self, age): #setter
        print('setter 호출')
        self._age = age

    # age = property(get_age, set_age) #퍼블릭 클래스변수 age, 이마저 귀찮아

# p1 = Person()
#p1._age = 25 금지
#print(p1._age) 금지

# p1.set_age(25)
# print(p1.get_age()) 좋지만 귀찮음

# p1.age =25
# print(p1.age) #age = property 과정이 귀찮다 -> 데코레이터 사용

'''
디버깅
Syntax Error = 인터프리터가 해석이 안됨
Exception = 해석은 했는데 이대로 실행하면 안됨

로직에러
1. print를 하나하나 다 찍어본다
2. 전체 코드를 살펴본다
3. 누군가에게 설명해봄

에러를 예외로 제어한다.
에러 처리는 가장 작은 에러부터 처리한다.
try:/ 필수
except: 문제 발생 시 실행/ 필수
else: except 발생 안한 경우/ 옵션
Finally: 반드시 실행 에러가나던 except하던 else하던/ 옵션
'''

#8과제
