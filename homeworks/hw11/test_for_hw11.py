import unittest
from homeworks.hw11.bank_deposit.bank import Bank
from homeworks.hw11.bank_deposit.currency import CurrencyConverter
from homeworks.hw11.library.book import Book
from homeworks.hw11.library.reader import Reader


class TestBank(unittest.TestCase):

    def test_register_client(self):
        bank = Bank()
        self.assertTrue(bank.register_client("001", "James Bond"))
        self.assertTrue(bank.register_client("002", "Guy Ritchie"))

    def test_register_client_2(self):
        bank = Bank()
        self.assertTrue(bank.register_client("003", "J. R. R. Tolkien"))
        self.assertFalse(bank.register_client("003", "J. R. R. Tolkien"))

    def test_open_deposit_account(self):
        bank = Bank()
        bank.register_client("001", "James Bond")
        self.assertTrue(bank.open_deposit_account("001", 1000, 1))

    def test_open_deposit_account_without_register_client(self):
        bank = Bank()
        self.assertFalse(bank.open_deposit_account("004", 10000, 2))

    def test_calc_interest_rate_if_unregister_user(self):
        bank = Bank()
        self.assertFalse(bank.calc_interest_rate("005"))

    def test_calc_interest_rate(self):
        bank = Bank()
        bank.register_client("001", "James Bond")
        bank.open_deposit_account("001", 1000, 1)
        self.assertEqual(bank.calc_interest_rate("001"), 1104.71)

    def test_calc_interest_rate_if_user_without_deposit(self):
        bank = Bank()
        bank.register_client("002", "Guy Ritchie")
        self.assertFalse(bank.calc_interest_rate("002"))

    def test_close_deposit_if_user_with_deposit(self):
        bank = Bank()
        bank.register_client("001", "James Bond")
        bank.open_deposit_account("001", 1000, 1)
        self.assertEqual(bank.close_deposit("001"), 1104.71)

    def test_close_deposit_if_user_without_deposit(self):
        bank = Bank()
        bank.register_client("002", "Guy Ritchie")
        self.assertFalse(bank.close_deposit("002"))

    def test_close_deposit_if_unregister_user(self):
        bank = Bank()
        self.assertFalse(bank.close_deposit("006"))

    def test_convert_currency(self):
        currency = CurrencyConverter()
        self.assertEqual(currency.convert("USD", 1000, "BYN"), 3267.7, "BYN")
        self.assertEqual(currency.convert("EUR", 1000, "BYN"), 3399, "BYN")
        self.assertEqual(currency.convert("BYN", 1000, "USD"), 306.03, "USD")
        self.assertEqual(currency.convert("BYN", 1000, "EUR"), 294.2, "EUR")
        self.assertEqual(currency.convert("USD", 1000, "EUR"), 961.37, "EUR")
        self.assertEqual(currency.convert("EUR", 1000, "USD"), 1040.18, "USD")

    def test_convert_incorrect_to_currency(self):
        currency = CurrencyConverter()
        with self.assertRaises(ValueError):
            currency.convert("USD", 1000, "BTC")
            currency.convert("BYN", 1000, "UsD")
            currency.convert("EUR", 1000, "USA")

    def test_convert_incorrect_from_currency(self):
        currency = CurrencyConverter()
        with self.assertRaises(ValueError):
            currency.convert("ETH", 1000, "USD")
            currency.convert("S", 1000, "BYN")
            currency.convert("bin", 1000, "EUR")


class TestBook(unittest.TestCase):

    def test_reserve_book_one_reader(self):
        book = Book("The Hobbit", "J. R. R. Tolkien", 310, "0345339681")
        reader = Reader("James Bond")
        self.assertTrue(reader.reserve_book(book))

    def test_reserve_book_two_reader_for_one_book(self):
        book = Book("The Hobbit", "J. R. R. Tolkien", 310, "0345339681")
        reader = Reader("James Bond")
        self.assertTrue(reader.reserve_book(book))
        reader2 = Reader("Guy Ritchie")
        self.assertFalse(reader2.reserve_book(book))

    def test_reserve_book_one_reader_for_one_book_twice(self):
        book = Book("The Hobbit", "J. R. R. Tolkien", 310, "0345339681")
        reader = Reader("James Bond")
        self.assertTrue(reader.reserve_book(book))
        self.assertFalse(reader.reserve_book(book))

    def test_cancel_reserve_if_user_with_reserve(self):
        book = Book("The Hobbit", "J. R. R. Tolkien", 310, "0345339681")
        reader = Reader("James Bond")
        self.assertTrue(reader.reserve_book(book))
        self.assertTrue(reader.cancel_reserve(book))

    def test_cancel_reserve_if_user_without_reserve(self):
        book = Book("The Hobbit", "J. R. R. Tolkien", 310, "0345339681")
        reader = Reader("James Bond")
        self.assertFalse(reader.cancel_reserve(book))

    def test_cancel_reserve_if_other_user_with_reserve(self):
        book = Book("The Hobbit", "J. R. R. Tolkien", 310, "0345339681")
        reader1 = Reader("James Bond")
        self.assertTrue(reader1.reserve_book(book))
        reader2 = Reader("Guy Ritchie")
        self.assertFalse(reader2.reserve_book(book))

    def test_get_book_if_book_without_reserve(self):
        book = Book("The Hobbit", "J. R. R. Tolkien", 310, "0345339681")
        reader = Reader("James Bond")
        self.assertTrue(reader.get_book(book))

    def test_get_reserved_book(self):
        book = Book("The Hobbit", "J. R. R. Tolkien", 310, "0345339681")
        reader = Reader("James Bond")
        self.assertTrue(reader.reserve_book(book))
        self.assertTrue(reader.get_book(book))

    def test_get_reserved_book_by_another_user(self):
        book = Book("The Hobbit", "J. R. R. Tolkien", 310, "0345339681")
        reader1 = Reader("James Bond")
        self.assertTrue(reader1.reserve_book(book))
        reader2 = Reader("Guy Ritchie")
        self.assertFalse(reader2.reserve_book(book))
        self.assertFalse(reader2.get_book(book))

    def test_get_book_where_another_user_got_book(self):
        book = Book("The Hobbit", "J. R. R. Tolkien", 310, "0345339681")
        reader1 = Reader("James Bond")
        self.assertTrue(reader1.reserve_book(book))
        self.assertTrue(reader1.get_book(book))
        reader2 = Reader("Guy Ritchie")
        self.assertFalse(reader2.get_book(book))

    def test_return_book_after_got_book(self):
        book = Book("The Hobbit", "J. R. R. Tolkien", 310, "0345339681")
        reader = Reader("James Bond")
        self.assertTrue(reader.get_book(book))
        self.assertTrue(reader.return_book(book))

    def test_return_book_if_user_without_book(self):
        book = Book("The Hobbit", "J. R. R. Tolkien", 310, "0345339681")
        reader = Reader("James Bond")
        self.assertFalse(reader.return_book(book))

    def test_another_user_return_book(self):
        book = Book("The Hobbit", "J. R. R. Tolkien", 310, "0345339681")
        reader1 = Reader("James Bond")
        self.assertTrue(reader1.get_book(book))
        reader2 = Reader("Guy Ritchie")
        self.assertFalse(reader2.return_book(book))
