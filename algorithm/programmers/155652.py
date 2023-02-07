alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#26문자

# new_idx = idx % 26

arrS = []
arrS.extend(s)
skipArr = []
skipArr.extend((skip))
for s in arrS:
    idx = alpha.index(s) + 5
    new_idx = idx %



