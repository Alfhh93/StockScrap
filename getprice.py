from bs4 import BeautifulSoup
import requests


url = 'https://finance.yahoo.com/quote/FTNT/'
page = requests.get(url, headers={
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36",
})
soup = BeautifulSoup(page.text, 'html.parser')
price = soup.find('fin-streamer', {'class': 'Fw(b) Fz(36px) Mb(-4px) D(ib)'}).text

print(price)

# thanks: https://stackoverflow.com/questions/70524523/why-is-web-scraping-stock-prices-through-beautiful-soup-returning-a-different-pr
