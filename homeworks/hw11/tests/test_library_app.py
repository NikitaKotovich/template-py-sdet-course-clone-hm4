import pytest
from homeworks.hw11.library.book import Book
from homeworks.hw11.library.reader import Reader
from homeworks.hw11.tests.conf_for_log import setup_logger

logger = setup_logger()


@pytest.mark.parametrize(
    "book_data,reader_name,expected", [
        ({"name": "The Hobbit", "author": "J. R. R. Tolkien",
          "pages": 310, "isbn": "0345339681"},
         "James Bond", True),
    ])
def test_reserve_book_one_reader(book_data, reader_name, expected):
    logger.info("Testing reserve book by one reader")
    book = Book(book_data["name"], book_data["author"],
                book_data["pages"], book_data["isbn"])
    reader = Reader(reader_name)
    result = reader.reserve_book(book)
    if result != expected:
        logger.error("Reserve book failed")
    assert result == expected
    logger.info("Testing reserve book by one reader is passed")


@pytest.mark.parametrize(
    "book_data,reader_names,expected", [
        ({"name": "The Hobbit", "author": "J. R. R. Tolkien",
          "pages": 310, "isbn": "0345339681"},
         ("James Bond", "Guy Ritchie"), False),
    ])
def test_reserve_book_two_reader_for_one_book(book_data,
                                              reader_names, expected):
    logger.info("Testing reserve by two readers for one book")
    book = Book(book_data["name"], book_data["author"],
                book_data["pages"], book_data["isbn"])
    reader1 = Reader(reader_names[0])
    reader1.reserve_book(book)
    reader2 = Reader(reader_names[1])
    result = reader2.reserve_book(book)
    if result != expected:
        logger.error("Reserve book failed")
    assert result == expected
    logger.info("Testing reserve by two readers for one book is passed")


@pytest.mark.parametrize(
    "book_data,reader_name,expected", [
        ({"name": "The Hobbit", "author": "J. R. R. Tolkien",
          "pages": 310, "isbn": "0345339681"},
         "James Bond", False),
    ])
def test_reserve_book_one_reader_for_one_book_twice(book_data, reader_name,
                                                    expected):
    logger.info("Testing reserve one book for one reader twice")
    book = Book(book_data["name"], book_data["author"],
                book_data["pages"], book_data["isbn"])
    reader = Reader(reader_name)
    reader.reserve_book(book)
    result = reader.reserve_book(book)
    if result != expected:
        logger.error("Reserve book failed")
    assert result == expected
    logger.info("Testing reserve one book for one reader twice is passed")


@pytest.mark.parametrize(
    "book_data,reader_name,expected", [
        ({"name": "The Hobbit", "author": "J. R. R. Tolkien",
          "pages": 310, "isbn": "0345339681"},
         "James Bond", True),
    ])
def test_cancel_reserve_if_user_with_reserve(book_data, reader_name, expected):
    logger.info("Testing cancel reserve if user with reserve")
    book = Book(book_data["name"], book_data["author"],
                book_data["pages"], book_data["isbn"])
    reader = Reader(reader_name)
    reader.reserve_book(book)
    result = reader.cancel_reserve(book)
    if result != expected:
        logger.error("Cancel reserve failed")
    assert result == expected
    logger.info("Testing cancel reserve if user with reserve is passed")


@pytest.mark.parametrize(
    "book_data,reader_name,expected", [
        ({"name": "The Hobbit", "author": "J. R. R. Tolkien",
          "pages": 310, "isbn": "0345339681"},
         "James Bond", False),
    ])
def test_cancel_reserve_if_user_without_reserve(book_data, reader_name,
                                                expected):
    logger.info("Testing cancel reserve if user without reserve")
    book = Book(book_data["name"], book_data["author"],
                book_data["pages"], book_data["isbn"])
    reader = Reader(reader_name)
    result = reader.cancel_reserve(book)
    if result != expected:
        logger.error("Cancel reserve failed")
    assert result == expected
    logger.info("Testing cancel reserve if user without reserve is passed")


@pytest.mark.parametrize(
    "book_data,reader_names,expected", [
        ({"name": "The Hobbit", "author": "J. R. R. Tolkien",
          "pages": 310, "isbn": "0345339681"},
         ("James Bond", "Guy Ritchie"), False),
    ])
def test_cancel_reserve_if_other_user_with_reserve(book_data, reader_names,
                                                   expected):
    logger.info("Testing cancel if other user with reserve")
    book = Book(book_data["name"], book_data["author"],
                book_data["pages"], book_data["isbn"])
    reader1 = Reader(reader_names[0])
    reader1.reserve_book(book)
    reader2 = Reader(reader_names[1])
    result = reader2.reserve_book(book)
    if result != expected:
        logger.error("Cancel reserve failed")
    assert result == expected
    logger.info("Testing cancel if other user with reserve is passed")


@pytest.mark.parametrize(
    "book_data,reader_name,expected", [
        ({"name": "The Hobbit", "author": "J. R. R. Tolkien",
          "pages": 310, "isbn": "0345339681"},
         "James Bond", True),
    ])
def test_get_book_if_book_without_reserve(book_data, reader_name, expected):
    logger.info("Testing get book if book without reserve")
    book = Book(book_data["name"], book_data["author"],
                book_data["pages"], book_data["isbn"])
    reader = Reader(reader_name)
    result = reader.get_book(book)
    if result != expected:
        logger.error("Get book failed")
    assert result == expected
    logger.info("Testing get book if book without reserve is passed")


@pytest.mark.parametrize(
    "book_data,reader_name,expected", [
        ({"name": "The Hobbit", "author": "J. R. R. Tolkien",
          "pages": 310, "isbn": "0345339681"},
         "James Bond", True),
    ])
def test_get_reserved_book(book_data, reader_name, expected):
    logger.info("Testing get reserved book")
    book = Book(book_data["name"], book_data["author"],
                book_data["pages"], book_data["isbn"])
    reader = Reader(reader_name)
    reader.reserve_book(book)
    result = reader.get_book(book)
    if result != expected:
        logger.error("Get book failed")
    assert result == expected
    logger.info("Testing get reserved book is passed")


@pytest.mark.parametrize(
    "book_data,reader_names,expected", [
        ({"name": "The Hobbit", "author": "J. R. R. Tolkien",
          "pages": 310, "isbn": "0345339681"},
         ("James Bond", "Guy Ritchie"), False),
    ])
def test_get_reserved_book_by_another_user(book_data, reader_names, expected):
    logger.info("Testing get reserved book by another user")
    book = Book(book_data["name"], book_data["author"],
                book_data["pages"], book_data["isbn"])
    reader1 = Reader(reader_names[0])
    reader1.reserve_book(book)
    reader2 = Reader(reader_names[1])
    result = reader2.reserve_book(book)
    if result != expected:
        logger.error("Get reserved book failed")
    logger.info("Testing get reserved book by another user is passed")


@pytest.mark.parametrize(
    "book_data,reader_names,expected", [
        ({"name": "The Hobbit", "author": "J. R. R. Tolkien",
          "pages": 310, "isbn": "0345339681"},
         ("James Bond", "Guy Ritchie"), False),
    ])
def test_get_book_where_another_user_got_book(book_data, reader_names,
                                              expected):
    logger.info("Testing get book where another user got book")
    book = Book(book_data["name"], book_data["author"],
                book_data["pages"], book_data["isbn"])
    reader1 = Reader(reader_names[0])
    reader1.reserve_book(book)
    reader1.get_book(book)
    reader2 = Reader(reader_names[1])
    result = reader2.get_book(book)
    if result != expected:
        logger.error("Get book failed")
    assert result == expected
    logger.info("Testing get book where another user got book is passed")


@pytest.mark.parametrize(
    "book_data,reader_name,expected", [
        ({"name": "The Hobbit", "author": "J. R. R. Tolkien",
          "pages": 310, "isbn": "0345339681"},
         "James Bond", True),
    ])
def test_return_book_after_got_book(book_data, reader_name, expected):
    logger.info("Testing return book after got book")
    book = Book(book_data["name"], book_data["author"],
                book_data["pages"], book_data["isbn"])
    reader = Reader(reader_name)
    reader.get_book(book)
    result = reader.return_book(book)
    if result != expected:
        logger.error("Return book failed")
    assert result == expected
    logger.info("Testing return book after got book is passed")


@pytest.mark.parametrize(
    "book_data,reader_name,expected", [
        ({"name": "The Hobbit", "author": "J. R. R. Tolkien",
          "pages": 310, "isbn": "0345339681"},
         "James Bond", False),
    ])
def test_return_book_if_user_without_book(book_data, reader_name, expected):
    logger.info("Testing return book if user without book")
    book = Book(book_data["name"], book_data["author"],
                book_data["pages"], book_data["isbn"])
    reader = Reader(reader_name)
    result = reader.return_book(book)
    if result != expected:
        logger.error("Return book failed")
    assert result == expected
    logger.info("Testing return book if user without book is passed")


@pytest.mark.parametrize(
    "book_data,reader_names,expected", [
        ({"name": "The Hobbit", "author": "J. R. R. Tolkien",
          "pages": 310, "isbn": "0345339681"},
         ("James Bond", "Guy Ritchie"), False),
    ])
def test_return_book_where_another_user_got_book(book_data, reader_names,
                                                 expected):
    logger.info("Testing return book where another user got book")
    book = Book(book_data["name"], book_data["author"],
                book_data["pages"], book_data["isbn"])
    reader1 = Reader(reader_names[0])
    reader1.get_book(book)
    reader2 = Reader(reader_names[1])
    result = reader2.return_book(book)
    if result != expected:
        logger.error("Return book failed")
    assert result == expected
    logger.info("Testing return book where another user got book is passed")
