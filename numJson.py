import re

f = open('email.json', 'r')
contents =f.read()
#contents = ' hello my nam eis aniruch@getmorph.com'

for email in contents.split(' '):
    #print(email)
    match = re.findall(r"^[0-9]*", email)
    if match != None:
	    print('NUM:' + email)
        

