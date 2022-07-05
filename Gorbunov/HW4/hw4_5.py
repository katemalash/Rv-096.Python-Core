# Money chenging count.

money= int(input("Enter money value: "))
a = money//200
b = (money-a*200)//10
c = (money-a*200-b*10)//1
print(f"For change we need:\n{a} of '200'\n{b} of '10'\n{c} of '1' UAH")
