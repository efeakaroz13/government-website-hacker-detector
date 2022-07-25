import requests
from bs4 import BeautifulSoup
from colorama import Fore, Back, Style

keywords = ["hacklenmiştir","kırılmıştır","kill-9","anonymous","hackers","hacker group",".onion","blackhat","black-hat","for money","hackerzz","localhost","kill","usa","russia","soviet"]
loclist = []
listopen = open("list.txt","r")
readlinesall = listopen.readlines()
riskypages=[]
riskwriter = open("risk.txt","a")
for r in readlinesall:
    print(Fore.CYAN+"INFO "+Fore.RESET+"|"+ Fore.GREEN+" SCANNING {}".format(r.replace("https://","").split("/")[0]))
    print(Fore.RESET)
    sitemap = requests.get(r.replace("%0a","").strip()+"/sitemap.xml").content
    soup = BeautifulSoup(sitemap, 'xml')
    allloc = soup.find_all("loc")
    for l in allloc:
        if l.get_text(strip=True) == "":
            pass
        else:
            loclist.append(l.get_text(strip=True))

    print(Fore.BLUE+"INFO"+Fore.RESET+" | {} PAGES FOUND AT SITEMAP, LOOKING FOR HACKERS!".format(len(loclist)))
    for pagename in loclist:
        page = requests.get(pagename,headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'})
        pagecontent = str(page.content).lower().replace("\n","")
       
        for w in keywords:
            try:
                pagecontent.split(keywords)[1]
                riskypages.append(page)
                print(Fore.RED+"KEYWORD FOUND AT => "+Fore.WHITE+str(pagename))
                print(Fore.RESET)
                riskwriter.write(pagename+"\n")
            except:
                pass
        indexer = loclist.index(pagename)
        if indexer == 1000 and len(riskypages) == 0:
            print(Fore.GREEN+"INFO | CLEAN |SCANNED 1000 PAGES ")
            print(Fore.RESET)
        if indexer == 1000 and len(riskypages) > 0:
            print(Fore.RED+f"INFO | {len(riskypages)} Word Detected SCANS | SCANNED 1000 PAGES ")
            print(Fore.RESET)
        if indexer == 2000 and len(riskypages) == 0:
            print(Fore.GREEN+"INFO | CLEAN |SCANNED 2000 PAGES ")
            print(Fore.RESET)



        
