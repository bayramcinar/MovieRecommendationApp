from os import times_result
from platform import release
from re import X
import requests
from bs4 import BeautifulSoup
import pandas as pd
import random
from IPython.display import clear_output
import time
a = 0
liste = []


r = requests.get("https://www.imdb.com/chart/moviemeter/?sort=rk,asc&mode=simple&page=1").content
soup1 = BeautifulSoup(r,"html.parser")
full_list = soup1.find_all("td",{"class":"titleColumn"}) # YOU CAN CHANGE THE NUMBER OF MOVIES IN THE MEMORY (limit=)

for movie in full_list:
        link_bası = "https://www.imdb.com"
        linksonu = movie.find("a").get("href")
        link = link_bası+ linksonu
        r1 = requests.get(link).content
        soup = BeautifulSoup(r1,"html.parser")
        try:
                title = soup.find("h1",{"data-testid":"hero-title-block__title"}).text.strip()
        except:
                title = "isim bilgisi bulunamadı"        
        #print(title)

        explanation = soup.find("span",{"class":"sc-16ede01-2 gXUyNh"}).text.strip()
        #print(explanation)

        releaseTime = soup.find("span",{"class":"sc-8c396aa2-2 itZqyK"}).text.strip()
        #print(releaseTime)
        try:
                imdb = soup.find("span",{"class":"sc-7ab21ed2-1 jGRxWM"}).text.strip()
        except:
                imdb = "imdb yok"    
        #print(imdb)  
        try:      
                times = soup.find("ul",{"class":"ipc-inline-list ipc-inline-list--show-dividers sc-8c396aa2-0 kqWovI baseAlt"}).find_all("li",{"class":"ipc-inline-list__item"})
        
                time1 = times[2].text
        except:
                time1 = "süre bilgisi yok"                        
        #print(time1)
        trailer = soup.find("a",{"class":"ipc-lockup-overlay sc-f0d4a9ac-2 gkiDbj hero-media__slate-overlay ipc-focusable"}).get("href")        
        trailerLink = link_bası+trailer
        #print(trailerLink)
        liste.append([title,time1,releaseTime,explanation,imdb,trailerLink])
        a = a+1
print(f"the number of movie : {len(full_list)}")

        
print("-----YOUR MOVIE RECOMMENDATION-----")        
mv = random.choice(liste)
print(f"name : {mv[0]}\nexplanation : {mv[3]}\nrelease time : {mv[2]}\nimdb point : {mv[4]}\ntime : {mv[1]}\ntrailer link : {mv[5]}")
