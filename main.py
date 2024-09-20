import json

# Load data from 'following.json' and 'followers.json'
with open('following.json') as file:
    following_json = json.load(file)

with open('followers.json') as file:
    followers_json = json.load(file)

#  extract usernames
def extract_usernames(json_data, key):
    usernames = []
    for item in json_data[key]:
        try:
            if "string_list_data" in item and isinstance(item["string_list_data"], list):
                usernames.append(item["string_list_data"][0]["value"])
        except (IndexError, KeyError, TypeError):
            # 
            continue
    return usernames

# Extract usernames from the JSON data
following_list = extract_usernames(following_json, "relationships_following")
followers_list = extract_usernames(followers_json, "relationships_followers")

# compare
people_not_following = [user for user in following_list if user not in followers_list]

# Assign a unique ID to each user 
unique_ids = {}
current_id = 1
for user in people_not_following:
    if user not in unique_ids:
        unique_ids[user] = current_id
        current_id += 1

# Display the list of people who unfollowed and their unique IDs
print("LIST OF PEOPLE WHO UNFOLLOWED:")
for user in people_not_following:
    print(f"- Username: {user}, Unique ID: {unique_ids[user]}")
