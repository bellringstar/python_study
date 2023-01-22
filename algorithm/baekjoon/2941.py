import sys
input = sys.stdin.readline

cro_alp =['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
inputS = input().rstrip()
counter = 0
for s in cro_alp:
    if s in inputS:
        counter += inputS.count(s)
        inputS = inputS.replace(s, ' ')
       
rst = counter + len(inputS.replace(' ',''))
print(rst)


'''
croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
word = input()

for i in croatia :
    word = word.replace(i, '*')
print(len(word))
'''