from core.book import Book
from core.user import User
from core.file_handling import FileHanding
import  json


class Library:
    def __init__(self):
        self.books: list[Book] = []
        self.users: list[User] = []
        self.dict_users = {'users': self.users}
        self.dict_books = {'books': self.books}

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

    def list_available_books(self) -> None:
        for book in self.books:
            if book.is_available:
                print(book)
        return None