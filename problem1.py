f = open("problem_1_input.txt", "r")
table = []

for x in f:
	table.append(x)

for x in table:
	x = x.replace('\\n', '')

table = [int(numeric_string) for numeric_string in table]

count = 0


#part 1
for y in range(1, len(table)):
	if (table[y] > table[y-1]):
		count += 1
print(count)


f = open('problem_1_input.txt')
count = 0
ints = []
i = 0

for line in f:
	inputInt = int(line)
	ints.append(inputInt)

	if (len(table) > 4):
		triplet1 = table[i] + table[i-1] + table[i-2]
		triplet2 = table[i-1] + table[i-2] + table[i-3]
		if triplet1 > triplet2:
			count += 1
	i = i+1
print(count)