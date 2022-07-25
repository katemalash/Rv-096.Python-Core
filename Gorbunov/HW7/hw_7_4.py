text = (input('Enter chars or words by space: ').split())
dict = {}
for i in text:
    dict[f'{i}'] = text.count(f'{i}')
print (dict)