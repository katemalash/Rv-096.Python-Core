# There are two character strings of lowercase and uppercase 
# Latin letters and numbers. Develop a program that builds 
# and prints in alphabetical order the set of letters that are
#  in both arrays and the set of letters 
# of the first and second arrays separately


str1='Qwerrrte efewff efwefesccdvb vvz43t4t78vzvt,iiltllililtRTG1234t3'
str2='SscccIlm  Fm123 LLL cscacs sca'
com_elem = sorted(set(str2).intersection(str1))
elem_of_first = sorted([x for x in set(str1) if x.isalpha()])
elem_of_second = sorted([x for x in set(str2) if x.isalpha()])

print(f"the common elements are {com_elem}")
print(f"the elements of  first array are {elem_of_first}")
print(f"the elements of second array are {elem_of_second}")

# test

