import requests
import json
import string

# Constants
QUANTITY = 2
base_path = "https://discord.com/billing/partner-promotions/1180231712274387115/"
url = 'https://api.discord.gx.games/v1/direct-fulfillment'
payload = {
    "partnerUserId": "d05d65629f9b076a55c0661fcf7e9871bbf7052042d26b5185784d29f06081ab"
}

# Headers for the HTTP request
headers = {
    'authority': 'api.discord.gx.games',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/json',
    'origin': 'https://www.opera.com',
    'referer': 'https://www.opera.com/',
    'sec-ch-ua': '"Opera GX";v="105", "Chromium";v="119", "Not?A_Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:121.0) Gecko/20100101 Firefox/121.0'
}

def gen():
    """
    This function sends a POST request to the specified URL and writes the received token to a file.
    If the server responds with a 429 status code (rate limit exceeded), the function returns False.
    If the server responds with a 2xx status code (successful), the function writes the token to a file and returns True.
    If the server responds with any other status code, the function prints an error message and returns True.
    """

    # Send a POST request
    response = requests.post(url, json=payload, headers=headers)

    # Check if the rate limit has been exceeded
    if response.status_code == 429:
        print("Rate limited")
        return False

    # Check if the request was successful
    if response.status_code // 100 == 2:
        try:
            # Extract the token from the response
            token = response.json().get('token', 'No token found')
            link = base_path + token

            # Write the link to the file 'nitrolinks.txt'
            with open('nitrolinks.txt', 'a') as file:
                file.write(link + "\n")
            print(link)
        except json.JSONDecodeError:
            print("JSONDecodeError: Unable to parse response as JSON.")
            print("Response text:", response.text)
        except Exception as e:
            print("An unexpected error occurred:", str(e))
    else:
        print(f"Request failed with status code {response.status_code}")
        print("Response text:", response.text)

    return True