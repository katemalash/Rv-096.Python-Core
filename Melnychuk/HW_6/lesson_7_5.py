all_elements = tuple((input('Enter the elements of the tuple: ')))
print(all_elements)
user_choice = input('Enter the symbol: ')
for i in all_elements:
    if user_choice == i:
        user_choice_index = all_elements.index(i)
if user_choice not in all_elements:
    print(f"There is no '{user_choice}' in the tuple.")
else:
    print(f"The index of user's input is {user_choice_index}" )
   