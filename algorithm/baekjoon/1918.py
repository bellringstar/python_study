s = input()

isp = {'+':1, '-':1, '*':2, '/':2, '(':3} #외부
icp = {'+':1, '-':1, '*':2, '/':2, '(':0} #내부
stack = []
ex = ''
for c in s:
    if c.isalpha():
        ex += c
    elif c == '(' or not stack :
        stack.append(c)
    elif c == ')':
        while stack[-1] != '(':
            ex += stack.pop()
        stack.pop()
    elif icp[stack[-1]] < isp[c]:
        stack.append(c)
    else:
        while stack and icp[stack[-1]] >= isp[c]:
            ex += stack.pop()
        stack.append(c)

while stack:
    ex += stack.pop()
print(ex)