# Output questions "What is your name?", "How old are you?", "Where do you live?". /
# Read the answer of user and output next information: "Hello, (answer(name))", /
# "Your age is (answer(age))", "You live in (answer(city))".

print("What is yor name?")
name = input("Please enter your name: ")
print("Hello, " , name , "!")
print("How old are you?")
age = input("Pleace enter your age:")
print("Your age is " + age + ".")
print("Where do you live?")
city = input("Please enter the name of your city:")
print("You live in " + city + ".")
print("Thank you!")