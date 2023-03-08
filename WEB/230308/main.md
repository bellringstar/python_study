## css
>css는 모든것이 박스 형태다

>원칙1. 모든 요소는 box-model, 왼쪽에서부터 오른쪽으로 위에서부터 아래쪽으로 쌓인다. = 행우선 탐색같다.

하나의 박스는 4 영역으로 나누어진다
- content<br>  
  글이나 이미지 등 요소의 실제 내용
- padding<br>
   테두리 안쪽
- border<br>   
   테두리
- margin<br>
   테두리 바깥의 외부 여백<br>
   배경색 지정 가능

>margin: x x = + 상,하/좌,우<br>
margin: x x x = %나누기 상/좌우/하<br>
margin: x x x x = 시계방향 

>box-sizing의 default는 content-box<br>
하지만 box-sizing을 border-box로 설저앟면 border까지 사이즈 설정

>원칙2. display에 따라 크기와 배치가 달라진다.

- 인라인<br>
  content 영역만 차지 span,a...= display:Inline<br>
  width,height,margin-top,margin-bottom 지정할 수 없다.
- 블록<br>
  한 block을 차지 div,p...=display:block
