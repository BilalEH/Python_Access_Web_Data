import urllib.request
from bs4 import BeautifulSoup

url = input('Enter URL: ')
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

span_tags = soup.find_all('span', class_='comments')

total = 0
count = 0

for tag in span_tags:
    number = int(tag.contents[0])
    total += number
    count += 1

print('Count', count)
print('Sum', total)