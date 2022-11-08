s = input("Enter the string: ")
f=(s.split())
mnr = 0
max = len(f[mnr])
for i in range(len(f)):
    if len(f[i]) > max:
	    max = len(f[i])
	    mnr = i
print(f[mnr])
