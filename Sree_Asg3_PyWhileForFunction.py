#------------ Number Guessing Game-------------

import random
secret_number=random.randint(1,10)
print("----Number Guessing Game---")
n=0
while n<3:
    number= int(input("Guess the number (between 1 and 10 :)"))
    if number >= 11 or number <=-1 :
        print("The number is out of Range.")
        continue
    if number > secret_number :
        print("Too High! Try again")
    if number < secret_number :
       print("Too Low! Try again")
    if number == secret_number :
            print("Congratulations! You guessed the correct number")
            break
    n +=1
else :
        print("Better luck next time")
        print("The Secret nukber is" ,secret_number)

#------------ Multiplication Table Generator-------

print("--------Multiplication Table Generator-------")
n=int(input("Enter the number for the multiplication table:"))
for i in range(1,11):
    num=i*n
    print(f'{n}  X  {i} = {num}')

#---------------- BMI Calculator-------------

print("--------BMI Calculator-------")
w=float(input("Enter your Weight in KG : "))
h=float(input("Enter your Height in METERS : "))
def bmi(we,he):
    return(we/he **2)
cal=bmi(w,h)
print("Your BMI is : ", round(cal,2))   
    
