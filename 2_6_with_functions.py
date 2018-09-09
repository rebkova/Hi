def is_vowel(x):
    for i in range(len(vowel)):
        if vowel[i] == x:
            return True
    return False

def not_vowel(x):
    for v in vowel:
        if v == x:
            return False
    return True

word = input("Which word you want to manipulate?")

vowel = ["a", "e", "i", "o", "u"]
rovar_list = []


for i in range(len(word)):
    rovar_list.append(word[i])
    if not_vowel(word[i]):
        rovar_list.append("o")

rovar_str = ''.join(rovar_list)
print(rovar_str)


