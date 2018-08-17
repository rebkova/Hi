word = input("Which word would you like to mess up with? \n")

upper = word.upper()
backwards = ''.join(reversed(upper))

print(backwards)

#join function to change the type of reversed to string