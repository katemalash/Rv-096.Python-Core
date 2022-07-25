character_string = input('Enter some characters: ')
operators = {'+', '-', '*', '/', '=', '%', '~', '<', '>'}
numbers = {'1', '2', '3', '4', '5', '6', '7', '8', '9', '0'}
new_character_list = []

for character in character_string:
    if character not in new_character_list and (character in numbers or character in operators):
        new_character_list.append(character)
    elif character.isalpha() or character == ' ':
        new_character_list.append(character)
    
new_character_string = ''.join(str(char) for char in new_character_list)
print(new_character_string)
