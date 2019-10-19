from WebScraper import getFood
import json

def dumpJSON():
	#file = open(filename,"w")
	jStrings = {
		"schiletter":getFood("schiletter","allday"),
		"core":getFood("core","allday")
	}
	jStrings = json.dumps(jStrings)
	return jStrings

if __name__ == "__main__":
	file = open("menus.json")
	file.write(dumpJSON())
	file.close()
