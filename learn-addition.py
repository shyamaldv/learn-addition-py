import math
import random

CORRECT_ROW = 3  #Number of correct attempts in a row

def main():
    count = 1
    while count <= CORRECT_ROW:     # Continue the while loop till correct row max attempts
        num1 = random.randint(10,99)   # Generate first random number
        num2 = random.randint(10,99)    # Generate second random number
        total = num1 + num2        # Addition of the two random numbers
        print('What is',num1,'+',num2,'?')    # Seeking user input about addition
        usr_input = int(input('Your answer:'))
        if usr_input > total:
            print('Incorrect! The expected answer is', + total)
            count = 1
        elif usr_input < total:
            print('Incorrect! The expected answer is', + total)
            count = 1
        if usr_input == total:
            print("Correct! You've gotten",str(count), "correct in a row.")
            count += 1
        if count > CORRECT_ROW:
            print("Congratulations! You mastered addition.")
            

if __name__ == '__main__':
    main()
