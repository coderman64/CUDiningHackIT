from bs4 import BeautifulSoup # to make the syntax pretty
import urllib.request # to get html document
import datetime #imports time and day
# user input for diningHall

def getFood(diningHall,mealTime):

    #where user is eating and key to add to url
    diningHallMap = {
        "schiletter":'1891',
        "core":'9713'
    }
    # what sort of meal user is searching to add key to html url
    mealMap = {
        "allday":"3000",
        "breakfast":"891",
        "litelunch":"972",
        "lunch":"892",
        "dinner":"893"
    }
    # sets date to variables to be used in URL
    date = datetime.datetime.now()
    y = date.year
    m = date.month
    day = date.day
    fulldate = str(m) + "%2F" + str(day) + "%2F" + str(y)
    #if shchiletter is closed return string
    if datetime.datetime.today().weekday() == 5 && diningHall == "schiletter":
        return "schiletter is closed on saturdays"
    #returns url of menu with hall, meal, and date the user is looking for
    menu = "https://" + "clemson.campusdish.com/api/menus/GetMenu?locationId=%s" % diningHallMap[diningHall] + "&mode=Daily&periodId=%s" % mealMap[mealTime] + "&date=%s" %  fulldate
    doc = urllib.request.urlopen(menu) # identifying url
    rawdoc = doc.read() # reads html code
    opendoc = rawdoc.decode("utf8") #converts to terminal textformat
    print(menu)

    soup = BeautifulSoup(opendoc,"html.parser") # to beautify the document we imported
    out1 = soup.find_all("a",class_="viewItem") # findf all of the food items in the document

    # makes list for food
    foodList = []
    for i in out1:
        #gets the name of the food, by searching for the first > symbol and last < symbol
        foodList.append(str(i)[str(i).find(">")+1:str(i).rfind("<")])
    print(foodList)
    return foodList
def main():
    getFood("", "")

if __name__ == "__main__":
    main()
