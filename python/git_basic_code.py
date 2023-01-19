# - `git config --global user.name {name}`
# - `git config --global user.email {email}`
# - `git init`
# - 깃 레포 만들기
# - `git add {파일 이름}`
# - staging area에 추가
# - `git commit -m '{message}'`
# - 커밋(기록) 남기기
# - `git status`
# - 상태 확인
# - `git log`
# - 커밋 확인
# - `git log --oneline`
# - `git remote add origin {url}`
# - 원격 연결
# - `git push origin master`
# - 업로드
# - `git push -u origin master`


# - `git clone {url}`
# - 깃허브에 있는 깃 새로 가져오기
# - `git pull origin master`
# - 이미 연결된 상태에서 당겨오기

# 
# add -> commit -> push/pull

'''
누군가 만든 프로젝트 깃허브 받기
프로젝트 파일 수정 후 git add . -> git commit -m "~~~" -> git push origin master (X)
master = 최종 프로덕트 따라서 신입주제에 수정하고 바로 넣지마라
따라서 master라는 브랜치 대신 신입을 위한 새로운 공간을 파준다 
git checkout -b @@@@@ ex) git checkout -b freshman   freshman을 위한 공간
-> git push origin freshman
그러면 깃헙에 들어가보면 compare & pull request 팝업 -> 거기에 들어가서 마스터에 체크 바란다는 등의 내용 작성 후 pull request
== master로 갈수있게 허락해주세요

깃 마스터가 들어가서 보면 커밋의 내용이 보임. 보고 판단 후 괜찮다면 Merge pull request == 실제 마스터에 병합.

내가 쓰던 중 커밋돼서 소스코드가 갱신됨 -> 확인 후 pull origin master를 통해 변화를 받아옴 = 동기화 / 내가 쓰고있던 코드가 나갈라가면 안된다.->
add/commit을 해서 저장 -> 그 후 pull origin master를 통해 동기화
'''