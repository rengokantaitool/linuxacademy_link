# pip install --upgrade beautifulsoup4
# pip install html5lib
# Hernan Y.Ke 2/9/2018
from bs4 import BeautifulSoup
import requests,sys,re

def start(args):
    outer = requests.get(args)
    pagesoup = BeautifulSoup(outer.content, "html5lib")
    file = open("result.txt","w")
    for videopage in pagesoup.findAll('a',href=re.compile("lesson")):
        inner = requests.get("https://linuxacademy.com/"+videopage['href'])
        innersoup = BeautifulSoup(inner.content, "html5lib")
        video = innersoup.findAll('a',href=re.compile("lesson"))[0]['href']
        video = video[23:] if "redirect" in video else video
        print("Writing https://linuxacademy.com"+video)
        file.write("https://linuxacademy.com"+video+"\n")
    file.close()
    print("Done")
    
if __name__=='__main__':
    arg=sys.argv[1]
    start(arg)
