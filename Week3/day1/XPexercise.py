# # # exercise 1
# 
# 
# class Cat:
# #     def __init__(self, cat_name, cat_age):
# #         self.name = cat_name
# #         self.age = cat_age

# # def oldest_cat (lst_cat):
# #     if lst_cat[0].age >= lst_cat[1].age:
# #         oldest = lst_cat[0]

# #     else:
# #         lst_cat[0].age <= lst_cat[1].age
# #         oldest = lst_cat[1]

# #     return  print(f'The oldest cat {oldest.name},he is {oldest.age} years old')

  



# # first_cat = Cat("Tom", 5)
# # second_cat = Cat("Miaou", 3)

# # cats = [first_cat, second_cat]

# # oldest_cat(cats)


# exercise 2

# class Dog:
#     def __init__(self,dog_name,height_dog) :
#         self.name = dog_name
#         self.height = height_dog
    
#     def bark(self) :
#         print(f"{self.name} said Woof !!")
    
#     def jump(self) :
#         high_jump = height_dog * 2
#         print(f"{jump.name} jumps {jump.high_jump} cm high")
#         return high_jump


# davids_dog = Dog("Rex", 50)
# print(f"his name is {davids_dog.name} and his height is {davids_dog.height} cm")
# davids_dog.bark
# davids_dog.jump

# sarahs_dog = Dog("Teacup", 20)
# print(f"his name is {sarahs_dog.name} and his height is {sarahs_dog.height} cm")
# sarahs_dog.bark
# sarahs_dog.jump

# if davids_dog.height >= sarahs_dog.height:
#     print(f"{davids_dog.name} bigger than {sarahs_dog.name}" )

# else:
#      print(f"{sarahs_dog.name} smaller than {davids_dog.name}" )

# exercise 3


class Song:
    def __init__(self, lyrics) :
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for i in self.lyrics:
            print(f"{i}")

    
stairway = Song(["There’s a lady who's sure","all that glitters is gold", "and she’s buying a stairway to heaven"])

stairway.sing_me_a_song()





