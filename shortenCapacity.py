# command center
def main ():
	# ADJUST: remove id from paths before committing
	readFile = '/home/[user]/Documents/projects/BuiltByMeT/scraper/fit-factory-scraper/capacitylog.csv'
	writeFile = '/home/[user]/Documents/projects/BuiltByMeT/scraper/fit-factory-scraper/visualization/data/viscapacitylog.csv'

	with open (readFile, "r") as file:
		lines = file.readlines()

	newLines = removeExcessCapacityInfo(lines)

	with open (writeFile, "w") as file:
		for line in newLines:
			file.write(line)

# gather all the lines with shortened capacity data
def removeExcessCapacityInfo (lines):
	newLines = ""
	firstLine = True

	for line in lines:
		# first line in the file is the header keep that the same
		if (firstLine):
			newLine = line
			firstLine = False
		else:
			newLine = withoutMaxCapacity(line)
		
		newLines += newLine

	return newLines

# create the line without the " / 500" at the end
def withoutMaxCapacity (line):
	letterIteration = 0
	firstSpace = 0
	whichComma = 0
	secondComma = 0
	# want 1st char after 2nd comma to 1st space
	for letter in line:
		if (letter == ","):
			whichComma += 1
		# grab the index of where to start (1st after 2nd comma)
		if (whichComma == 2 and secondComma == 0):
			secondComma = letterIteration + 1
		# grab the index of where to end (1st space)
		elif (whichComma == 2 and letter == " "):
			firstSpace = letterIteration
			break
		letterIteration += 1

	shortCapacity = line[secondComma:firstSpace]		
	newLine = line[:secondComma] + shortCapacity + "\n"

	return newLine

main()