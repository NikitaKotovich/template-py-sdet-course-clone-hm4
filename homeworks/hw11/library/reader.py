class Reader:

    def __init__(self, name):
        self.name = name

    def reserve_book(self, book):
        return book.reserve(self.name)

    def cancel_reserve(self, book):
        return book.cancel_reserve(self.name)

    def get_book(self, book):
        return book.get_book(self.name)

    def return_book(self, book):
        return book.return_book(self.name)
