import sys
import matplotlib.pyplot as plt

###############################################
# Draw a scattered graph from two files
# where each file has one number per line
##############################################

#Use different colors for each category
colors = ['dummy', 'blue', 'orange']

#Maximum points to draw per category
numPoints = 10000

for i in [2, 1]:
	# Get file name from the command line
	fname = sys.argv[i]

	# Read numbers from each line and save to a list
	with open(fname) as f:
		content = f.readlines()
	# Strip \n
	content = [x.strip() for x in content] 

	# Generate sequantial numbers for x axis
	x = list(range(numPoints))

	# Plot
	plt.scatter(x, content[0:numPoints], marker='.', c=colors[i], s=1)

plt.show()
