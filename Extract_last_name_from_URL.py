import urllib.request, urllib.error
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')
count = int(input('Enter count: '))
position = int(input('Enter position: ')) - 1

print(f'Retrieving: {url}')

for i in range(count):
    try:
        html = urllib.request.urlopen(url, context=ctx).read()
        soup = BeautifulSoup(html, 'html.parser')
        
        tags = soup('a')
        if position >= len(tags):
            print(f"Error: Position {position+1} is out of range for this page")
            break
            
        url = tags[position].get('href', None)
        print(f'Retrieving: {url}')
        
    except Exception as e:
        print("Error:", e)
        break

last_name = url.split('_')[-1].split('.')[0]
print("\nThe answer to the assignment is:", last_name)