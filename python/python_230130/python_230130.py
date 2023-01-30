'''
OOP(Object-Oriented Programming)
1. 절차지향 프로그래밍
하나의 프로그램이 유기적으로 모든 절차가 기술되어 있는 것. 하나의 흐름
기능 중심 프로그램 / 순서가 정해져 있어 실행이 빠름
하지만 프로그램이 커질수록 수정이 복잡해지고 생산 속도가 느려짐

2. 객체지향 프로그래밍
절차 대신 '데이터'를 중심으로 생각
데이터를 중심으로 절차를 도입해서, 현실의 사물을 나타내고 이런 것들을 조립하는 방식으로 개발
여러개의 독립된 객체들과 그 객체간의 상호작용으로 파악
객체 [data, methods...] 데이터와 기능(메서드)분리
'추상화'된 구조 

class Person:

    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
    
    def greeting(self):
        print(f'안녕하세요, {self.name}입니다.')

jimin = Person('지민', '남')
Jimin.greeting() # 안녕하세요, 지민입니다.

장점
1. 재사용의 용이성
2. 객체는 그 자체로 데이터와 행동이 정의됨(독립정) == 내부 구조를 몰라도 가져다 쓸 수 있다.
3. 객체 단위로 모듈화시켜 개발할 수 있으므로 많은 인원이 참여하는 대규모 소프트웨어 개발 가능
4. 개발 용이성, 유지 보수 편의성, 신뢰성을 바탕으로 생산성이 대폭 증가
단점
1. 설계 시 많은 노력과 시간이 필요함
다양한 객체들의 상호 작용 구조를 만들기 위해 많은 노력과 시간이 필요
2. 실행 속도가 상대적으로 느림
절차 지향 프로그래밍이 컴퓨터의 처리구조와 비슷해서 실행 속도가 빠름


OPP기초
객체: 컴퓨터 과학에서 객체 또는 오브첵트는 '클래스에서 정의한 것을 토대로 메모리에 할당된 것'으로
프로그램에서 사용되는 데이터 또는 식별자에 의해 참조되는 공간을 의미, 변수,자료 구조, 함수 또는 메서드가 될 수 있다.
속성(Data)과 행동(Method)으로 구성된 모든 것

클래스로 만든 객체를 '인스턴스' 라고도 함

파이썬은 사실 모든것이 객체다.

클래스 정의 = 나만의 타입을 만든다.
isinstance(instance, class)

객체비교하기 
1. ==
equal
객체가 동등한(내용이 같은)경우 True
두 객체가 같아 보이지만 실제로 동일한 대상을 가리키고 있다고 확인해 준 것은 아님
2. is
동일한(identical)
두 변수가 동일한 객체를 가리키는 경우 True

속성(attribute)
클래스 변수
인스턴스 변수
인스턴스에서 특정 속성에 접근하면, 인스턴스-클래스 순으로 탐색

self
인스턴스 자기자신

메서드의 종류
1. 인스턴스 메서드
most common
Must have self parameter
No decorator needed
Can be accessed through object
인스턴스 변수를 사용하는 함수를 만들고 싶을 때
1-1. 매직 메서드
(__)가 있는 메서드. 특정 상황에 자동으로 불리느 ㄴ메서드 ex)__init__(self)

2. 클래스 메서드
Doesn't need self parameter
Need cls as parameter
Need decorator @classmethod
Can be accessed directly through the class. Don't need instance of class
클래스 단위에서 공통적으로 갖고싶을 때, 클래스가 사용

class Person:
    count = 0
    
    def __init__(self, name):
        self.name = name
        Person.count += 1
    @classmethod
    def number_of_population(cls):
        print(f'인구수는 {cls.count}입니다.')
person1 = Person('이찬혁')
person2 = Person('아이유')

Person.number_of_population() #2
person1.number_of_population() #2
person2.number_of_population() #2

3. 정적 메서드
그 외
'''
#7주차 실습/ 과제: 7주차 1,2번

