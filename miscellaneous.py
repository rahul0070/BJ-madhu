def compare(a, b):
	if a == b:
		result = 0
	elif a>b:
		result = 1
	else:
		result = 2
	return result


def isInList(Input):
	li = ['J', 'K', 'Q']
	if Input == 'J' or Input == 'K' or Input == 'Q':
		return True

def sumWithAce(list, aceValue):
	result = 0
	for i in list:
		if i == 'A':
			i = int(aceValue)
		if isInList(i) == True:
			i = 10
		result = result + int(i)
	return result


def sumOfList(listInput):
	sum1 = sumWithAce(listInput, 1)
	sum2 = sumWithAce(listInput, 11)
	return sum1
