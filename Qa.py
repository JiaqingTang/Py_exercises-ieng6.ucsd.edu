def linear_gap_pen(s1, s2):
	table = []
	#initialize row
	for i in xrange(len(s1)+1):
		row = []
		row.append(0)
		table.append(row)
	#initialize col
	for i in xrange(1, len(s2)+1):
		table[0].append(0)
	print table
	#DP
	for i in xrange(1, len(s1)+1):
		for j in xrange(1, len(s2)+1):
			diff = 0
			if s1[i-1] == s2[j-1]:
				diff = 1
			else:
				diff = -1
			table[i].append(max(0, table[i-1][j-1] + diff, table[i][j-1] - 1, table[i-1][j] - 1))
	print table

if __name__ == '__main__':
	linear_gap_pen("tcat", "tgcaa")