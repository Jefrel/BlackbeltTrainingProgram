"""
Jefrel Jan Espenida
Task 2
"""
import random
rand = random.randint(1,10)
while True:
    number = int(input("Guess the number: "));
    if number == rand:
        print("Correct!");   
        break
    elif number!= rand:
        print("Wrong, try again!"); 
    

