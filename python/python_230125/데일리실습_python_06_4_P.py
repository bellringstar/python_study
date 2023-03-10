import collections

entry_record = ['이싸피', '박장고', '조실습', '이싸피', '조실습', '오디비', '임온실', '조실습', '조실습', '이싸피', '안도둑', '임온실', '최이썬', '오디비', '안도둑', '염자바', '박장고', '조실습',
                '최이썬', '조실습', '염자바', '박장고', '임온실', '임온실', '이싸피', '임온실', '오디비', '조실습', '염자바', '임온실', '박장고', '최이썬', '안도둑', '염자바', '임온실', '박장고', '이싸피', '안도둑',
                '임온실', '오디비', '최이썬', '안도둑', '이싸피', '오디비', '안도둑', '이싸피', '박장고', '박장고', '안도둑', '안도둑', '안도둑', '염자바', '최이썬', '오디비', '오디비', '최이썬', '이싸피', '임온실', '안도둑']

exit_record = ['최이썬', '조실습', '이싸피', '안도둑', '임온실', '안도둑', '이싸피', '오디비', '염자바', '박장고', '최이썬', '이싸피', '염자바', '염자바', '박장고', '임온실', '이싸피',
               '박장고', '안도둑', '염자바', '이싸피', '조실습', '조실습', '임온실', '박장고', '이싸피', '조실습', '박장고', '오디비', '안도둑', '조실습', '임온실', '안도둑', '안도둑', '임온실', '조실습', '최이썬', '안도둑', '임온실',
               '염자바', '이싸피', '임온실', '안도둑', '오디비', '안도둑', '오디비', '임온실', '염자바', '임온실', '박장고', '조실습', '이싸피', '최이썬', '최이썬', '오디비', '오디비', '염자바', '오디비', '안도둑', '박장고']


entry_count = collections.Counter(entry_record)
exit_count = collections.Counter(exit_record)

# count_num = 0
# print('입장 기록 많은 Top3')
# for name,count in sorted(entry_count.items(), key=lambda x: x[1], reverse=True):
#     if count_num == 3:
#         break
#     print(f'{name} {count}회')
#     count_num += 1

# for name in entry_count:
#     gap = entry_count[name] - exit_count[name]
#     if gap != 0:
#         if gap > 0:
#             print(f'{name}은 입장 기록이 {gap}회 더 많아 수상합니다.')
#         else:
#             print(f'{name}은 퇴장 기록이 {-gap}회 더 많아 수상합니다.')
print('입장 기록 많은 Top3')
for t in entry_count.most_common(3):
    print(f'{t[0]} {t[1]}회')

print('\n출입 기록이 수상한 사람')
entry_count.subtract(exit_count)
for counter in entry_count:
    if entry_count[counter] > 0:
        print(f'{counter}은 입장 기록이 {entry_count[counter]}회 더 많아 수상합니다.')
    elif entry_count[counter] < 0:
        print(f'{counter}은 퇴장 기록이 {-entry_count[counter]}회 더 많아 수상합니다.')
