class Book:

    def __init__(self, book_name, author, num_pages, isbn):
        self.book_name = book_name
        self.author = author
        self.num_pages = num_pages
        self.isbn = isbn
        self.reserved = None
        self.issued = None

    def reserve(self, name):
        if self.reserved is not None:
            return False
        else:
            self.reserved = name
            return True

    def cancel_reserve(self, name):
        if self.reserved == name:
            self.reserved = None
            return True
        else:
            return False

    def get_book(self, name):
        if self.issued is None:
            if self.reserved == name or self.reserved is None:
                self.issued = name
                self.reserved = None
                return True
        return False

    def return_book(self, name):
        if self.issued == name:
            self.issued = None
            return True
        else:
            return False
