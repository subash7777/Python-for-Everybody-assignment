name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

di = dict()
for line in handle:
    if not line.startswith("From "): continue
    wds=line.rstrip()
    for w in wds[1]:
    	if w in di:
    		di[w] =di[w] +1
    	else:
    		di[w] =1
    	print(w,di[w])
