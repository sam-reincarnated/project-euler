numbers_list = [3,5]
MAX = 1000
SUM = 0

def test_if_multiple(numbers_list, input_number):
	for numbers_list_item in numbers_list:
		if(not(input_number%numbers_list_item)):
			return True
	return False

iterator = range(1,MAX)
for i in iterator:
	# print(i)
	if(test_if_multiple(numbers_list,i)):
		SUM += i

print(SUM)