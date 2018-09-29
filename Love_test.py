#Fill in the names for the love test
print("Are you in love? With this test you can check if you are a match or not.")
print("Please insert your name and the name of the person you are in love with.")
your_name = input("What's your name? ")
name_lover = input("What's the name of the person you are in love with? ")
your_name = your_name.lower().strip()
name_lover = name_lover.lower().strip()

print("Let's check if you and " + name_lover + " are a good match. You are a: ")

#Check if you need to stay together or not
#if your_name == name_partner:
#	print("Mmm, you like eachother, but you won't get married. Having the same name is to confusing.")
#elif your_name > name_partner:
#	print("This is what I'm talking about! You will stay together forever because your name has more characters.")
#elif your_name < name_partner:
#	print("Break up immediatly! Your name has less characters. This means that you will have a horrible time if you stay together")
	
#Calculating number of characters  
characters_your_name = int(len(your_name))
characters_name_lover = int(len(name_lover))

# calculating the difference in characters
difference = abs(characters_your_name - characters_name_lover)

# calculating the percentages. Low difference is better match
if difference == 0:
	print("100% match")
elif difference == 1:
	print("80% match")
elif difference == 2:
	print("60% match")
elif difference == 3:
	print("40% match")
elif difference == 4:
	print("20% match")
else:
	print ("0% match")