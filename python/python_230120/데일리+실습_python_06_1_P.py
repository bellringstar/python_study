# A. 입력예시
# de_identify('970103-1234567')
# de_identify('8611232345678')

# B. 출력예시
# 970103*******
# 861123******* 

def de_identify(idnum):
    return idnum[:6]+"*"*7

print(de_identify('970103-1234567'))
print(de_identify('9701031234567'))