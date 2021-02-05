'''
In order to actually determine the existence of a file, I had to make a search
on the internet. It turned out I had to do some import, the first statement
of the program.
'''
import os.path

def noteTaker():
    '''This is the main program'''
    
    fileName = input("Enter the name of the file: ")
    if os.path.exists(fileName):
        print("The filename you entered already exists. Do you want to:")
        print("    1. Read the file")
        print("    2. Delete the file and start over")
        print("    3. Append the file")
        print("    4. Replace a single line")
        try:
            choice = int(input("Press a number to make your choice: "))
            if choice == 1:
                fileManager(fileName, 'r')
            elif choice == 2:
                fileManager(fileName, 'w') # empty file if 0 lines entered, see fileManager below
            elif choice == 3:
                fileManager(fileName, 'a')
            elif choice == 4:
                file = open(fileName, 'r')
                listOfLines = file.readlines()
                file.close()
                print("The file has", len(listOfLines), "lines")
                try:
                    lineChoice = int(input("Enter the number of line to replace(lines start from 0): "))
                    newLineContent = input("Enter the new content for the chosen line:\n")
                    listOfLines[lineChoice] = newLineContent + "\n"
                    file = open(fileName, 'w')
                    for line in listOfLines:
                        file.write(line)
                except ValueError:
                    print("You entered an invalid value for row.")
                    print("The origram is exiting.")
                except IndexError:
                    print("The number of line you chose is not valid.")
                    print("The program is exiting.")
                finally:
                    file.close()
            else:
                print("The value you entered is not one of the choices presented.")
                print("Program is exiting.")
        except ValueError:
            print("The value you entered is not correct.")
            print("The program is exiting.")
        
    else:
        fileManager(fileName, 'w')


'''
The function below helps makes the main function above shorter (maybe?).
It provides some extra functionality compared to just using the
open() command.
'''
def fileManager(fileName, mode):
    if mode == 'w':
        file = open(fileName, mode)
        try:
            numberOfLines = int(input("How many lines of text do you want to enter? "))
            print("Enter", numberOfLines, "of text:")
            for i in range(numberOfLines):
                line = input()
                file.write(line + "\n")
        except ValueError:
            print("Incorrect value for number of rows")
            print("Exiting program")
        file.close()
    elif mode == 'r':
        file = open(fileName, mode)
        for line in file:
            print(line, end='')
        file.close()
    elif mode == 'a':
        file = open(fileName, 'a')
        numberOfLines = int(input("How many lines of text do you want to add to the existing file? "))
        print("Enter", numberOfLines, "of text:")
        for i in range(numberOfLines):
            line = input()
            file.write(line + "\n")
        file.close()

    
        
noteTaker()
    
