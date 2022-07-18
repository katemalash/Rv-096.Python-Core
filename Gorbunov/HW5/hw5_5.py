p,h=11,32
sum=0; multiply=1; count =0; digit=0
while digit!=p and digit!=h:
    digit= int(input("Enter digit: "))
    if digit>h:
        multiply*=digit  #наприклад 15 30 32. Мультіплай лишається 1
        sum+=digit
        count+=1
    elif digit>p:
        sum+=digit   
        count+=1
print(f"Sum of digits bigger then 'P' is:\t{sum}.\nMultiply of digits bigger then 'H' is:\t{multiply}.\
    \nCount of digits between 'P'and 'H' is:\t{count}.")


