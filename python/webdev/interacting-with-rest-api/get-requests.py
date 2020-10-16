# Make sure to install requests first: pip install requests
import requests, json # imports both requests and json into this python program

# GET REST API from gorest.co.in, retrieving users
response = requests.get('https://gorest.co.in/public-api/users')
# Turning the response content into a JSON object
users = json.loads(response.text)['data'] # Specifically getting the "data" key to process important data only

print('Number of users: ' + str(len(users))) # Converts the number of users within the list then prints it with a String
print('First person in the list: ' + users[0]['name']) # Accesses the first index in a list/array (0), and accesses the "name" key
print('Last person in the list: ' + users[len(users)-1]['name']) # Gets the last index in a list (length - 1) and accesses the "name" key