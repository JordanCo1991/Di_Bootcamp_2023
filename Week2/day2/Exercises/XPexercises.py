# # Ex 1#

# # my_fav_numbers = [2,7,8,13,24]
# # my_fav_numbers.insert (3, 10)
# # my_fav_numbers.append(26)

# # friend_fav_numbers = [4,5,33,22,20]
# # our_fav_numbers = my_fav_numbers + friend_fav_numbers
# # print(our_fav_numbers)

# # Ex 2#


# # Ex3 #

# # basket = ["Banana", "Apples", "Oranges", "Blueberries"]
# # basket.pop(0)
# # basket.pop()
# # basket.append("Kiwi")
# # basket.insert(0,"Apples")
# # basket.count("Apples")
# # basket.clear()
# # print(basket)


# # Exercise 4
# # list = [1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5]
# # floats_num = list[::2]
# # print(floats_num)


# # #Exercise 5
# # numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

# # for num in numbers :
# #     if num % 2 == 0 :
# #         print("the number is even")
# #     else :
# #         print(num)




# # Exercise 7



# favorite_fruits_input = input("Please enter your favorite fruit(s), separated by a space: ")
# # favorite_fruits = favorite_fruits_input.split()
# # chosen_fruit = input("Please enter the name of a fruit: ")
# # if chosen_fruit in favorite_fruits:
# #     print("You chose one of your favorite fruits! Enjoy!")
# # else:
# #     print("You chose a new fruit. I hope you enjoy.")


# exe 9

total_cost = 0
num_family_members = int(input("How many family members want a ticket? "))


for i in range(num_family_members):
    age = int(input("Enter the age of family member {}: ".format(i+1)))
    

    if age < 3:
        ticket_cost = 0
    elif age <= 12:
        ticket_cost = 10
    else:
        ticket_cost = 15
    

    total_cost += ticket_cost


print("The total cost for all family members is $", total_cost)
