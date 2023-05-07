text = input("Enter a string (10 characters): ")
user_imput =len(text)

if user_imput > 10:
    print ("Your String is too long")

else: user_imput < 10 
print ("Your String is too short")


string = input("Enter a string: ")

for i in range(1, len(string) + 1):
    substring = string[:i]
    print(substring)

