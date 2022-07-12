'''Aleksieiev Valentyn
12/07/2022 HomeWork#5, Task#6
For user-entered numbers, determine the percentage of positive and negative numbers.
When entering the number 0, finish the job.
'''
from cheker import variable_check


num_lst = []
while True:
    try:
        num_lst.append(int(input(f'Input your int number to calc % positive and negative or 0 to finish: ')))
    except Exception:
        print('You input not integer number')
        continue
    
    if num_lst[-1] != 0:
        print('Your numbres:', *sorted(num_lst))
        pos_lst = list(filter(lambda x: x>0, num_lst))
        neg_lst = list(filter(lambda x: x<0, num_lst))
        print(f'The positiv numbers are: {len(pos_lst)/len(num_lst)*100:.2f} percentage')
        print(f'The negative numbers are: {len(neg_lst)/len(num_lst)*100:.2f} percentage')
        print('===============================================================\n')
    else:
        break

print('I hope you liked it :)')


    