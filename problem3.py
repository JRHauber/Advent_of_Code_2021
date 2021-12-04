f = open('problem_3_input.txt')
binary_input = []
gamma_rate = []
epsilon_rate = []

for line in f:
	binary_input.append(str(line))

for x in range(0, 11):

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

print("Gamma Rate: ", binary_to_decimal(gamma_rate))
print("Epsilon Rate: ", binary_to_decimal(epsilon_rate))
print("Power Consumption: ", (binary_to_decimal(gamma_rate) * binary_to_decimal(epsilon_rate)))