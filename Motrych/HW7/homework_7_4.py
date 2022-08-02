#  User enters the text. A word is a sequence of non-empty characters
# that follow in a row, words are separated by one or more spaces.
#  Create a dictionary in which the keys are the words from the sentence,
# and the values ​​- the number of it's occurrences in the sentence.

text= (input("Enter words split by spaces ").split())

dic={}

for i in text:
    dic[i]=text.count(i)

print(dic)
