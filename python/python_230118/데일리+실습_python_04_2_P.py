students = [
    '박해피',
    '이영희',
    '조민지',
    '조민지',
    '김철수',
    '이영희',
    '이영희',
    '김해킹',
    '박해피',
    '김철수',
    '한케이',
    '강디티',
    '조민지',
    '박해피',
    '김철수',
    '이영희',
    '박해피',
    '김해킹',
    '박해피',
    '한케이',
    '강디티',
]

student_dict = {students.count(name):name for name in students}

res = student_dict

print(sorted(res.items(), reverse=True))