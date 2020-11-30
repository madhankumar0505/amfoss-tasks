RUST SCRAP :

My efforts to learn Rust didnt help me complete the task. But I still wished to complete the task with other prog languages. So I thought of programming in Python. I knew that we have to do web scrapping only in rust, but still I wanted to give a try and wish to share the code with u :)

PYTHON CODE FOR WEB SCRAPPING:

import requests
import bs4
import lxml
res=requests.get('https://www.worldometers.info/coronavirus/#countries')
type(res)
res.text 
print(res.text)
soup=bs4.BeautifulSoup(res.text,'lxml')
hi=soup.select('title')
print(hi)
soup.title.text
print(soup.title.text)

for link in soup.find_all("countries"):
    print("Inner Text: {}".format(link.text))
    print("Title: {}".format(link.get("title")))
    print("href: {}".format(link.get("href")))  #Code yet to be completed.
