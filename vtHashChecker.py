#
# Author: Andrew Bornt
# sources: https://developers.virustotal.com/v2.0/reference/file-report
# and a lot of trial and error
#

import requests
import json

checkingResponse = 1
while checkingResponse == 1:
    checkingKey = 1
    while checkingKey == 1:
        api_key = input("Please enter your API key for Virus Total: ")
        if len(api_key) == 0:
            print("API Key cannot be empty.")
        else:
            break

    checkingHash = 1
    while checkingHash == 1:
        resource = input("Please enter the md5 hash you want to check: ")
        # md5sum hashes are 32 characters in length
        if len(resource) != 32:
            print("Please enter an appropriate hash.")
        else:
            break

    # the next few lines are directly from API documentation.
    url = 'https://www.virustotal.com/vtapi/v2/file/report'

    params = {'apikey': api_key, 'resource': resource}

    response = (requests.get(url, params=params))

    # prints out the status code 
    print(response)

    try:
        # if the response cannot be parsed correctly, we received something other than a status code 200.
        response = json.loads(response.text)
        break
    except:
        print("Your API key is invalid")


try:
    if (response['positives'] > 5):
        print("The file is malicious.")
    elif (response['positives'] > 0):
        print("The file is potentially malicious.")
    else:
        print("The file is not known to be malicious.")
except:
    print("Hash not found.")
