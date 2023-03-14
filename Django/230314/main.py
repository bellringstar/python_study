'''
Framework
자주쓰는, 재사용 가능한 코드들을 모아 놓은 것
=> 서비스 개발에 필요한 기능들을 미리 구현해서 모아 놓은 것
Frame(뼈대,틀)을 가져와 Work 일한다.
틀에는 규약이 존재한다. 즉 Framework는 개발을 위한 도구들과 규약을 제공해준다.

장점
1. 개발속도 향상
2. 검증 된 코드를 사용할 수 있다 
3. 반복이 감소
4. 해당 프레임워크에는 규약이 있기 때문에 협업이 용이해진다
-> 생산성 증가
단점
1. 선택의 폭이 좁아진다.
2. 러닝커브(학습곡선)가 존재

Django
1. Python으로 작성된 프레임워크
2. 다양한 유용한 기능들
3. 검증된 웹 프레임워크 ex)화해, Toss, 두나무, 당근마켓, 요기요...

클라이언트-서버 구조
requests/resopnese
클라이언트
- 웹 사용자의 인터넷에 연결된 장치
- 웹 브라우저
- 서비스를 요청하는 주체
서버
- 웹페이지, 사이트, 또는 앱을 저장하는 컴퓨터
- 클라이언트가 웹 페이지에 접근하려고 할 때 서버에서 클라이언트 컴퓨터로 웹 페이지 데이터를 응답해
사용자의 웹 브라우저에 표시됨
- 요청에 대해 서비스를 응답하는 주체

python -m venv venv
source venv/Scripts/activate <->deactivate
pip freeze > requirements.txt
pip install -r requirements.txt

django-admin startproject fistpjt
python manage.py runserver


settings.py
Django 프로젝트 설정을 관리

urls.py
처리하고싶은 url이 있는 곳.
각각의 url에 따라 원하는 작동을 views에 작성. 연결

python manage.py startapp articles
app = 하나의 큰 기능 단위
단일 app으로 개발해도 됨. 개발자의 판단

admin.py
관리자용 페이지
models.py
app에서 사용하는 Model을 정의하는 곳
MTV 패턴의 M
views.py
view 함수들(우리 app의 logic,기능)이 정의되는 곳
MTV 패턴의 V

***** app을 사용하기 위해서는 반드시 settings.py에 INSTALLED_APPS 리스트에 추가해야함

Django의 세가지 구조
MTV = Model, View, Template
URL -> VIEW ->TEMPLATE
'''

