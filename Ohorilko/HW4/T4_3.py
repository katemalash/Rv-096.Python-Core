#The user enters a number, the program must display its description. For example, \
# "positive one-digit", "negative two-digit", etc.
#Питання як тут зробити якщо інше число: наприклад 100
number=int(input("Please, input the number: "))
if number>-9 and number<=9:
    if number>0:
        print("positive one-digit")
    else:
        print("negative one-digit")
else:
    if number >=10 and number<100:
        print("positive two-digit")
    else:
        if number >=-99 and number<=-10:
            print("negative two-digit")
        