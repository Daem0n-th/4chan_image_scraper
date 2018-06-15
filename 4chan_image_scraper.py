import sys
import argparse
from urllib.request import urlopen,Request,urlretrieve
from bs4 import BeautifulSoup as BS


base_url="https://boards.4chan.org/"
headers={"User-Agent": "Mozilla/5.0"}

parser = argparse.ArgumentParser(description="Scrape images of 4chan threads")
parser.add_argument('-b',"--board",help="Specify Board",required=True)
parser.add_argument('-t',"--thread",help="Thread Number",required=True)
args=parser.parse_args(sys.argv[1:])

url=base_url + args.board + "/thread/" + args.thread
print("Scraping {}".format(url))
req=Request(url,headers=headers)
try:
    html=urlopen(req).read()
except:
    print("There was an Error!")
    sys.exit(1)
soup=BS(html,"html.parser")
links=soup.find_all("div",{"class":"fileText"})
img_links=["https:" + i.a.get('href') for i in links]
n=len(img_links)
print("Found {} images".format(n))
count=1
for i in img_links:
    sys.stdout.write('\r')
    sys.stdout.write("Retrieving..." + str(count) + "/" + str(n) )
    sys.stdout.flush()
    urlretrieve(i,i[i.rfind('/')+1:])
    count+=1
print("\nDone!")
