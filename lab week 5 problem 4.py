# Camryn Echevarria
# 11/1/2022

# the code has to print number from 1-50 and then divide it by 3 and 5.

# number = int(input("what is your number?\n"))
for numbers in range(1, 51):

    # this is printing all the numbers that are divisible by 3 as the word
    if numbers % 3 == 0 and numbers % 5 == 0:
        print("Divisible by both")

    elif numbers % 3 == 0:
        print("Divisible by 3")

    elif numbers % 5 == 0:
        print("Divisible by 5")

    else:
        print(numbers)
