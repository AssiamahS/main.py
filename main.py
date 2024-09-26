

import requests
from bs4 import BeautifulSoup

def scrape_videos(url):
    try:
        # Send a GET request to the URL
        response = requests.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the HTML content of the page
            soup = BeautifulSoup(response.text, 'html.parser')

            # Find all iframe elements on the page
            iframe_elements = soup.find_all('iframe')

            # Extract video links from the 'src' attribute of the iframes
            video_links = []
            for iframe in iframe_elements:
                if 'src' in iframe.attrs:
                    video_links.append(iframe['src'])

            return video_links
        else:
            print(f"Failed to retrieve the page. Status code: {response.status_code}")
    except requests.RequestException as e:
        print(f"An error occurred during the request: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

    return []

# Example usage
url_to_scrape = "https://www.dailymotion.com/video/x6wh5ey"  # Replace with the URL of the page
video_links = scrape_videos(url_to_scrape)

if video_links:
    print("Found video links:")
    for link in video_links:
        print(link)
else:
    print("No video links found.")
