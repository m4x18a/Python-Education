s = 'orange strawberry barley gooseberry apple apricot barley currant orange melon pomegranate banana banana orange barley apricot plum grapefruit banana quince strawberry barley grapefruit banana grapes melon strawberry apricot currant currant gooseberry raspberry apricot currant orange lime quince grapefruit barley banana melon pomegranate barley banana orange barley apricot plum banana quince lime grapefruit strawberry gooseberry apple barley apricot currant orange melon pomegranate banana banana orange apricot barley plum banana grapefruit banana quince currant orange melon pomegranate barley plum banana quince barley lime grapefruit pomegranate barley'
mylist = s.split()
mylist1 = []
mydict = {}
for word in mylist:
    mydict[word] = mydict.get(word, 0) + 1
maxx = max(mydict.values())
for key, value in mydict.items():
    if value == maxx:
        mylist1.append(key)
mylist1.sort()
print(mylist1[0])

