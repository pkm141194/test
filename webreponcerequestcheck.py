
import requests

r = requests.get('https://www.amazon.com.au/')
#print(dir(r))
#print(help(r))
print(text(r))
import requests
import bs4

result = requests.get("https://www.amazon.com.au/NETGEAR-Whole-Tri-Band-System-RBK752/dp/B089NMH2WX/ref=sr_1_1?dchild=1&keywords=Netgear%2BOrbi%2BAX4200%2BTri-Band%2BWi-Fi%2B6%2BMesh%2BSystem%2B(2%2BPack)&qid=1634016452&sr=8-1&th=1",verify=False)


#print the result
soup = bs4.BeautifulSoup(result.text,'lxml')
print(soup)
prd_price = soup.select('div#price table.a-lineitem span#priceblock_ourprice')[0].getText()if len(
                        soup.select('div#price table.a-lineitem span#priceblock_ourprice')) > 0 else "0.00",
)

print("Price: ",prd_price)
                

'''
from requests_html import HTMLSession
session = HTMLSession()
given_url = "https://www.ebay.com.au/itm/164376839971?epid=17040739296&hash=item26459f8723:g:HF4AAOSwu4lg5TBX"
r = session.get(url=given_url)
print(r)
print (r.html)

#print(f'{len(items)} Results Found for: {given_url}')
'''
