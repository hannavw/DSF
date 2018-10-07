# Open csv file and create a list
f = open("politicians.csv")
politicians = []

# Strip the csv and create a for loop to append input to the multidimensional list
index = 0                                  
for politician in f:
    politician = politician.strip().split(",")
    name = politician[0]
    last_name = politician[1]
    birthyear = politician[2]
    party = politician[3]
    items = [name, last_name, birthyear, party]
    politicians.append(items)
    
# Print the items in the list in a full sentence and add 1 to the index number 
# for the next loop.
    
    print(str(index) + ": " + name, last_name + " was born in " + birthyear)
    print(name + " is a member of the political party " + party + ".")
    index = index + 1

# Print the amount of politicians in the database.
amount = str(len(politicians))
if amount == "1":
    print("There is " + amount + " politician in the database.")
else:
    print("There are " + amount + " politicians in the database.")

# Close the csv file and print a statement for usability.
f.close()
print("If you want, you can now edit the file or quit the program.")

# Create a while loop with 4 actions. Ask the user for input.
while True:
    print("To continue, make your choice:")
    print(" - To remove a politician: press 1")
    print(" - To add a politician: press 2")
    print(" - To save the database to the csv file: press 3")
    print(" - To quit the program: press 4")
    action = input("What do you want to do? ")
    
# Remove a politician if there are any politicians in the database.
# Otherwise, print feedback that the list is empty.
    if action == "1":
        print("You've chosen to remove a policitian from the database.")
        if amount > "0":
            index = int(input("Who do you want to remove? Please give the index number: "))
            print("You've succesfully removed " + politicians[index][0] + " from your database.")
            politicians.pop(index)
            if str(len(politicians)) == "1":
                print("There is " + str(len(politicians)) + " politician in the database.")
            else:
                print("There are " + str(len(politicians)) + " politicians in the database.")
            print("Don't forget to save your file before you close the program.")
        else:
            print("There are no politicians to remove. Please choose a different option.")

# Ask the user for input and add a politician to the multidimensional list
    elif action == "2":
        print("You've chosen to add a politician to the database.")
        new_name = input("What's the first name of the politician? ").title()
        new_last_name = input("What's the last name of the politician? ").title()
        birthyear = input("What's the birth year of " + new_name + " " + new_last_name + "? ")
        party = input("Of wich political party is " + new_name + " " + new_last_name + " a member of? ")
        new_politician = [new_name, new_last_name, birthyear, party]
        politicians.append(new_politician)
        
# Give feedback to the user.
        print(new_name + " " + new_last_name + " is now added to the database.")
        amount = str(len(politicians))
        if amount == "1":
            print("There is " + amount + " politician in the database.")
        else:
            print("There are " + amount + " politicians in the database.")
        print("Don't forget to save your file before you close the program.")

# Save the database to the original file.
    elif action == "3":
        import csv
        with open("politicians.csv", "w", newline = "") as f:
            writer = csv.writer(f)
            writer.writerows(politicians)
            print("You're database is saved to your file.")
            print("Quit the program to see the changes you've made in your file.")

# Quit the while loop.
    elif action == "4":
        print("You've chosen to quit the program.")
        break
    
# Give users an option to choose again.
    else:
        print("You've chosen a non-existing option. Please choose again.")

# Close the program. 
print("Goodbye!")
f.close()