import re

match = re.search('a', 'bat')
print match.group()

match = re.search(r'\w+.\w+@\w+', r'saric.tony@gmail.com')
print match.group()

match = re.search(r'\w+.\w+@\w+', r'tony@gmail.com')
print match.group()

match = re.findall(r'([\w.-]+)@([\w.-]+)', r'tony@gmail.com saric.tony@gmail.com asdfdfa@gmail.com adsfasd')
print match

for m in match:
  print m
  print m[0]
  print m[1]