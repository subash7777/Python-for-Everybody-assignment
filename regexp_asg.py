#In this assignment you will read through and parse a file with text and numbers. You will extract all the numbers in the file and compute the sum of the numbers.

import re
hand = open('regex_sum_926182.txt')
addsum=0
for line in hand:
    line = line.rstrip()
    x = re.findall('([0-9]+)', line)
    if len(x) > 0:
    	print(x)
    	for num in x:
    		num=num.rstrip()
    		sum = int(num)
    		addsum+=sum
print (addsum)


       