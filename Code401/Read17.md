# Web Scraping

[web scraping](https://towardsdatascience.com/how-to-web-scrape-with-python-in-4-minutes-bc49186a8460)

[wiki-web scraping](https://en.wikipedia.org/wiki/Web_scraping)

Automating web parsing.

- Usually not legal for commercial use.
- Can cause blocking issues if you are using too much bandwidth.

## Uses

- data mining
- price comparison
- web change detection
- weather data
- web indexing

### Libraries

### BeautifulSoup

```python
import requests
import urllib.request
import time
from bs4 import BeautifulSoup

url = 'http://somethingsomething.com
response = requests.get(url)

# Parse response with BeautifulSoup
soup = BeautifulSoup(response.txt, 'html.parser')

soup.findAll('a')

single_a_tag = soup.findAll('a')[5]
link = single_a_tag['href']

```

### URL Requests

```python
line_count = 1
for tag in soup.findAll('a'):
  link = tag['href']
  download_url = 'http://wwwsomethingsomething.com'+link
  urllib.request.urlretrieve(download_url,'./',+link[link.find('/turnstile_')+1:])
  time.sleep(1)  # prevent spamming site
  line_count += 1

```

[Prevent getting blocked](https://www.scrapehero.com/how-to-prevent-getting-blacklisted-while-scraping/)

- robots.txt file
  > User-agent: *
  > Disallow:/

- slow down the web crawling
- IP proxy
- Rotate User Agents  on request headers
- Do not scrape behind a login
- Use capcha services for large scaping



#### Beautiful Soup

[Beautiful Soup Docs](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)

> poetry add beautifulsoup4

```python
from bs4 import BeautifulSoup

soup = BeautifulSoup(html_doc, 'html.parser')

soup.prettify()
soup.title
soup.title.name
soup.title.string
soup.title.parent.name
soup.p
soup.p['className']
soup.a
soup.find_all('a')
soup.find(id='fishcakes')

link.get('href')

## Tags
tag = soup.b
type(tag)  # tags match an html tag

tag.name
tag.attrs


# 
for link in soup.find_all('a'):
  print(link)

```