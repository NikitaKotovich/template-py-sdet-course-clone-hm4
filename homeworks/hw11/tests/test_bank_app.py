import time
import pytest
from homeworks.hw11.bank_deposit.bank import Bank
from homeworks.hw11.bank_deposit.currency import CurrencyConverter
from homeworks.hw11.tests.conf_for_log import setup_logger

logger = setup_logger()


@pytest.mark.parametrize("client_id,name,expected", [
    ("001", "James Bond", True),
    ("002", "Guy Ritchie", True)
])
def test_register_client(client_id, name, expected):
    bank = Bank()
    logger.info(f"Testing client registration: {name} (ID: {client_id})")
    result = bank.register_client(client_id, name)
    if result != expected:
        logger.error(f"Client {client_id} registration failed: {result}")
    assert result == expected
    logger.info(f"Test completed at: {time.strftime('%Y-%m-%d %H:%M:%S')}")


@pytest.mark.parametrize("client_id,name,expected", [
    ("003", "J. R. R. Tolkien", False),
])
def test_register_client_2(client_id, name, expected):
    bank = Bank()
    logger.info(f"Testing duplicate client registration: "
                f"{name} (ID: {client_id})")
    bank.register_client(client_id, name)
    result = bank.register_client(client_id, name)
    if result != expected:
        logger.error(f"Client {client_id} registration failed: {result}")
    assert result == expected
    logger.info(f"Test completed at: {time.strftime('%Y-%m-%d %H:%M:%S')}")


@pytest.mark.parametrize("client_id,name,start_balance,expected", [
    ("001", "James Bond", 1000, True),
])
def test_open_deposit_account(client_id, name, start_balance, expected):
    bank = Bank()
    bank.register_client(client_id, name)
    logger.info(f"Testing deposit account opening: "
                f"{name} (ID: {client_id}, Balance: {start_balance})")
    result = bank.open_deposit_account(client_id, name, start_balance)
    if result != expected:
        logger.error(f"Client {client_id} open deposit failed: {result}")
    assert result == expected
    logger.info(f"Test completed at: {time.strftime('%Y-%m-%d %H:%M:%S')}")


@pytest.mark.parametrize("client_id,name,start_balance,expected", [
    ("004", "James Bond", 10000, False),
])
def test_open_deposit_account_without_register_client(client_id, name,
                                                      start_balance, expected):
    bank = Bank()
    logger.info(f"Testing deposit account without registration: "
                f"{name} (ID: {client_id}, Balance: {start_balance})")
    result = bank.open_deposit_account(client_id, name, start_balance)
    if result != expected:
        logger.error(f"Client {client_id} open deposit failed: {result}")
    assert result == expected
    logger.info(f"Test completed at: {time.strftime('%Y-%m-%d %H:%M:%S')}")


@pytest.mark.parametrize("client_id,expected", [
    ("001", False),
])
def test_calc_interest_rate_if_unregister_user(client_id, expected):
    bank = Bank()
    logger.info(f"Testing interest calculation for unregistered user (ID: "
                f"{client_id})")
    result = bank.calc_interest_rate(client_id)
    if result != expected:
        logger.error(f"Client {client_id} calc interest rate failed: {result}")
    assert result == expected
    logger.info(f"Test completed at: {time.strftime('%Y-%m-%d %H:%M:%S')}")


@pytest.mark.parametrize("client_id,name,start_balance,years,expected", [
    ("001", "James Bond", 1000, 1, 1104.71),
])
def test_calc_interest_rate(client_id, name, start_balance, years, expected):
    bank = Bank()
    bank.register_client(client_id, name)
    bank.open_deposit_account(client_id, start_balance, years)
    logger.info(f"Testing interest calculation: "
                f"{name} (ID: {client_id}, Balance: "
                f"{start_balance}, Years: {years})")
    result = bank.calc_interest_rate(client_id)
    if result != expected:
        logger.error(f"Client {client_id} calc interest rate failed: {result}")
    assert result == expected
    logger.info(f"Test completed at: {time.strftime('%Y-%m-%d %H:%M:%S')}")


@pytest.mark.parametrize("client_id,name,expected", [
    ("001", "James Bond", False),
])
def test_calc_interest_rate_if_user_without_deposit(client_id, name, expected):
    bank = Bank()
    bank.register_client(client_id, name)
    logger.info(f"Testing interest calculation without deposit: "
                f"{name} (ID: {client_id})")
    result = bank.calc_interest_rate(client_id)
    if result != expected:
        logger.error(f"Client {client_id} calc interest rate failed: {result}")
    assert result == expected
    logger.info(f"Test completed at: {time.strftime('%Y-%m-%d %H:%M:%S')}")


@pytest.mark.parametrize("client_id,name,start_balance,years,expected", [
    ("001", "James Bond", 1000, 1, 1104.71),
])
def test_close_deposit_if_user_with_deposit(client_id, name,
                                            start_balance, years, expected):
    bank = Bank()
    bank.register_client(client_id, name)
    bank.open_deposit_account(client_id, start_balance, years)
    logger.info(f"Testing deposit closure with deposit: "
                f"{name} (ID: {client_id}, Balance: "
                f"{start_balance}, Years: {years})")
    result = bank.close_deposit(client_id)
    if result != expected:
        logger.error(f"Client {client_id} close deposit failed: "
                     f"{result}")
    assert result == expected
    logger.info(f"Test completed at: {time.strftime('%Y-%m-%d %H:%M:%S')}")


@pytest.mark.parametrize("client_id,name,expected", [
    ("001", "James Bond", False),
])
def test_close_deposit_if_user_without_deposit(client_id, name, expected):
    bank = Bank()
    bank.register_client(client_id, name)
    logger.info(f"Testing deposit closure without deposit: "
                f"{name} (ID: {client_id})")
    result = bank.close_deposit(client_id)
    if result != expected:
        logger.error(f"Client {client_id} close deposit failed: {result}")
    assert result == expected
    logger.info(f"Test completed at: {time.strftime('%Y-%m-%d %H:%M:%S')}")


@pytest.mark.parametrize("client_id,expected", [
    ("001", False),
])
def test_close_deposit_if_unregister_user(client_id, expected):
    bank = Bank()
    logger.info(f"Testing deposit closure for unregistered user (ID: "
                f"{client_id})")
    result = bank.close_deposit(client_id)
    if result != expected:
        logger.error(f"Client {client_id} close deposit failed: {result}")
    assert result == expected
    logger.info(f"Test completed at: {time.strftime('%Y-%m-%d %H:%M:%S')}")


@pytest.mark.parametrize("from_curr,to_curr,amount,expected", [
    ("USD", "BYN", 1000, 3267.7),
    ("EUR", "BYN", 1000, 3399),
    ("BYN", "USD", 1000, 306.03),
    ("BYN", "EUR", 1000, 294.2),
    ("USD", "EUR", 1000, 961.37),
    ("EUR", "USD", 1000, 1040.18),
])
def test_convert_currency(from_curr, to_curr, amount, expected):
    currency = CurrencyConverter()
    logger.info(f"Testing currency conversion: "
                f"{amount} {from_curr} to {to_curr}")
    result = currency.convert(from_curr, amount, to_curr)
    if result != expected:
        logger.error(f"Client {amount} close convert currency failed: "
                     f"{result}")
    assert result == expected
    logger.info(f"Test completed at: {time.strftime('%Y-%m-%d %H:%M:%S')}")


@pytest.mark.parametrize("from_curr,to_curr,amount,expected", [
    ("BYN", "EEUR", 1000, "Unsupported currency: {curr}"),
])
def test_convert_incorrect_to_currency(from_curr, to_curr, amount, expected):
    bank = Bank()
    logger.info(f"Testing incorrect to currency: "
                f"{amount} {from_curr} to {to_curr}")
    with pytest.raises(ValueError) as info:
        assert bank.exchange_currency(from_curr, amount, to_curr)
    assert str(info.value) == expected.format(curr=to_curr)
    logger.info(f"Test completed at: {time.strftime('%Y-%m-%d %H:%M:%S')}")


@pytest.mark.parametrize("from_curr,to_curr,amount,expected", [
    ("EEUR", "BYN", 1000, "Unsupported currency: {curr}"),
])
def test_convert_incorrect_from_currency(from_curr, to_curr, amount, expected):
    bank = Bank()
    logger.info(f"Testing incorrect from currency: "
                f"{amount} {from_curr} to {to_curr}")
    with pytest.raises(ValueError) as info:
        assert bank.exchange_currency(from_curr, amount, to_curr)
    assert str(info.value) == expected.format(curr=from_curr)
    logger.info(f"Test completed at: {time.strftime('%Y-%m-%d %H:%M:%S')}")
