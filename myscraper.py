# !!!!!!!!!!!!!!!!!!!!!!!!!!!
# adjust [user] in filename
# before/after committing
# because privacy
# !!!!!!!!!!!!!!!!!!!!!!!!!!!
from bs4 import BeautifulSoup
import datetime
import requests

# cleaner with a main() than all these at the bottom
def main():
	#capacity = '12'
	capacity = soupify()
	returned_time = findCurrentTime()
	new_data = combineData(capacity,returned_time)
	writeToFile(new_data)

# scrape to get the wanted data point w/ bs4 and requests
def soupify():
	url = "https://www.fitfactoryclubs.com/gyms/massachusetts/north-attleboro"
	req = requests.get(url)
	soup = BeautifulSoup(req.text,"lxml")

	id_to_find = 'p_lt_ctl03_pageplaceholder_p_lt_ctl03_FitFactory_ClubCapacity_capacityLabel'
	capacity_id = soup.find(id = id_to_find)
	current_capacity = capacity_id.p.span.get_text()

	print(current_capacity)
	return current_capacity

# grab the current time w/ datetime
def findCurrentTime():
	day = datetime.datetime.now().strftime('%a')
	hour = datetime.datetime.now().strftime('%I')
	minute = datetime.datetime.now().strftime('%M')
	ampm = datetime.datetime.now().strftime('%p')

	current_time = (hour + ':' +  minute + ' ' + ampm)
	return [day,current_time]

# combine new data points into what's being written to csv
def combineData(capacity,returned_time):
	day = returned_time[0]
	current_time = returned_time[1]
	new_data = day + ',' + current_time + ',' + capacity + '\n'
	return new_data

# write the scraped data to csv
def writeToFile(new_data):
	i = 0
	# filename if running individually
	#filename = 'capacitylog.csv'
	# filename for cronjob since it needs an absolute path
	filename = '/home/[user]/Documents/projects/BuiltByMeT/fit-factory-scraper-public/capacitylog.csv'

	# open and read the file into lines on its own
	with open(filename, 'r') as file:
		file_by_lines = file.readlines()

	# open the file a second time to write to the file
	# overwrites on open (same as w+ to truncate) but
	# lines already saved off from read only so it's ok
	with open(filename, 'w') as file:
		for line in file_by_lines:
			if i == 1:
				file.write(new_data)
			file.write(line)
			i += 1

		# catch if it's the first entry
		if i == 1:
			file.write(new_data)

main()