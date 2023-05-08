# number = int(input("Enter a number: "))
# length = int(input("Enter the desired length: "))

# multiples = []
# count = 0
# current_multiple = 0

# while count < length:
#     current_multiple += number
#     multiples.append(current_multiple)
#     count += 1

# print("List of multiples of", number, "until length", length, ":")
# print(multiples)


input_string = input("Enter a string: ")
new_string = ""
for s in range(len(input_string)):
    if s == 0 or input_string[s] != input_string[s-1]:
        new_string += input_string[s]

print("New string with duplicate consecutive letters removed:")
print(new_string)
