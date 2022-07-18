number = float(input("Enter next number: "))
positive_share = 0
negative_share = 0
qty = 1
while number != 0:
    if number > 0:
        positive_share=(positive_share+1)/qty
        qty=qty+1
    else:
        negative_share =(negative_share+1)/qty
        qty=qty+1
    number = float(input("Enter next1 number: "))    

print(f"share of positive numbers is {positive_share},\nshare of negative share is {negative_share}")