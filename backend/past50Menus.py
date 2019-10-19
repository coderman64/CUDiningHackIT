# import webScraper and json formatter
from WebScraper import getFood
import datetime
import json
import pytz

#creates and formats a json file, and returns the string form. Does NOT save to file
def dumpJSON():
	#jStrings is first a dictionary representing the JSON structure.
	date = datetime.datetime.now(tz=pytz.timezone('America/New_York'))
	finalSet = set()
	for i in range(50):
		list1 = set(getFood("schiletter","allday",date))
		list2 = set(getFood("core","allday",date))
		finalSet = finalSet | list1 | list2
		date = date - datetime.timedelta(days=1)
	jString = json.dumps({"items":sorted(list(finalSet))})
	#jStrings = {
	#	"schiletter":getFood("schiletter","allday",date),
	#	"core":getFood("core","allday",date)
	#}
	##jStrings is now a string containing the JSON file
	#jStrings = json.dumps(jStrings)
	return jString

if __name__ == "__main__":
	# open the json file, and write our JSON code to it.
	file = open("/home/ubuntu/CUDiningHackIT/backend/fulllist.json","w")
	file.write(dumpJSON())
	file.close()
