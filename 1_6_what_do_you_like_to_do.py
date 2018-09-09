# list = [""]
#
# if list != "stop":
#     hobbies = input("What do you like to do?")
#     list.append(hobbies)
#
# else:
#     print("OK. Hobbies are {}.".format(list))



hobbies = []

while "stop" not in hobbies:
    hobby = input("What do you like to do?")
    hobbies.append(hobby)

else:
    del hobbies[-1]
    print("OK. Hobbies are {}.".format(hobbies))






# infinite loop with the question - works
# interupeted with the stop answer - works
# use list.format()
#     print(inventory"")