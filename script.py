#myscript
#Importing the os module to work with folders
import os
#Importing the CSV module to work with CSV files
import csv
#Creating a path variable to create the folder in
pathh="/home/local/TECHSTORY/"
#Opening the csv file 
with open("/home/scripts/userexport.csv") as csv_file:
        #Putting the content of the file in the reader variable
        reader = csv.reader(csv_file, delimiter=',')
        #skipping the first 2 lines
        next(reader)
        next(reader)
        #adding the reader variable to the list rows
        rows = list(reader)
        #looping over the rows variable
        for x in rows:
                #defining the characters to be removed
                characters_to_remove = "[]'"
                #Putting the x in a string
                new_string = str(x)
                #looping over the characters
                for character in characters_to_remove:
                        #removing those characters from the string
                     new_string = new_string.replace(character, "")      
                     #displaying a message with the full path of the folder to be created
                print(f"{pathh}{new_string}")
                #Checking if the folder already exists
                if not os.path.exists(f"{pathh}{new_string}"):
                        # creating the folder using the name of the user
                        os.mkdir(f"{pathh}{new_string}")
                        # setting the permissions
                        os.chmod(f"{pathh}{new_string}",0o0777)
                        # os.chown(new_string)

