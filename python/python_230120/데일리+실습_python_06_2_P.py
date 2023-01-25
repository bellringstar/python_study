grain_lst = [('고구마',3000), ('감자',2000), ('옥수수',4500),('토란',1300)]
max_price = grain_lst[0][1]
max_grain =''
for grain in grain_lst:
    if grain[1] > max_price:
        max_price = grain[1]
        max_grain = grain[0]

print(max_grain)
