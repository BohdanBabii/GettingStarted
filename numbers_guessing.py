from random import randrange

def guess_the_number(num: int, random_num: int, min_boarder: int, max_boarder)->tuple[bool, int, int]:

    if num > random_num:
        print("Number is lower")
        max_boarder = min(max_boarder,num)
        return False, min_boarder, max_boarder
    elif num < random_num:
        print("Number is higher")
        min_boarder = max(min_boarder,num)
        return False, min_boarder, max_boarder
    
    print(f"Guessed correctly, number {random_num} is right!!!")
    return True, min_boarder, max_boarder


print("What is the range of the numbers to guess?")
num_of_guesses = str("inf")
n_start = int(input("Enter Lower Boundary: "))
n_end = int(input("Enter Higher Boundary: "))
min_boarder = n_start
max_boarder = n_end
random_num = randrange(n_start,n_end)
correctly_guessed=False

print("How many guesses?")
num_of_guesses = int(input())

while not correctly_guessed:
    num_of_guesses -= 1
    print("Guess the Number: ")
    num = int(input())
    correctly_guessed, min_boarder, max_boarder = guess_the_number(num=num, random_num=random_num, min_boarder=min_boarder, max_boarder=max_boarder)

    if num_of_guesses <= 0:
        print("Reached max number of tries.")
        print("Game Over")
        break

    if  not correctly_guessed:    
        print()
        print(f"Number of guesses: {num_of_guesses}")
        print(f"Current minimal value  {min_boarder}")
        print(f"Current maximum vallue {max_boarder}")
        print()