import requests
import json
import sys

QUANTITY = 2
base_path = "https://discord.com/billing/partner-promotions/1180231712274387115/"
url = 'https://api.discord.gx.games/v1/direct-fulfillment'
payload = {
    "partnerUserId": "d05d65629f9b076a55c0661fcf7e9871bbf7052042d26b5185784d29f06081ab"
}
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
    # Add a variable to track how many times a proxy has been used
    proxy_use_count = 0
    used_proxy = False
    proxies = None

    while True:  # Add a loop to keep sending requests until a successful response is received
        # Send a POST request
        response = requests.post(url, json=payload, headers=headers, proxies=proxies)

        # Check if the rate limit has been exceeded
        if response.status_code == 429:
            print("You have been rate limited.")
            sys.exit()
            # proxy code(horribly written and not working properly) :(
            if used_proxy and proxy_use_count >= 2:
                # Ask the user if they want to use another proxy
                use_another_proxy = input("The current proxy has been rate limited. Do you want to use another proxy? (yes/no): ").lower() == "yes"
                if not use_another_proxy:
                    print("Exiting the program as no other proxy is to be used.")
                    sys.exit()
                proxy_use_count = 0  # Reset the count for the new proxy
            else:
                print("You have been rate limited. Do you want to use a proxy?")
                use_proxy = input("Do you want to use a proxy? (yes/no): ").lower()
                if use_proxy == "yes":
                    proxy = input("Please enter the proxy URL: ")
                    proxy_auth_needed = input("Is authentication needed for the proxy? (yes/no): ").lower() == "yes"
                    if proxy_auth_needed:
                        proxy_username = input("Please enter the proxy username: ")
                        proxy_password = input("Please enter the proxy password: ")
                        proxies = {
                            "http": f"http://{proxy_username}:{proxy_password}@{proxy}",
                            "https": f"https://{proxy_username}:{proxy_password}@{proxy}",
                        }
                    else:
                        proxies = {
                            "http": proxy,
                            "https": proxy,
                        }
                    used_proxy = True
                else:
                    print("Exiting the program as no proxy is to be used.")
                    sys.exit()

            proxy_use_count += 1  # Increment the count each time a proxy is used

        # Check if the request was successful
        elif response.status_code // 100 == 2:
            try:
                # Extract the token from the response
                token = response.json().get('token', 'No token found')
                link = base_path + token

                # Write the link to the file 'nitrolinks.txt'
                with open('nitrolinks.txt', 'a') as file:
                    file.write(link + "\n")
                print(link)
                break  # Exit the loop once a successful response is received
            except json.JSONDecodeError:
                print("JSONDecodeError: Unable to parse response as JSON.")
                print("Response text:", response.text)
            except Exception as e:
                print("An unexpected error occurred:", str(e))
        else:
            print(f"Request failed with status code {response.status_code}")
            print("Response text:", response.text)
        if response.status_code == 504:
            print("504 error, retrying...")


    return True

print("Discord Nitro Generator and by elily_uwu on discord")
print("start? (y/n)")
start = input()
if start == "n":
    print("but why did you start it then?")
    sys.exit()
elif start == "y":
    gen()
else:
    print("invalid input")
    sys.exit()

rate_limit_count = 0
while rate_limit_count < 5:
    if not gen():
        rate_limit_count += 1
    else:
        rate_limit_count = 0

for i in range(QUANTITY):
    gen()

# if you want to use this code, please give credit to elily_uwu on discord
# oh and also, please dont use this for malicious purposes
# thanks :)
# one last thing, hi :) 
    





































#pls fix my code if you can, i am a beginner and i dont know how to fix it :(