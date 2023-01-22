import sys
input = sys.stdin.readline

alp_dict = {('A','B','C'):2, ('D', 'E', 'F'):3, ('G', 'H', 'I'):4, ('J', 'K', 'L'):5,
('M', 'N', 'O'):6, ('P', 'Q', 'R', 'S'):7, ('T', 'U', 'V'):8, ('W', 'X', 'Y', 'Z'):9}

string = input()
rst = 0
for s in string:
    for key in alp_dict.keys():
        if s in key:
            rst += alp_dict[key] + 1
    
print(rst)
