### 16 / 01 / 2021
### Toby Rutherford
### Library Application

# This application will allow user input for books that will save inputs within a dictionary, that can be recalled at any time.
import json # may be used later
from initial_classes import Book
from initial_classes import Users

library = []
library_file = 'library.json'

users = []
users_file = 'users.json'

# Loads known users
try:
    with open(users_file, 'r+') as file_object:
        users_load = json.load(file_object)
except FileNotFoundError:
    begin_file = ""
    with open(users_file, 'w') as file_object:
        json.dump(begin_file, file_object)
        print("\nCreating user file...")
except json.decoder.JSONDecodeError:
    print('\nNo users to load from file.')
else:
        print("\nLoading user file...")
        for user in users_load:
            users.append(user)

# Loads known books
try:
    with open(library_file, 'r+') as file_object:
        library_load = json.load(file_object)
except FileNotFoundError:
    begin_file = ""
    with open(library_file, 'w') as file_object:
        json.dump(begin_file, file_object)
        print("\nCreating library file...")
except json.decoder.JSONDecodeError:
    print('\nNo books to load from file.')
else:
        print("\nLoading library file...")
        for book in library_load:
            library.append(book)


# Too many breaks in loop

def start():
        
    # Log in to the library
    while True:
        log_input = input("\nWould you like to: \n1. Register \n2. Login \n3. Quit program \nEnter here: ")
        while True:
            #Register new user
            if log_input == '1':
                username = input("\nWhat username would you like to use? \nEnter here: ")

                while True:
                    if username in users:
                        print("That username is taken. Please try another")
                        break

                    elif username not in users:
                        password = input("\nPlease set a password, it will be case sensitive. \nEnter here: ")

                        user_input = Users(username, password)
                        user_output = user_input.build_user()
                        users.append(user_output)
                        print("\nRegistration successful! \nReturning to menu...")
                        break

                    else:
                        print("Something went wrong! Returning to menu...")
                        break

                break
            
            elif log_input == '2':
                print("\nPlease enter your login details:\n")
                username = input("Username: ")
                password = input("Password: ")

                for user in users:
                    if username == user['username'] and password == user['password']:
                        print("\nHi " + username + "! Welcome to your library.")
                        return
                    elif username == user['username'] and password != user['password']:
                        print("\nIncorrect username or password. Is this account registered?")
                        print("\nReturning to menu...")
                        break

            elif  log_input == '3':
                print("\nNothing was saved from this session.")
                print("\nClosing the program...")
                exit()
            
            else:
                print("\nInvalid input. \nReturning to menu...")
                break

            break


def main():

    while True:
        
        op_input = input("\nPlease input what operation you wish to perform.\n1. Enter a new book to your library. \n2. Find a specific book within your library. \n3. View all registered books in your library. \n4. Quit the program. \nEnter here: ")
        # Input statements for new books
        if op_input == '1':
            print("\nPlease enter book details as requested.\n")
            ibook_title = input("Enter book title: ")
            iauthor =  input("Enter the author: ")
            igenre = input("Enter the genre: ")
            ipublisher = input("Enter the publisher: ")
            ipublished_year =  input("Enter the year of publication: ")

            # Send book info to Book class for formatting and returns for input to list
            book_input = Book(ibook_title, iauthor, igenre, ipublisher, ipublished_year)
            book_output = book_input.build_book()    
            library.append(book_output)

            print("\nThank you for the info! Returning to main menu...")

        elif op_input == '2':

            while True:
                att_input = input("\nPlease input which search criteria you would like to use. \n1. Title \n2. Author \n3. Genre \n4. Publisher \n5. Year of Publication \n6. Return to previous menu \nEnter here: ")

                start_number = 0

                if att_input == '1':
                    search_title = input("\nWhich title were you looking for? ")
                    book_count = 0
                    for book in library:
                        book_count += 1
                        if search_title == book['title'].upper().lower():
                            start_number += 1
                            print("\nBook " + str(start_number) + " details:")
                            print("Title: " + book['title'] + "\nAuthor: " + book['author'] + "\nGenre: " + book['genre'] + "\nPublisher: " + book['publisher'] + "\nYear of Publication: " + book['published_year']) 
                    
                    print("\nBooks found: " + str(start_number) + "/" + str(book_count))

                elif att_input == '2':
                    search_author = input("\nWhich author were you looking for? ")
                    for book in library:
                        book_count += 1
                        if search_author == book['author'].upper().lower():
                            start_number += 1
                            print("\nBook " + str(start_number) + " details:")
                            print("Title: " + book['title'] + "\nAuthor: " + book['author'] + "\nGenre: " + book['genre'] + "\nPublisher: " + book['publisher'] + "\nYear of Publication: " + book['published_year'])
                    
                    print("\nBooks found: " + str(start_number) + "/" + str(book_count))
                        
                elif att_input == '3':
                    search_genre = input("\nWhich genre were you looking for? ")
                    for book in library:
                        book_count += 1
                        if search_genre == book['genre'].upper().lower():
                            start_number += 1
                            print("\nBook " + str(start_number) + " details:")
                            print("Title: " + book['title'] + "\nAuthor: " + book['author'] + "\nGenre: " + book['genre'] + "\nPublisher: " + book['publisher'] + "\nYear of Publication: " + book['published_year'])
                            
                    print("\nBooks found: " + str(start_number) + "/" + str(book_count))

                elif att_input == '4':
                    search_publisher = input("\nWhich publisher were you looking for? ")
                    for book in library:
                        book_count += 1
                        if search_publisher == book['publisher'].upper().lower():
                            start_number += 1
                            print("\nBook " + str(start_number) + " details:")
                            print("Title: " + book['title'] + "\nAuthor: " + book['author'] + "\nGenre: " + book['genre'] + "\nPublisher: " + book['publisher'] + "\nYear of Publication: " + book['published_year'])

                    print("\nBooks found: " + str(start_number) + "/" + str(book_count))
                            
                elif att_input == '5':
                    search_published_year = input("\nWhat year of publication were you looking for? ")
                    for book in library:
                        book_count += 1
                        if search_published_year == book['published_year']:
                            start_number += 1
                            print("\nBook " + str(start_number) + " details:")
                            print("Title: " + book['title'] + "\nAuthor: " + book['author'] + "\nGenre: " + book['genre'] + "\nPublisher: " + book['publisher'] + "\nYear of Publication: " + book['published_year'])

                    print("\nBooks found: " + str(start_number) + "/" + str(book_count))
                            
                elif att_input == '6':
                    print("Returning to main menu...")
                    break

                else:
                    print("Invalid input, try again.")
            
                sel_input = input("\nPlease input what you would like to do next. \n1. Return to main menu. \n2. Return to search selection menu. \n3.  Quit program. \nEnter here: ")
                if sel_input == '1':
                    print("Returning to main menu...")
                    break

                elif sel_input == '2':
                    print("Returning to search selection menu...")

                elif sel_input == '3':
                    print("Closing the program...")
                    return

                else:
                    print("Invalid input, returning to main menu...")
                    break

        elif op_input == '3':
            #This option allows for all books in library to be output
            start_number = 1
            print("\nList of registered books:")
            for book in library:
                print(str(start_number) + '. ' + book['title'].title())
                start_number += 1
            
            print("\nReturning to main menu...")

        elif op_input == '4':
            # How to quit the program
            "Closing program..."
            break

        else:
            #Sends you back to start if you enter unavailable input
            print("Invalid input, try again.")

start()
main()

# Saves inputs from main into memory
try:
    with open(users_file, 'w') as file_object:
        json.dump(users, file_object)
except FileNotFoundError:
    print("Could not save users in user file!")
else:
    print("Saved all this sessions users to user file.")

# Saves inputs from main into memory
try:
    with open(library_file, 'w') as file_object:
        json.dump(library, file_object)
except FileNotFoundError:
    print("Could not save books in library file!")
else:
    print("Saved all this sessions books to library file.")
