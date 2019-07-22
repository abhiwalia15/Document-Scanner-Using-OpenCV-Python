import json

str = ' he is my naukar'

f = open('email.txt','w')

json.dump(str, f)