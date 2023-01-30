
class ClassHelper:
    
    def __init__(self, lst):
        self.name_list = lst

    def pick(self, n):
        import random
        return random.sample(self.name_list, n)

    def match_pair(self):
        import random
        pair = []
        while True:
            pick_up = random.sample(self.name_list,2)
            pair.append(pick_up)
            self.name_list.remove(pick_up[0])
            self.name_list.remove(pick_up[1])
            if len(self.name_list) == 3:
                pair.append(self.name_list)
                break
            elif len(self.name_list) == 0:
                break
        return pair








ch = ClassHelper(['김해피', '이해킹', '조민지', '박영수', '정민수'])

print(ch.pick(1))
print(ch.pick(1))
print(ch.pick(2))
print(ch.pick(3))
print(ch.pick(4))

print(ch.match_pair())
