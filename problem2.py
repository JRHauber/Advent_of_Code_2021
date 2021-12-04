f = open("problem_2_input.txt")
commands = []
values = []
h_pos = 0
depth = 0

for line in f:
	temp = line.split(' ')
	commands.append(temp[0])
	values.append(int(temp[1]))

print('\nPart 1\n')
#part 1
i = 0

while(i < len(commands)):
	if(commands[i] == 'forward'):
		h_pos += values[i]
	elif(commands[i] == 'down'):
		depth += values[i]
	else:
		depth -= values[i]
	i += 1

print("Horizontal Position: ", str(h_pos))
print("Depth: ", str(depth))
print("Problem Solution: ", str(h_pos * depth))
#
print('\nPart 2\n')
#part 2
aim = 0
h_pos = 0
depth = 0
i = 0
while(i < len(commands)):
	if(commands[i] == 'forward'):
		h_pos += values[i]
		depth += (values[i] * aim)
	elif(commands[i] == 'up'):
		aim -= values[i]
	else:
		aim += values[i]
	i += 1
print("Aim: ", str(aim))
print("Horizontal Position: ", str(h_pos))
print("Depth: ", str(depth))
print("Problem Solution: ", str(h_pos * depth))