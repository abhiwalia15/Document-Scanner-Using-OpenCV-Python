import re

f = open('email.txt', 'r+')
#contents =f.read()
contents = ' hello my nam eis aniruch@getmorph.com'
for email in contents.split(' '):
    print(email)
    match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', email)
    if match != None:
	    print('EMAIL:' + email)