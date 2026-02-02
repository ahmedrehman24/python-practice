import time
import random

#name = input("Enter your name: ")

# result = len(name)
# print(result)

# result=name.find("a")
# print(result)

####################################################


# username = input("Enter a username: ")


# length = len(username)

# if length > 12:

#     print("Username is too long")

# elif username.find(" ") != -1:

#     print("Username can't contain a space")

# elif username.isalpha() != True:

#     print("Username can't contain a digit")
# else:

#     print("Username is valid")

##########################################################


# credit_number = input("enter your credit card number: ")


# if len(credit_number) == 16 and credit_number.isdigit():

#     last_digits = credit_number[-4:]

#     print(f"xxxx-xxxx-xxxx-{last_digits}")
# else:

#     print("Invalid credit card number (must be 16 digits and contain only numbers)")

##########################################################



# price1 = 101.455

# price2 = 45.678

# price3 = 33.789


# print(f"The price of item 1 is: ${price1:.2f}")

# print(f"The price of item 2 is: ${price2:.2f}")

# print(f"The price of item 3 is: ${price3:.2f}")


##########################################################


# name = input("enter your name")


# while name == "": 

#     print("you did not enter your name")

#     name = input("enter your name")

#     print(f"hello {name}")



# num = int(input("enter a number between 1- 10:"))


# while num < 1 or num > 10:

#    print(f"{num}is not valid") 

#    num = int(input("enter a number between 1- 10:"))


# print(f"your number is {num}")
##########################################################


# for x in reversed(range(1,11,2)):

#     print(x)

# print ("happy new year")



# my_time = int(input ( "enter the time in seconds: "))


# for i in range(my_time, 0, -1):

#     seconds = i % 60

#     minutes = i // 60

#     hours = i // 3600

#     print(f"{hours:02d}:{minutes:02d}:{seconds:02d}")

#     time.sleep(1)

# print("time's up!")


###################Lists######################


# fruits = ["apple", "banana", "cherry" , "orange" , "mango"]


# print(fruits[4])


##########################Shopping Cart Program######################


products = []

prices = []

total = 0


# while True:

#     name = input("Enter a product name: ")

#     price = float(input("Enter the price: "))

#     products.append(name)

#     prices.append(price)

#     total += price

#     print(f"Added {name} to the cart")

#     choice = input("Do you want to add another product? (yes/no): ")

#     if choice == "no":

#         break


# print("/nshopping cart:")

# for name, price in zip(products, prices):

#     print(f"{name}: ${price:.2f}")

# print(f"Total: ${total:.2f}")


####################2dlists#####################


# groceries = [["apple", "banana", "cherry"], ["carrot", "broccoli", "spinach"], ["chicken", "beef", "turkey"]]


# for items in groceries:
#     for item in items:
#         print(item , end=" ")
#     print()



# num_pad = ((1,2,3), (4,5,6), (7,8,9), ("*",0,"#"))


# for row in num_pad:

#     for num in row:
#         print(num, end=" ")
#     print()


#####################Quiz Game#####################


# questions = (("what was the name of your first school?"),("who was your first friend?"),("what was your favorite color?"),("what was your favorite food?"),("what was your favorite subject?"))

# options = (("A.bgs", "B.adb", "C.hec", "D.ddd"),

#            ("A.moiz", "B.adb", "C.hec", "D.ddd"),

#            ("A.red", "B.adb", "C.hec", "D.ddd"),

#            ("A.pizza    ", "B.adb", "C.hec", "D.ddd"),

#            ("A.computer", "B.adb", "C.hec", "D.ddd"))   


# answers = ("a", "a", "a", "a", "a")

# guesses = []

# score = 0

# question_num = 0


# for question in questions:
#     print("-----------------------------------")

#     print(question)

#     for option in options[question_num]:
#         print(option)

#     guess = input("Enter your answer: ").lower()

#     guesses.append(guess)

#     if guess == answers[question_num]:

#        score += 1

#        print("Correct!")
#     else:

#        print("Wrong!")

#     question_num += 1

# print("-----------------------------------")

# print("Quiz Results:")
# print("-----------------------------------")

# for answer in answers:

#     print(answer, end=" ")
# print()

# for guess in guesses:

#     print(guess , end=" ")
# print()

# print(f"Your score is: {score}")


######################### iteration over list using for loop ##########################
    

# fruits = ["apple", "banana", "cherry", "apple", "mango"]


# for item in fruits[:]:   
#     if item == "apple":

#         fruits.remove(item)

# print(fruits)

###############################Dictionary############################


# dictionary = {"name": "John", "age": 30, "city": "New York"}


# dictionary.update({"country": "USA"})

# print(dictionary)

#####################################################################


#########################consession stand program#########################


# menu = {"pizza": 2.50, "burger": 3.00, "fries": 1.50, "drink": 1.00}

# cart = []

# total = 0


# for key, value in menu.items():

#     print(f"{key:10}: ${value:.2f}")
# print ("-----------------------------------")

# while True:

#     food = input("enter an item you want to buy: (q to quit)").lower()

#     if food == "q":

#         break

#     elif menu.get(food) is not None:

#         cart.append(food)


# print("-----------------your order------------------:")
# for food in cart:

#     total += menu.get(food)
#     print(food, end=" ")

# print()

# print(f"your total is: ${total:.2f}")

#####################################################################


# low = 1

# high = 100

# options = ("rock", "paper", "scissors")

# cards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]


# #number = random.randint(low, high)

# # option = random.choice(options)
# # print(option)

# # random.shuffle(cards)
# # print(cards)


#############################number guessing game###########################################


# lowest_num = 1

# highest_num = 100

# answer = random.randint(lowest_num , highest_num)

# guesses = 0

# is_running = True


# print ("-----------------python number guessing game------------------")

# print (f"guess the number between {lowest_num} and {highest_num}")
 

# while is_running:

#     guess = input("enter your guess: ")
    

#     if guess.isdigit():

#         guess = int(guess)

#         guesses += 1

#         if guess < lowest_num or guess > highest_num:

#             print("out of range")

#             print (f"please enter a valid number between {lowest_num} and {highest_num}")

#         elif guess < answer:

#             print("too low")

#         elif guess > answer:

#             print("too high")
#         else:
#             print("correct")

#             print(f"you got it in {guesses} guesses")

#             is_running = False
#     else:

#         print("invalid guess")

#         print (f"please enter a valid number between {lowest_num} and {highest_num}")


###################################rock paper scissors game###########################################  


# options = ("rock", "paper", "scissors")

# running = True


# while running:


#     player = None

#     computer = random.choice(options)


#     while player not in options:

#         player = input("enter your choice (rock, paper, scissors): ").lower()


#     print(f"player: {player}")

#     print(f"computer: {computer}")


#     if player == computer:
#         print("tie")

#     elif player == "rock" and computer == "scissors":

#         print("player wins")

#     elif player == "paper" and computer == "rock":

#         print("player wins")

#     elif player == "scissors" and computer == "paper":

#         print("player wins")
#     else:

#         print("computer wins")


#     if not input("play again? (yes/no): ").lower() == "yes":

#         running = False


# print("thanks for playing") 

#######################################################


# def create_name(first , last):

#     first = first.capitalize()

#     last = last.capitalize()

#     return first + " " + last

# first_name = input("enter your first name: ").lower()

# last_name = input("enter your last name: ").lower()

# full_name = create_name(first_name, last_name)

# print ("your full name is: ")

# print(full_name)

#######################################################

# def count (start , end ):

#     for x in range (start , end + 1):

#         print(x)

#         time.sleep(1)

#     print("done!")


# count(1, 10)


##########################keyword arguments#############################

# def hello (greeting, title , first , last):

#     print(f"{greeting} {title} {first} {last}")


# hello("hello", first="john", last="doe", title="mr")


######################Arbitrary arguments#############################


#args = arguments

#kwargs = keyword arguments


def display_name(*args):
    for arg in args:
        print(arg, end=" ")
    
display_name("john", "doe", "smith", "jones" ) 