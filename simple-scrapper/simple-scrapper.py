import requests
from bs4 import BeautifulSoup 

url = "http://books.toscrape.com/?"

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Safari/605.1.15"
}

response=requests.get(url,headers=headers)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    books = soup.find_all('h3')

    for book in books:
        title = book.get_text(strip = True)
        print(f"-{title}\n")
else:
   print("Error") 
