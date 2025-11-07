import pytest
from homeworks.hw11.library.book import Book
from homeworks.hw11.library.reader import Reader
from homeworks.hw11.tests.conf_for_log import setup_logger

logger = setup_logger()


class TestLibraryApp:

    @pytest.fixture
    def book(self):
        return Book("The Hobbit", "J. R. R. Tolkien", 310, "0345339681")

    @pytest.fixture
    def reader(self):
        return Reader("James Bond")

    @pytest.fixture
    def reader2(self):
        return Reader("Guy Ritchie")

    def test_reserve_book_one_reader(self, book, reader):
        logger.info("Testing reserve book by one reader")
        result = reader.reserve_book(book)
        if not result:
            logger.error("Reserve book failed")
        assert result is True
        logger.info("Testing reserve book by one reader is passed")

    def test_reserve_book_two_reader_for_one_book(self, book, reader, reader2):
        logger.info("Testing reserve by two readers for one book")
        reader.reserve_book(book)
        result = reader2.reserve_book(book)
        if result:
            logger.error("Reserve book failed")
        assert result is False
        logger.info("Testing reserve by two readers for one book is passed")

    def test_reserve_book_one_reader_for_one_book_twice(self, book, reader):
        logger.info("Testing reserve one book for one reader twice")
        reader.reserve_book(book)
        result = reader.reserve_book(book)
        if result:
            logger.error("Reserve book failed")
        assert result is False
        logger.info("Testing reserve one book for one reader twice is passed")

    def test_cancel_reserve_if_user_with_res(self, book, reader):
        logger.info("Testing cancel reserve if user with reserve")
        reader.reserve_book(book)
        result = reader.cancel_reserve(book)
        if not result:
            logger.error("Cancel reserve failed")
        assert result is True
        logger.info("Testing cancel reserve if user with reserve is passed")

    def test_cancel_reserve_if_user_without_res(self, book, reader):
        logger.info("Testing cancel reserve if user without reserve")
        result = reader.cancel_reserve(book)
        if result:
            logger.error("Cancel reserve failed")
        assert result is False
        logger.info("Testing cancel reserve if user without reserve is passed")

    def test_cancel_reserve_if_oth_usr_with_res(self, book, reader, reader2):
        logger.info("Testing cancel if other user with reserve")
        reader.reserve_book(book)
        result = reader2.reserve_book(book)
        if result:
            logger.error("Cancel reserve failed")
        assert result is False
        logger.info("Testing cancel if other user with reserve is passed")

    def test_get_book_if_book_without_reserve(self, book, reader):
        logger.info("Testing get book if book without reserve")
        result = reader.get_book(book)
        if not result:
            logger.error("Get book failed")
        assert result is True
        logger.info("Testing get book if book without reserve is passed")

    def test_get_reserved_book(self, book, reader):
        logger.info("Testing get reserved book")
        reader.reserve_book(book)
        result = reader.get_book(book)
        if not result:
            logger.error("Get book failed")
        assert result is True
        logger.info("Testing get reserved book is passed")

    def test_get_reserved_book_by_another_user(self, book, reader, reader2):
        logger.info("Testing get reserved book by another user")
        reader.reserve_book(book)
        result = reader2.reserve_book(book)
        if result:
            logger.error("Get reserved book failed")
        assert result is False
        logger.info("Testing get reserved book by another user is passed")

    def test_get_book_another_user_got_book(self, book, reader, reader2):
        logger.info("Testing get book where another user got book")
        reader.reserve_book(book)
        reader.get_book(book)
        result = reader2.get_book(book)
        if result:
            logger.error("Get book failed")
        assert result is False
        logger.info("Testing get book where another user got book is passed")

    def test_return_book_after_got_book(self, book, reader):
        logger.info("Testing return book after got book")
        reader.get_book(book)
        result = reader.return_book(book)
        if not result:
            logger.error("Return book failed")
        assert result is True
        logger.info("Testing return book after got book is passed")

    def test_return_book_if_user_without_book(self, book, reader):
        logger.info("Testing return book if user without book")
        result = reader.return_book(book)
        if result:
            logger.error("Return book failed")
        assert result is False
        logger.info("Testing return book if user without book is passed")

    def test_return_book_where_anoth_us_got_book(self, book, reader, reader2):
        logger.info("Testing return book where another user got book")
        reader.get_book(book)
        result = reader2.return_book(book)
        if result:
            logger.error("Return book failed")
        assert result is False
        logger.info("Testing return book where anoth user got book is passed")
