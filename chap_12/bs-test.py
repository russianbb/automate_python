import bs4, requests

res = requests.get('https://nostarch.com')
res.raise_for_status()

noStarchSoup = bs4.BeautifulSoup(res.text, 'html.parser')
type(noStarchSoup)