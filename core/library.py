from core.book import Book
from core.user import User
from core.file_handling import FileHandling
import  json


class Library:
    def __init__(self):
        self.books: list[Book] = []
        self.users: list[User] = []
        self.dict_books = {'books': self.books}
        self.dict_users = {'users': self.users}

    def add_book(self, book: Book) -> None:
        self.books.append(book)

    def add_user(self, user: User) -> None:
        self.users.append(user)


    @staticmethod
    def borrow_book(user: User, book: Book) -> None:
        if book.is_avaklable and user.user_id:
            user.borrowed_books.append(book.isbn)
            book.set_available()
        return None

    @staticmethod
    def return_book(user: User, book: Book) -> None:
        if book.is_avaklable and user.user_id:
            user.borrowed_books.remove(book.isbn)
            book.set_available()
        return None

    def search_book(self, title_or_author) -> None:
        for book in self.books:
            if book.title == title_or_author or book.author == title_or_author:
                print(book)

        return None

    def list_available_books(self) -> None:
        for book in self.books:
            if book.is_available:
                print(book)
        return None

    @staticmethod
    def save_users(self):
        """save the users data into a json file"""

        try:
            FileHanding.dump_data('users', self.dict_users)
        except:
            print("ERROR")

    @staticmethod
    def load_users(self):
        """load the users data from a json file"""

        try:
            data = FileHanding.load_data('users')
            return data
        except:
            print("ERROR")
        return None
    @staticmethod
    def save_books(self):
        '''save the books data into a json file'''
        try:
            FileHandling.dump_data('books', self.dict_books
        except:
            print("ERROR")
    @staticmethod
    def load_books(self):
        '''load the books data from a json file'''
        try:
            data = FileHandling.load_data('books')
            return data
        except:
            print("ERROR")
