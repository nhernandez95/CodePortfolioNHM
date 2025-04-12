# © 2025 Nathanael Hernandez – Universal version
# This script has been sanitized to remove any proprietary or sensitive information.

# Author: Nathanael H.
# Date: 2024-10-03
# This code is used to add memos to merchants in IRIS CRM using the IRIS API.
# The code sends a POST request to the IRIS API with the memo data and merchant ID.

import requests

# headers for the API request
# The headers include the content type and the API key for authentication
headers = {
    'Content-Type':'application/json',
    'X-API-KEY':'insert your API key here'
}

# The data to be sent in the POST request
# This includes the memo text and visibility status
data = {
  "memos": [
    {
      "text": "This is a test memo",
      "is_visible": "Yes"
    }
  ]
}

url = "insert your URL here"

mids = ['insert your merchant IDs here']

# Loop through each merchant ID and send a POST request to add the memo
# The URL is constructed using the merchant ID
for mid in mids:
    url = f"https://iriscrm.com/api/v1/merchants/{mid}/memos"
    response = requests.post(url,headers=headers,json=data)
    if response.status_code==200:
        print(f'memo added to {mid} in {url}')
    else:
        print(f'memo not added to {mid} on {url}')




