# import json

# user = {
#     "firstName": "Jane",
#     "lastName": "Doe",
#     "hobbies": ["running", "sky diving", "singing"],
#     "age": 35,
#     "email" : None,
#     "children": [
#         {
#             "firstName": "Alice",
#             "age": 6,
#             "loves_school" : True
#         },
#         {
#             "firstName": "Bob",
#             "age": 8,
#             "loves_school" : False
#         }
#     ]
# }

# # covert a cictionary to a json string
# # my_json = json.dumps(user)
# # print(my_json)


# # Loads converts a json string into python dictionary


# import requests
# response = requests.get("http://api.open-notify.org/iss-now.json")
# print(response)


import requests
response = requests.get("https://pokeapi.co/api/v2/pokemon/pikachu")

info = response .json()
type_pickachu = info["types"][0]["type"]['name']
sentance = f"Pickachu is of type {type_pickachu}"
print(sentance)
