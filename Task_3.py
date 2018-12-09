'''
TASK 3 UPDATE
attribute list: [{‘CLR’: [‘RED’, ‘BLUE’, ‘GREEN’]}, {‘MEM’: [‘16GB’, ‘64GB’, ‘128GB’]}]
Pattern: ‘IPHONE [CLR]-[MEM]’
You guys need to create the one function and pass above two parameters then output like below. Order of list can be any.
IPHONE RED-16GB
IPHONE BLUE-16GB
IPHONE GREN-16GB
IPHONE RED-64GB
IPHONE BLUE-64GB
IPHONE GREN-64GB
IPHONE RED-128GB
IPHONE BLUE-128GB
IPHONE GREN-128GB
'''
import re

def fun (att , patt):
    c = [[x,y] for x in att[0] for y in att[1]]
    for i in range(0,9):
        subs = {'[CLR]' : c[i][0] , '[MEM]' : c[i][1]}
        print(re.sub('|'.join(re.escape(key) for key in subs.keys()),
                  lambda k: subs[k.group(0)], patt))
    return

A = [['RED' , 'BLUE' , 'GREEN'] , ['16 GB' , '64 GB' , '128 GB']]
P = "IPHONE [CLR]-[MEM]"
fun(A , P)
