
#########################################
#										#
# Jaime Manuel Trillos Ujueta			#
# Luis Daniel Fernandes Rotger			#
#										#
# Programming Assignment A 				#
# Celular Automata						#
#										#
#########################################

from random import randint
import sys


print 'CELULAR AUTOMATA'
print '======= ========'
print ''
print ''
print ''


# Parameters insertion
radius = raw_input('Enter the neighbourhood radius: ')

while(radius != '1'  and radius != '2'):
	radius = raw_input('Please enter a valid radius (1 or 2): ')

rule = raw_input('Enter the rule for the CA (in Wolfram Notation): ')

while(int(rule) < 0):
	rule = raw_input('Please enter a valid rule (>= 0): ')

mode = raw_input('Select the starting condition ((1) a seed, (2) random): ')

while(mode != '1'  and mode != '2'):
	mode = raw_input('Select a valid starting condition ((1) a seed, (2) random): ')


# Parsing radius
radius = int(radius)

# Rule generation
b_rule = []
quotient = int(rule)

# Transforming the rule into binary
while quotient > 0:
	b_rule.insert(0, quotient % 2)
	quotient = quotient / 2


# Insertion of the rest of necessary zeros.
while (len(b_rule) < pow(2,2*int(radius) + 1)):
	b_rule.insert(0, 0)


# Cells initialization
cells = [0] * 84

# Case 1, with the seed
if (mode == '1'):
	cells[41] = 1
# Case 2, random
elif (mode == '2'):
	for i in range(84):
		cells[i] = randint(0,1);

# Fix the boundary cells
cells[0] = 0
cells[1] = 0
cells[82] = 0
cells[83] = 0


raw_input('Press enter everytime you want to see the new state of the automata. Ctrl + C to Exit.')

# Printing the first line
for k in range(84):
	sys.stdout.write(' ' + str(cells[k]))

raw_input()	


while True:
	# Creating the new line all zeros
	new_cells = [0] * 84
	# Extract the neighbourhood
	for i in range(2, 81):
		neighbourhood = []
		j = i - radius
		# Go through the neighbourhood
		while(j <= i + radius):
			# Extract the element
			neighbourhood.append(str(cells[j]))
			j += 1
		
		# Parse the neighbourhood, to integer
		which_rule = int(''.join(neighbourhood), 2)
		# Change the cell into its new state
		new_cells[i] = b_rule[len(b_rule) - which_rule - 1] 
	
	#Copy the new list into the cells list
	cells = new_cells[:]

	#Print line
	for k in range(84):
		sys.stdout.write(' ' + str(cells[k]))

	# Wait for input
	raw_input()	

