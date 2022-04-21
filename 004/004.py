"""
I KNOW THIS IS A NOT SO OPTIMAL SOLUTION, BUT I JUST WANT TO RUSH TO 100TH. PLEASE EXCUSE ME.
"""
digits = 3

def is_palindrome(input_number):
	string_number = str(input_number)
	iterator = reversed(string_number)
	reversed_number = ""
	for each_char in iterator:
		reversed_number += each_char
	# print("original string : ", string_number)
	# print("reversed string : ", reversed_number)
	if string_number == reversed_number:
		return True
	else:
		return False

candidates = set()

item2 = item1 = pow(10,digits)

for item1_counter in range(1,item1):
	for item2_counter in range(1, item2):
		candidates.add(item1_counter*item2_counter) 

palindromic_candidates = set()

for each_candidate in candidates:
	if(is_palindrome(each_candidate)):
		palindromic_candidates.add(each_candidate)

highest_palindrome = 0

for each_palindromic_candidate in palindromic_candidates:
	if highest_palindrome < each_palindromic_candidate:
		highest_palindrome = each_palindromic_candidate

print(highest_palindrome)