user_choice = None
user_numbers = []
positive_numbers = []
negative_numbers = []

while user_choice != "0":
    user_choice = input("Enter the number: ")
    if float(user_choice) > 0:
        positive_numbers.append(float(user_choice))
    elif float(user_choice) < 0:
        negative_numbers.append(float(user_choice))
    user_numbers.append(float(user_choice))
    
percentage_positive = round((len(positive_numbers)/len(user_numbers) * 100), 2)
percentage_negative = round((len(negative_numbers)/len(user_numbers) * 100), 2)
    
print(f'The percentage of positive numbers is {percentage_positive} %.\nThe percentage of negative numbers is {percentage_negative} %.')
    

 
 
 