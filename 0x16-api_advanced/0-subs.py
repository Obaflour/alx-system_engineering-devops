import requests

def number_of_subscribers(subreddit):
    # Set the API endpoint URL and headers
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    headers = {'User-Agent': 'Custom User Agent'}

    # Send a GET request to the API endpoint and check for errors
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        return 0

    # Parse the JSON data from the API response and return the subscriber count
    data = response.json()
    return data['data']['subscribers']
