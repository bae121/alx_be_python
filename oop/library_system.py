# library_system.py

class Book:
    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author

    def __str__(self):
        return f"'{self.title}' by {self.author}"


class EBook(Book):
    def __init__(self, title: str, author: str, file_size: int):
        Book.__init__(self, title, author) 
        self.file_size = file_size

    def __str__(self):
        parent_str = Book.__str__(self) 
        return f"EBook: {parent_str} [{self.file_size}]"


class PrintBook(Book):
    def __init__(self, title: str, author: str, page_count: int):
        Book.__init__(self, title, author)
        self.page_count = page_count

    def __str__(self):
        parent_str = Book.__str__(self)
        return f"PrintBook: {parent_str} [{self.page_count} pages]"


class Library:
    def __init__(self):
        self.books = [] 

    def add_book(self, book: Book):
        self.books = self.books + [book] 

    def list_books(self):
        if not self.books:
            print("The library is empty.")
        else:
            for book in self.books:
                print(book)