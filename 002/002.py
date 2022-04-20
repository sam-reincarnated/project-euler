MAX = 4000000
SUM = 0
fibbonacci_series = [1,2]

while fibbonacci_series[-1] < MAX:
	fibbonacci_series.append(fibbonacci_series[-1]+fibbonacci_series[-2])
# print(fibbonacci_series)

for each_element in fibbonacci_series:
	if(not(each_element%2)):
		# print(each_element)
		SUM += each_element

print(SUM)