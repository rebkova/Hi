word = input("Which word you want to manipulate?")

vowel = ["a", "e", "i", "o", "u"]
rovar_list = []


for i in range(len(word)):
    rovar_list.append(word[i])
    if word[i] not in vowel:
        rovar_list.append("o")

rovar_str = ''.join(rovar_list)

print(rovar_str)



