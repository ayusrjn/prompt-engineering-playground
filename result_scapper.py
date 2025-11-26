import requests
from bs4 import BeautifulSoup
import time

def check_webpage(url):
    try:
        # Send a GET request to the webpage
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        
        # Parse the HTML content
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Print basic information
        print(f"Status Code: {response.status_code}")
        print(f"URL: {url}")
        print(f"Title: {soup.title.string if soup.title else 'No title found'}")
        print(f"Content Length: {len(response.content)} bytes")
        
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

# Example usage
if __name__ == "__main__":
    webpage_url = "https://www.beu-bih.ac.in/backend/v1/result/get-result?year=2023&redg_no=23155126031&semester=III&exam_held=July/2025"
    
    while True:
        check_webpage(webpage_url)
        time.sleep(2)  # Wait 2 seconds before next check