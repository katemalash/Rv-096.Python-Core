num_to_words = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', \
             6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten', \
            11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', \
            15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', \
            19: 'nineteen', 20: 'twenty'}    
    
number = input('Enter the number please: ')
try:
    if float(number) > 0:
       print('positive')
    elif float(number) < 0:
        print('negative')
    else:
        print('the number is 0')
except: 
    print('You entered not a number!')
    exit()

lenth_number = len(number)
if not number.isdigit():        
    if '.' in number and '-' in number:
       lenth_number = lenth_number - 2
    elif '.' in number or '-' in number:
       lenth_number = lenth_number - 1
    print(f'{num_to_words[lenth_number]}-digit')
else:
    print(f'{num_to_words[lenth_number]}-digit')         