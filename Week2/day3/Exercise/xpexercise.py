# Exercise 1#


# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]

# result= zip(keys, values)
# print (list(result))

# Exercise 2 #


# family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}

# total_cost = 0

# for name, age in family.items():
#     if age < 3:
#         ticket_price = 0
#     elif 3 <= age <= 12:
#         ticket_price = 10
#     else:
#         ticket_price = 15

#     total_cost += ticket_price
#     print(f"{name} has to pay ${ticket_price}.")

# print(f"\nTotal cost for the family: ${total_cost}.")

 ## Exercise 3##


# brand = {
#     "name": "Zara",
#     "creation_date": 1975,
#     "creator_name": "Amancio Ortega Gaona",
#     "type_of_clothes": ["men", "women", "children", "home"],
#     "international_competitors": ["Gap", "H&M", "Benetton"],
#     "number_stores": 7000,
#     "major_color": {
#         "France": ["blue"],
#         "Spain": ["red"],
#         "US": ["pink", "green"]
#     }
# }

# brand["number_stores"] = 2
# print("Zara's clients are Men, Women, Children & Home")

# brand["country_creation"] = "Spain"
# if "international_competitors" in brand:
#     brand["international_competitors"].append("Desigual")

# del brand["creation_date"]
# print(brand["international_competitors"][-1])
# print(brand["major_color"]["US"])
# print(len(brand))
# print(len(brand))

# more_on_zara = {
#     "creation_date": 1975 , 
#     "number_stores": 10000 ,
# }

# brand.update(more_on_zara)
# print(brand ["number_stores"])

#exercise 4

users = ["Mickey", "Minnie", "Donald", "Ariel", "Pluto"]
disney_users_B = {}

for i, user in enumerate(users):
    disney_users_B[i] = user

print(disney_users_B)


users = ["Mickey", "Minnie", "Donald", "Ariel", "Pluto"]
disney_users_C = {user: i for i, user in enumerate(users)}
disney_users_C = dict(sorted(disney_users_C.items(), key=lambda x: x[0]))

print(disney_users_C)


users = ["Mickey", "Minnie", "Donald", "Ariel", "Pluto"]
disney_users_A = {}

for i, user in enumerate(users):
    if 'i' in user:
        disney_users_A[user] = i

print(disney_users_A)


users = ["Mickey", "Minnie", "Donald", "Ariel", "Pluto"]
disney_users_A = {}

for i, user in enumerate(users):
    if user[0] in ['m', 'p']:
        disney_users_A[user] = i

print(disney_users_A)
