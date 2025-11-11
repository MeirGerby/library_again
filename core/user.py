from core.book import Book


class User:
    def __init__(self,name:str,user_id:int):
        self.name = name
        self.user_id = user_id
        self.borrowed_books = []

