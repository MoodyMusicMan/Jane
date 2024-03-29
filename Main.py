
'''

# 05.21.19


# 1 access a seed site, store seed site in "Visited" text file

# 2. Collect all the links on that seed site

# 3. Write those links to a "Master" text file in the form
#   Origin : Link

4. Access the first site listed in the links and store in "Visited" text file

5. Collect all the links on that site

6. Write those links to a text file in the form
    Origin : Link

7. Check next site for previously visited site

8. Access next site not in "Visited" text file

9. repeat steps 5 - 9

'''


# 0 Imports ---------------------------------

import urllib3
from bs4 import BeautifulSoup, SoupStrainer
import urllib.request
import time
import re

# 1------------------------------------

def getPage(address):
    data = urllib.request.urlopen(address)
    soup = BeautifulSoup(data, from_encoding=data.info().get_param('charset'))
    print("Visiting Page " + str(address) + "\n")
    return soup

seedSite = "https://wikipedia.org"
#seedSite = "play.google.com/store/apps/details?id=org.wikipedia&referrer=campaign_id%3Dportal"
#seedSite = "www.wikisource.org/"
seedSite = "https://www.creativecommons.org/licenses/by-sa/3.0/"
seedSite = "https://stackoverflow.com/questions/1080411/retrieve-links-from-web-page-using-python-and-beautifulsoup"


timez = time.localtime()
timeMarker = ''
for item in timez[0:5]:
    timeMarker += "_" + str(item)



newStack = []
visitedStack = [seedSite]
masterListName = "MasterListFile" + timeMarker +".txt"
visitedListName = "VisitedListFile" + timeMarker +".txt"
errorsListName = "ErrorsListFile" + timeMarker +".txt"

pageData = getPage(seedSite)
print("Site visited...Checking Links...")
for link in pageData.find_all('a', href=True):
    print("Found Link " )
    print(link)
    thisLink = link['href']
    print("extracted link" + str(thisLink))

    #print(thisLink)
    if thisLink not in visitedStack:
        print("Adding it to Master List")
        wFile = open(masterListName, 'a')
        wFile.write(seedSite + " : " + thisLink + "\n")
        wFile.close()
        newStack.append(thisLink)
    else :
        print("Lionk is duplicate, not added to Master List")

print("Visiting Next Site if there is one...")

while len(newStack) > 0 :
    nextSite = newStack.pop()
    print("Going to :" + str(nextSite))
    print(nextSite)
    if nextSite not in visitedStack:
        try:
            visitedStack.append(nextSite)
            wFile = open(visitedListName, 'a')
            wFile.write(nextSite + "\n")
            wFile.close()
            pageData = getPage(nextSite)
            for link in pageData.find_all('a', href=True):

                thisLink = link['href']
                #print(thisLink)
                if thisLink not in visitedStack:
                    wFile = open(masterListName, 'a')
                    wFile.write(nextSite + " : " + thisLink + "\n")
                    wFile.close()
                    newStack.append(thisLink)

        except:
            wFile = open(errorsListName, "a")
            wFile.write(nextSite + "\n")
            wFile.close()
            #print to errors page

    else :
        print ("Oh, it was in the list already, nvm...")

