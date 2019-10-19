# import webScraper and json formatter
from WebScraper import getFood
import datetime
import json

#creates and formats a json file, and returns the string form. Does NOT save to file
def dumpJSON():
	#jStrings is first a dictionary representing the JSON structure.
	date = datetime.datetime.now(tz=pytz.timezone('America/New_York'))
	jStrings = {
		"schiletter":getFood("schiletter","allday",date),
		"core":getFood("core","allday",date)
	}
	#jStrings is now a string containing the JSON file
	jStrings = json.dumps(jStrings)
	return jStrings

if __name__ == "__main__":
	# open the json file, and write our JSON code to it.
	file = open("/home/ubuntu/CUDiningHackIT/backend/menus.json","w")
	file.write(dumpJSON())
	file.close()
