prime_factor = 600851475143
# let us assume this is the prime_factor and lets keep dividing prime numbers from this
prime_list = [2]
# print(prime_list)

def divisibility_test(input_prime, input_test_number):
	if(not(input_test_number%input_prime)) and input_test_number != input_prime:
		# print(input_test_number, "is input number and ", input_prime, "is the prime number dividing")
		return True
	else:
		return False

def prime_test(prime_list, input_number):
	for prime_number in prime_list:
		if(divisibility_test(prime_number, input_number)):
			return False
	# print(input_number, "is a prime")
	return True

def get_next_prime(prime_list):
	largest_prime_number = prime_list[-1]
	# print(largest_prime_number)
	while(largest_prime_number < prime_factor):
		largest_prime_number+= 1
		if(prime_test(prime_list,largest_prime_number)):
			# print("FFF")
			prime_list.append(largest_prime_number)
			break

test_val = divisibility_test(2, 9);
print(test_val)

get_next_prime(prime_list)

# while max_prime is smaller than prime_factor, keep searching.
while(prime_list[-1] < prime_factor):
	# no need to test if current current primes are dividing
	# get the next prime
	get_next_prime(prime_list)
	# try to divide the prime factor with this
	if divisibility_test(prime_list[-1], prime_factor):
		# print("Prime factor", prime_factor, " is divisible by", prime_list[-1], "\n current prime factor is", prime_factor/prime_list[-1])
		prime_factor = prime_factor/prime_list[-1]
print(prime_factor)