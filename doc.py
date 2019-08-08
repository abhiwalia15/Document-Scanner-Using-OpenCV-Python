import re

f = open('email.json','r')
contents =f.read()

for o in contents.split(' '):
    # print(o)
    match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', o)
    if match != None:
	    print('EMAIL:' + o)
