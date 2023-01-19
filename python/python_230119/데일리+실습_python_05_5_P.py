words_dict = {'proper' : '적절한',
'possible' : '가능한',
'moral' : '도덕적인',
'patient' : '참을성 있는',
'balance' : '균형',
'perfect' : '완벽한',
'logical' : '논리적인',
'legal' : '합법적인',
'relevant' : '관련 있는',
'responsible' : '책임감 있는',
'regular' : '규칙적인'}

'''
in + b,m,p -> im-
in + l -> il-
in + r -> ir-
'''

change = [['b', 'm', 'p'], ['l'], ['r']]
key_list = list(words_dict.keys())
not_list = []
for key_word in key_list:
    if key_word[0] in change[0]:
        key_word = 'im' + key_word 
    elif key_word[0] in change[1]:
        key_word = 'il' + key_word
    elif key_word[0] in change[2]:
        key_word = 'ir' + key_word
    not_list.append(key_word)

print(not_list)
    