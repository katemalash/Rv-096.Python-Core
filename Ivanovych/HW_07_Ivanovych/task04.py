sentence=input('Enter sentence:')
sentList=list(sentence)
word=''
sentLen=len(sentList)
keyList=[]
valueList=[]


for i in range(sentLen):

    if sentList[i]!=' ':
        word=word+sentList[i]
    else:
        keyList.append(word)
        word=''
keyList.append(word)

keyLen=len(keyList)

for i in range(keyLen):
    value=keyList.count(keyList[i])
    valueList.append(value)

sentDict={keyList[i]:valueList[i] for i in range(len(keyList))}

print('Dictionary from sentence:',sentDict)
