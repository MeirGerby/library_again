class Book:

    def __init__(self, title: str, author: str, isbn: int):
        self.title: str = title
        self.author: str = author
        self.isbn: int = isbn
        self.is_available: bool = True

    def __str__(self):
        return f'------Book------\n Title: {self.title}\n Author: {self.author}'

    def set_available(self):
        self.is_available = not self.is_available