import sys
import random
import requests
from bs4 import BeautifulSoup
baseurl="https://www.flipkart.com"
input="dslr camera"
i=1

url="https://www.flipkart.com/search?q="
    
array=input.split()
for i in array:
    url+=i
    url+='+'


headers={
    "user_Agent":"https://developers.whatismybrowser.com/useragents/parse/2899915-chrome-windows-blink"
}

res=requests.get(url)
if res.status_code!=200:
     print("No connection")
     exit()


soup=BeautifulSoup(res.content, 'html.parser')
productlist=soup.find_all('div',class_="_1AtVbE col-12-12")
productlinks=[]
i=0
for item in productlist:
    for link in item.find_all('a',href=True):
        productlinks.append(baseurl+link['href'])
    i+=1
    if i==10:
        break
print(productlinks)
for link in productlinks:

    r=requests.get(link,headers=headers)
    soup=BeautifulSoup(r.content,'html.parser')
    imgsrc=soup.find('img')
    image=imgsrc['src']
    name=""
    price=""
    image=""
    rating=""
    try:
      price=soup.find('div',class_='_30jeq3 _16Jk6d').text
      rating=soup.find('div',class_='_3_L3jD').text
      name=soup.find('h1',class_="yhB1nd").text
    except:
       name:'No'
       rating:'No'
       price:'No'
    print(image)
    print(name)
    print(price)
    print(rating)







    





