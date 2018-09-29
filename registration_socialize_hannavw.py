#Welcomes the new user and ask to register.
print("Welcome to Socialize! Please register to be a part of this community.")

#Ask for first name and clean this name.
first_name = input("What's your first name? ")
first_name = str(first_name.lower().strip())
print("Hi, " + first_name.capitalize() + ". Please complete your profile to get sociable with Socialize.")

#Ask for infix and clean this name.
ask_if_infix = input("Do you have an infix (such as 'van' or 'de' before your last name)? yes/no ")
aks_if_infix = str(ask_if_infix.lower().strip())

if ask_if_infix == "yes":
    infix = input("Please insert you're infix: ")
else:
    infix = ""
	
#Ask for last name and compare it to my last name and index
last_name = input("What's your last name? ")
last_name = str(last_name.lower().strip())
my_last_name = "Woerden"
my_last_name = str(my_last_name.lower().strip())
my_infix = "van"
my_infix = my_infix.lower().strip()

if (infix and last_name) == (my_infix and my_last_name):
    print("We have the same last name " + (first_name.capitalize()) + " " + infix + " " + (last_name.capitalize()) + "! We're probably family:)")
elif (infix == ""):
     print("Beautiful name, " + (first_name.capitalize()) + " " + (last_name.capitalize()) + "! We're happy to welcome you on board.")
else:
    print("Beautiful name, " + (first_name.capitalize()) + " " + infix + " " + (last_name.capitalize()) + "! We're happy to welcome you on board.")
	
#calculate age by using the current date
import datetime
print("To continue, please insert your date of birth: ")

year = input("What's your birthyear? ")
if len(year) == 4:
    month = int(input("In which month were you born? Please enter the number of the month. "))
else:
    year = input("Something went wrong. Please try again: what's your birthyear? ")
    if year == 4:
        month = int(input("In which month were you born? Please enter the number of the month. "))
    else:
        month = int(input("In which month were you born? Please enter the number of the month. "))

year = int(year)
day = int(input("On what day of the month were you born? "))
date_of_birth = datetime.datetime(year,month,day)
age = (datetime.datetime.now() - date_of_birth)

convert_days = int(age.days)
import math
years = str(math.trunc(convert_days/365))
print("Great, with your " + years + " years, you can use Socialize!")

#Check if user is old enough. If so, ask to invite friends.
years = int(years)
if years >= 18:
    email = input("What's your email address? ")
else:
    print("Sorry, Socialize is only available for people of 18 years and older. Please come back if you're 18")
    exit()
	
#Follow-up questions
password = input("Please insert your password: ")
number_invite_friends = input("Socialize is even better with friends. How many friends do you want to send an invite? ")
if int(number_invite_friends) == 1:
    email_friends = input("Please insert the email address of your friend.")
    print ("Thanks! You're friends will receive an invitation to join Socialize as well.")
elif int(number_invite_friends) > 0:
    email_friends = input("Please insert the email addresses of your " + number_invite_friends + " friends, seperated by a comma. ")
    print ("Thanks! You're friends will receive an invitation to join Socialize as well.")
else:
    print("That's okay, you can always invite friends later on.")

city = input("In which city do you live? ")

#Calculate value user. A user can get a total of 10 points. The more points the higher the value. Value is based on:
#1: number of friends that are invited (more = better because more connections equals a greater reach)
#2: first letter of the city (A t/m N = 1 point O t/m Z = 3 points)
#3: age (older = richer and therefore better for advertisers)

#1
if int(number_invite_friends) == 0:
    value_1 = 0
elif int(number_invite_friends) <= 2:
    value_1 = 2
else:
    value_1 = 4

#2
first_letter = city[:1]
if first_letter == "a"or "b" or "c" or "d" or "e" or "f" or "g" or "h" or "i" or "j" or "k" or "l" or "m" or "n":
    value_2 = 1
else:
    value_2 = 3
    
#3
if years <= 25:
    value_3 = 1
elif years > 25 or years <= 40:
    value_3 = 2
else:
    value_3 = 3
    
#I don't want to print the value of the user to the user, but to get the value you can use the print function:
#value_user = str(value_1 + value_2 + value_3)
#print(first_name.capitalize() + " has a value of " + value_user + " out of 10.")

#Feedback and welcome statement
print(first_name.capitalize() + ", welcome to Socialize! We've send an email to " + email + " with your profile information, so you won't forget it.") 
print("But, just to be sure, below you find your profile information. Happy socializing!")
      
if infix == "":
    print("Name: " + (first_name.capitalize()) + " " + (last_name.capitalize()))
else:
    print("Name: " + (first_name.capitalize()) + " " + infix + " " + (last_name.capitalize()))
print("Age: " + str(years))
print("Email: " + email)
print("Password: " + password)
print("Friends you've invited: " + email_friends)
print("City: " + city)