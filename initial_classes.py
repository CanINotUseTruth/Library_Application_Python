### 16 / 01 / 2021
### Toby Rutherford
### Library Application - This is the main class file for Library App

class Book():

    def __init__(self, title, author, genre, publisher, published_year):
        """ Initializes the attributes needed within the Book class """

        self.title = title
        self.author = author
        self.genre = genre
        self.publisher = publisher
        self.published_year = published_year

    def build_book(self):
        """ Create a dictionary of book information """

        book = {'title' : self.title.title(), 'author' : self.author.title(), 'genre' : self.genre.title(), 'publisher' : self.publisher.title(), 'published_year' : self.published_year}
        return book

class Users():

    def __init__(self, username, password):
        """ Initializes the attributes need within the User class """

        self.username = username
        self.password = password

    def build_user(self):
        """ Create a dictionary for user info """

        user = {'username' : self.username, 'password' : self.password}
        return user