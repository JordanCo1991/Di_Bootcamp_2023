text = input("Please enter a string that is 10 characters long: ")

length = len(text)
if length < 10:
    print("String is too short,you have only", len(text),"characters")
elif length > 10:
    print("String is too long, you have", len(text),"characters")
else:
    print("String length is :" , len(text))


string = input("Enter a string: ")

for bla in range(1, len(string) + 1):
    substring = string[:bla]
    print(substring)

