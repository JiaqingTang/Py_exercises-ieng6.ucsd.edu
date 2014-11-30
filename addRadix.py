'''The input should be two string represent two numbers in the specific base '''
def add(a, b, base):
	numa = [int(i) for i in a[::-1]]
	numb = [int(i) for i in b[::-1]]
	result = []
	i, j, carry = 0, 0, 0
	while i < len(numa) or j < len(numb) or carry > 0:
		a, b = 0, 0
		if i < len(numa):
			a = numa[i]
			i += 1
		if j < len(numb):
			b = numb[j]
			j += 1
		cur_sum = a + b + carry
		result.append(cur_sum % base)
		carry = cur_sum / base

	return ''.join([str(i) for i in result[::-1]])

def addList(data, base):
	while len(data) >= 2:
		a = data.pop()
		b = data.pop()
		tmp_sum = add(a, b, base)
		data.append(tmp_sum)
	return data[0]
