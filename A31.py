import random
from sets import Set
def dna_gen(length, pa, pt, pg, pc):
	pa = int(length * pa)
	pt = int(length * pt)
	pg = int(length * pg)
	pc = int(length * pc)
	remainder = length - pa - pt - pg - pc
	s = ''.join('A' * pa + 'T' * pt + 'G' * pg + 'C' * pc + random.choice('ATGC') * remainder)
	return ''.join(random.sample(s, len(s)))
	# print ''.join(random.choice('ATGC') for _ in xrange(length))

def dna_set_gen(num, size):
	result = []
	for i in xrange(num):
		result.append(dna_gen(size, 0.25, 0.25, 0.25, 0.25))
	return result

def get_frequency(dna_set):
	result = {}
	dict = {'A' : 0, 'T': 0, 'G' : 0, 'C' : 0}
	total = 0.00
	for dna in dna_set:
		total += len(dna)
		for base in 'ATCG':
			dict[base] = dict[base] + dna.count(base)
	for base in 'ATGC':
		result[base] = dict[base] / total

	return result

def get_score(s1, s2, match, mismatch, indel):
	result = 0
	start = 0, 0
	end = 0, 0
	S = (len(s2)+1) * [(0,(0,0))]
	for i in xrange(1, len(s1)+1):
		pre = S[0]
		for j in xrange(1, len(s2)+1):
			diff = 0
			if s1[i-1] == s2[j-1]:
				diff = match
			else:
				diff = mismatch
			cur = max(0, pre[0] + diff, S[j][0] + indel, S[j-1][0] + indel)
			cur_start = pre[1]
			if pre[0] == 0:
				cur_start = i, j
			pre = S[j]
			S[j] = cur, cur_start
			if S[j][0] > result:
				result = S[j][0]
				start = S[j][1]
				end = i,j
	return end[0] - start[0] + 1 

def p1c():
	f = open('record.txt','a+b')

	# print ''.join(random.sample(s, len(s)))
	# dna = dna_gen(100, 0.25, 0.25, 0.25, 0.25)
	seq_len_set = [100, 200, 500, 1000, 1500, 2000]
	ITERATION = 10
	SEQLEN = 1000
	for SEQLEN in seq_len_set:
		dna_set1 = dna_set_gen(ITERATION, SEQLEN)
		dna_set2 = dna_set_gen(ITERATION, SEQLEN)
		total = 0
		for i in xrange(ITERATION):
			total += get_score(dna_set1[i], dna_set2[i], 1, 0, 0)
		f.write( str(total/ITERATION)+' '+ str(SEQLEN)+'\n')
		total = 0
		for i in xrange(ITERATION):
			total += get_score(dna_set1[i], dna_set2[i], 1, -30, -20)
		f.write( str(total/ITERATION)+' '+ str(SEQLEN)+'\n')
	f.close()

def p2():
	ITERATION = 10
	SEQLEN = 1000
	dna_set1 = dna_set_gen(ITERATION, SEQLEN)
	dna_set2 = dna_set_gen(ITERATION, SEQLEN)
	mismatch = [-30, -20, -10, -1, -0.5, -0.33, -0.25, 0]
	for mis in mismatch:
		total = 0
		for i in xrange(ITERATION):
			total += get_score(dna_set1[i], dna_set2[i], 1, 0, 0)
		f.write( str(total/ITERATION)+' '+ str(SEQLEN)+'\n')
		total = 0
		for i in xrange(ITERATION):
			total += get_score(dna_set1[i], dna_set2[i], 1, -30, -20)
		f.write( str(total/ITERATION)+' '+ str(SEQLEN)+'\n')
	f.close()

# print get_score("tgcaa", "tcat", 1, -1, -1)
p1c()