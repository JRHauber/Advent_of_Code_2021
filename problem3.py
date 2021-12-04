f = open('problem_3_input.txt')
binary_input = []
gamma_rate = []
epsilon_rate = []

for line in f:
	binary_input.append(str(line))

for x in range(0, 12):

	total = 0

	for y in range(0, len(binary_input)):
		total += int(binary_input[y][x])

	if(total > (len(binary_input)/2)):
		gamma_rate.append(1)
		epsilon_rate.append(0)
	else:
		gamma_rate.append(0)
		epsilon_rate.append(1)



def binary_to_decimal(binary):
	decimal = 0
	for digit in binary:
		decimal = decimal*2 + int(digit)

	return decimal

print("Binary Gamma Rate: ", gamma_rate)
print("Binary Epsilon Rate: ", epsilon_rate)
print("Gamma Rate: ", binary_to_decimal(gamma_rate))
print("Epsilon Rate: ", binary_to_decimal(epsilon_rate))
print("Power Consumption: ", (binary_to_decimal(gamma_rate) * binary_to_decimal(epsilon_rate)))
##################
######PART 2######

def find_bit_rating(arr, high_or_low, bit, length):
	#most common: high_or_low = 1
	#least common: high_or_low = 0
	#bit = current bit
	#length = length of binary string

	deciding_bit = 1

	if((bit+1) > length):
		arr[0] = arr[0].replace('\n','')
		return arr
	else:
		total = 0
		next_arr = []
		for x in arr:
			total += int(x[bit])

		if(high_or_low == 1):
			if(total > (len(arr)/2)):
				deciding_bit = 1
			elif(total < (len(arr)/2)):
				deciding_bit = 0
			else:
				deciding_bit = 1
		elif(high_or_low == 0):
			if(total > (len(arr)/2)):
				deciding_bit = 0
			elif(total < (len(arr)/2)):
				deciding_bit = 1
			else:
				deciding_bit = 1
		else:
			deciding_bit = 1

		for y in arr:
			if(int(y[bit]) == deciding_bit):
				next_arr.append(y)

		return find_bit_rating(next_arr, high_or_low, bit+1, length)
	
print('Test: ', binary_to_decimal(find_bit_rating(binary_input, 1, 0, 12)))