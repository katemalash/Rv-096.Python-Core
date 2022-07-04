
from pickle import TRUE


cat_coll = dict()
auto_coll = dict()
elephant_coll = dict()
my_collections = [cat_coll, auto_coll, elephant_coll]

new_mark = input(f'Enter name of a new MARK: ')
if new_mark in cat_coll or new_mark in auto_coll or new_mark in elephant_coll:
   print("You have another one ", new_mark, "now its", new_mark+1)
   

cat_coll['MARK white cat'] = "the bigest cat"
cat_coll['MARK white cat']
cat_coll['MARK white cat']
cat_coll['MARK green cat'] = 'a very strange cat'
auto_coll['MARK ferrari'] = '1 million $ car'
print(my_collections)
