character_string_lower = '123456789abcdefg'
character_string_upper = '123456987FGHIJKLOMNPQ'
set_lower_str =set()
set_upper_str = set()

for character in character_string_lower:
    if character.isalpha():
        set_lower_str.add(character)
        
character_string = character_string_upper.lower()
for character in character_string:
    if character.isalpha():
       set_upper_str.add(character)

set_letters_both_str = set_lower_str.intersection(set_upper_str)
set_letters_lower_str = set_lower_str.difference(set_upper_str)
set_letters_upper_str = set_upper_str.difference(set_lower_str)

print(f'Those are letters from both strings {dict.fromkeys(sorted(set_letters_both_str))}')
print(f'Those are lower letters {dict.fromkeys(sorted(set_letters_lower_str))}')
print(f'Those are upper letters {dict.fromkeys(sorted(set_letters_upper_str))}')




