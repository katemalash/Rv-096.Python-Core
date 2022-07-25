character_string = '11112hkhjggfdfsdsfghgjkjklk223334445556677+++*******--09089887876yuhjk.lkj,jghhgddgfchbjm45454 hello world'
operators = {'+', '-', '*', '/', '=', '%', '~', '<', '>'}
numbers = {'1', '2', '3', '4', '5', '6', '7', '8', '9', '0'}
line_without_repeats = set()
letter_list = []

for character in character_string:
    if character in numbers or character in operators:
        line_without_repeats.add(character)
    elif character.isalpha() or character == ' ':
        letter_list.append(character)
        
print(character_string)
print(''.join(str(char) for char in line_without_repeats) + ' ' + ''.join(str(char) for char in letter_list))