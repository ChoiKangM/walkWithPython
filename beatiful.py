import requests
import bs4

response = requests.get('http://finance.naver.com/sise/').text
text = bs4.BeautifulSoup(response)
kospi = text.select_one("#KOSPI_now")
print(kospi.text)