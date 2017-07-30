def main(pickle):

  if pickle>5:
    print " 13 is greater than 5"

  elif pickle == 5:
    print "happy happy joy joy"
  else:
    print "who are you"  


main(1)

# def main2():
#   user_input = int(raw_input('Pick a number: '))

#   if user_input > 5:
#     print '%s is greater than 5' % str(user_input)

#   else:
#     print '%s is less than 5' % str(user_input)

# main2()

for i in range(10):
  print i

words = ["pickle", 'bob', "greg"]

for w in words:
  print w  

while True:
  print 'in a while loop'
  break
print 'all loops printed'

c = 0
while c < 10:
  if c == 5:
    c+= 1
    continue
    
  print 'in a while loop with c = %d' % c

  c += 1









