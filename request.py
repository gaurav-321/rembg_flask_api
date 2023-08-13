import time
import requests
import json

# API endpoint URL
API_URL = 'https://reqres.in/api/users'

# Payload data for the POST request
PAYLOAD = {
    'name': 'John Doe',
    'job': 'Software Engineer'
}
API_TEST_COUNT = 10
API_SPEED_TEST = True
print("[+]Starting Api Test")
for i in range(API_TEST_COUNT):
    s_time = time.time()
    try:
        # Send the POST request
        response = requests.post(API_URL, data=json.dumps(PAYLOAD))

        # Check if the request was successful (status code 201 for created)
        if response.status_code == 201:
            # Parse the response as JSON
            data = response.json()

            # Process the response data
            print("\t[*]New User Created with ID:", data['id'])
        else:
            print('[-]Error: Request failed with status code', response.status_code)
    except requests.exceptions.RequestException as e:
        print('[-]Error: An exception occurred while making the request:', str(e))
    if API_SPEED_TEST:
        time_elapsed = time.time() - s_time
        print(f"[+]It took {time_elapsed}s to complete api call.")

print("[+]Api Test Finished")