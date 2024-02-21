import requests
from bs4 import BeautifulSoup

def scrape_headlines(url):
    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find the elements containing headlines (you may need to inspect the webpage to find the correct tags)
        headline_tags = ['h1', 'h2', 'h3']
        headlines = []
        for tag in headline_tags:
            headlines.extend(soup.find_all(tag))

        # Extract the text from the headlines and print them
        for headline in headlines:
            print(headline.text.strip())
    else:
        print('Failed to retrieve webpage:', response.status_code)

# URL of the website to scrape
url = input("Enter the URL of the website to scrape: ")

# Call the function to scrape headlines
scrape_headlines(url)
