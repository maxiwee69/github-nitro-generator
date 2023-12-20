if you think this is fake or something watch https://www.youtube.com/watch?v=yWqqMp6ca30&t

This script sends POST requests to a specified URL and writes the received tokens to a file named 'nitrolinks.txt'. The script continues to send requests until it has been rate limited 5 times in a row.

Modules:

requests: Used to send HTTP requests.
json: Used to parse the JSON response from the server.
Constants:

QUANTITY: The number of times to call the gen function after the rate limit check. Currently set to 2.
base_path: The base URL to which the received token is appended to form the complete link.
url: The URL to which the POST requests are sent.
payload: The JSON payload to be sent in the POST request.
headers: The headers to be included in the POST request.
Functions:

gen: This function sends a POST request to the specified URL and writes the received token to a file. If the server responds with a 429 status code (rate limit exceeded), the function returns False. If the server responds with a 2xx status code (successful), the function writes the token to a file and returns True. If the server responds with any other status code, the function prints an error message and returns True.
Main Script: The script first checks for rate limiting by calling the gen function in a while loop until it has been rate limited 5 times in a row. After the rate limit check, the gen function is called QUANTITY times.
