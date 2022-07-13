# roll a "die" some number of times.
# roll - run it once and go into a loop
# roll 1 - produce a number 1-6 random and print it
# roll 2 - produce two numbers 1-6 and print them
# roll 3 - produce three numbers and print them.
#
import random


roll_num = int(input("how many dice do you want to roll? "))
roll_list = []
for i in range(roll_num):
    roll_list.append(random.randint(1, 6))
    print(roll_list[i])
