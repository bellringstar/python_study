vowels = ['a', 'e', 'i', 'o', 'u']
def count_vowels(string):
    count = 0
    for s in string:
        if s in vowels:
            count +=1
    return count

print(count_vowels('apple')) #=> 2
print(count_vowels('banana')) #=> 3