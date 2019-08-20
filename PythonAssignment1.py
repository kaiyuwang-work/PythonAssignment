import csv
import random

file_handle = open('/Users/kaiyuwang/Desktop/Countries.csv') #where countries.csv stored
reader = csv.DictReader(file_handle) #read the contents of the file into a dictionary
countries = list(reader) #convert the reader into a list 

file_handle.close() #close the file since we're done with it

randomcountry = random.choice(countries)
guess ="" #instantiate an empty string
attempts = 0 #set the number of attempts = 0
unmatched = False
print(randomcountry)

randomcountryname = randomcountry['\ufeffcountry']


while guess != randomcountryname and attempts <10:
    guess = input("What country am I?").casefold()
    attempts += 1
    if guess == randomcountryname.casefold():
        print("Well done! You have successfully indentified the country")
        break
    if attempts >=10:
        print("You are fresh out of guesses")
        break
        
        
    for country in countries:

        if guess.casefold() == country['\ufeffcountry'].casefold():
          if randomcountry['lat'] >country['lat']:
             print('I am located north of ' +guess)
          else:
             print('I am located south of '+guess)


          if randomcountry['long'] >country['long']:
            print('I am located east of ' +guess)
          else:
            print('I am located west of '+guess)
