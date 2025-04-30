import urllib.request
import xml.etree.ElementTree as ET

def get_sum_from_url(url):
    print(f"Retrieving {url}")
    try:
        # Open the URL and read the data
        with urllib.request.urlopen(url) as response:
            data = response.read()
        
        print(f"Retrieved {len(data)} characters")
        
        # Parse the XML data
        tree = ET.fromstring(data)
        
        # Find all count elements using XPath
        counts = tree.findall('.//count')
        
        # Extract values and convert to integers
        count_values = [int(count.text) for count in counts]
        
        print(f"Count: {len(count_values)}")
        print(f"Sum: {sum(count_values)}")
        
        return sum(count_values)
    
    except Exception as e:
        print(f"Error: {e}")
        return None

def main():
    # Prompt for URL
    url = input("Enter location: ")
    
    # Get the sum
    total = get_sum_from_url(url)
    
    if total is not None:
        print(f"The sum of all comment counts is: {total}")

if __name__ == "__main__":
    main()