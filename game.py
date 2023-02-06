import numpy as np
number = np.random.randint(1,101)
count = 0
while True:
    count += 1
    predict_number = int(input("Guess the number 1 to 100 "))
    if predict_number > number:
        print("The number must be less!")
    elif predict_number < number:
        print("The number must bee more!")
    else:
        print(f"You guess the number! The number = {number} for {count} attempts")
        break