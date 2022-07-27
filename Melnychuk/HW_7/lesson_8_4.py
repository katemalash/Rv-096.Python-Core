#'Mort'
# But not any Death. This is the Death whose particular sphere of operations is, well, not a sphere at all, but the Discworld, which is flat and rides on the back of four giant elephants who stand on the shell of the enormous star turtle Great A'Tuin, and which is bounded by a waterfall that cascades endlessly into space.

text = input('Enter the text: ')

list_text = text.split()
set_text = set(list_text)

dict_text = dict.fromkeys(sorted(set_text), 0)

for word in list_text:
    if word in set_text:
        dict_text[word] += 1

print(dict_text)