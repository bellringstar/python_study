# 입력 예시
# # mass percent.py 실행 시
# 1.소금물의 농도(%)와 소금물의 양(g)을 입력하십시오: 1% 400g
# 2.소금물의 농도(%)와 소금물의 양(g)을 입력하십시오: 8% 300g
# Done

# 출력 예시
# 4.0% 700.0g
is_on = True
count = 1
salt = []
water = []
while is_on:
    salt_water = input(f'{count}.소금물의 농도(%)와 소금물의 양(g)을 입력하십시오: ').split(" ")
    if salt_water[0] == "Done" or count >= 5:
        con_salt = sum(salt)
        con_water = sum(water)
        con_salt_water = round(con_salt * 100 / con_water, 2)
        print(f'{con_salt_water}% {con_water}g')
        is_on = False
    else:
        salt.append(int(salt_water[0][:-1]) * int(salt_water[1][:-1]) / 100)
        water.append(int(salt_water[1][:-1]))
        count += 1

