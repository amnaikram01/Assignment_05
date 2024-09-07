#numerical no 01 : Checking if number is even or odd
#solution
def check_even_odd(num):
    if num % 2 == 0:
        print(f"{num}  is Even.")
    else:
        print(f"{num} is Odd.")

number = int(input ("Enter any number:  "))
check_even_odd(number)

print("______________________\n")


#Numerical no 02 : checking Postive,negative and zero integer:
#solution
def sign_check(num):
    if num > 0:
        print(f"{num} is Positive")
    elif num < 0:
        print(f"{num} is negative")
    else:
        print(f"{num} is neutral.")

number = int(input("Enter any  number: "))
sign_check(number)

print("______________________\n")


#Numerical no 03 : Checking number is divsible by 2 or 3 or both.
def divisible(number):
    if number % 2 == 0 and number % 3 == 0:
        print(f"{number} is divisible by both 2 and 3.")
    elif number % 2 == 0:
        print(f"{number} is divisible by 2.")
    elif number % 3 == 0:
        print(f"{number} is divisible by 3.")
    else:
        print(f"{number} is not divisible by either 2 or 3.")

number = int(input("Enter number to check its divisiblity:  "))
divisible(number)

print("______________________\n")


#numerical no 04 : taking user age and checking their eligiblity for casting vote 
def vote_age(number):
    if age == 18 or age > 18 :
        nationality = str(input("Are you citizen of Pakistan? "))
        if nationality.lower() == "yes":
            print("You are eligible for casting vote.")
        else:
            print("Please obtsin a valid ID to vote.")
    else:
        print("You are not eligible for casting vote.")
    
age = int(input("Enter your age: "))
vote_age(age)

print("______________________\n")


#numerical no 05 : Checking the life stage of user from their age

def life_stage(age):
    if age <= 12 :
        print("You are a child.")
    elif age > 13 and age <19:
        print("You are a teenager.")
    elif  age > 20 and age < 59 :
        print("You are an adult.")
    elif age > 60 and age < 150:
        print("You are a senior citizen.")
    else:
        print("Invalid age.")
    
age = int(input("Enter your age: "))
life_stage(age)

print("______________________\n")

#numerical no 06 :checking number of days of month
def month_days(number):
    if number in [4, 6, 9, 11]:
        print(f"{number}th month has 30 days.")
    elif number == 2:
        print(f"{number}nd month has 28 days.")
    else:
        print(f"{number}th month has 31 days.")

number = int(input("Enter the number of month: "))
month_days(number)

print("______________________\n")

#numerical no 07 : Check if year is leap year or not 
                    # Solution
def leap_year(year):
    if year % 4 == 0:
       print(f"{year} is a leap year.")
    else:
        print(f"{year} is not a leap year.")

year = int(input("Enter the Year in number : "))
leap_year(year)