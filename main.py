import json

try:
  with open('followers.json') as file:
    followers_json = json.load(file)
except FileNotFoundError:
  print('Error: followers.json not found')
  followers_json = []

try:
  with open('following.json') as file:
    following_json = json.load(file)
except FileNotFoundError:
  print('Error: following.json not found')
  following_json = []

following_list = []
for following in following_json.get("relationships_following", []):
  following_list.append(following.get("string_list_data", [{}])[0].get("value"))

for follower in followers_json:
  if follower.get("string_list_data", [{}])[0].get("value") in following_list:
    following_list.remove(follower.get("string_list_data", [{}])[0].get("value"))

for user in following_list:
  print(user)