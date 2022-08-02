'''Task #2 
Output questions “What is your name?“,
“How old are you?“, Where do you live?“. Read the answer of user and output next information:
“Hello, (answer(name))“, “Your age is  (answer(age))“, “You live in  (answer(city))“ '''

name = input('What is your name? ').title()
try:
    age = int(input('How old are you? '))
except:
    print('You entered not only numbers, so your age will be 100 years old:)')
    age = 100
city = input('Where do you live ').title()

print(f'''=========================
Hello, {name}.
Your age is {age}.
You live in {city}.''')