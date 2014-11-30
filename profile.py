def readFamily(family_file):
	f = open(file, 'r')
	family = []
	tmp = f.readline()
	while tmp:
		family.append(tmp[0:-1])
		tmp = f.readline()
	f.close()
	print family