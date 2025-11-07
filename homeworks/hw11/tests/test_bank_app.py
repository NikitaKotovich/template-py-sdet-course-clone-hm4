import time
import pytest
from homeworks.hw11.bank_deposit.bank import Bank
from homeworks.hw11.bank_deposit.currency import CurrencyConverter
from homeworks.hw11.tests.conf_for_log import setup_logger

logger = setup_logger()


class TestBankApp:

    @pytest.fixture
    def bank(self):
        return Bank()

    @pytest.fixture
    def client(self, bank):
        client_id = '001'
        bank.register_client(client_id, 'James Bond')
        return client_id

    @pytest.fixture
    def currency_converter(self):
        return CurrencyConverter()

    def test_register_client(self, bank, client):
        logger.info("Testing client registration")
        if client not in bank.client:
            logger.error("Client registration failed")
        assert client in bank.client

    def test_register_client_2(self, bank):
        logger.info("Testing duplicate client registration")
        result = bank.register_client("001", "James Bond")
        if result is not False:
            logger.error("Client registration failed")
        assert result is False

    def test_open_deposit_account(self, bank, client):
        logger.info("Testing deposit account opening")
        result = bank.open_deposit_account(client, 1000, 1)
        if result is not True:
            logger.error("Client open deposit failed")
        assert result is True

    def test_open_deposit_account_without_register_client(self, bank):
        logger.info("Testing deposit account without registration")
        result = bank.open_deposit_account("001", 1000, 1)
        if result is not False:
            logger.error("Client open deposit failed")
        assert result is False

    def test_calc_interest_rate_if_unregister_user(self, bank):
        logger.info("Testing interest calculation for unregistered user")
        result = bank.calc_interest_rate("001")
        if result != 0:
            logger.error("Client calc interest rate failed")
        assert result == 0

    def test_calc_interest_rate(self, bank, client):
        logger.info("Testing interest calculation")
        bank.open_deposit_account(client, 1000, 1)
        result = bank.calc_interest_rate(client)
        if result != 1104.71:
            logger.error(f"Client {client} calc interest rate failed")
        assert result == 1104.71
        logger.info(f"Test completed at: {time.strftime('%Y-%m-%d %H:%M:%S')}")

    def test_calc_interest_rate_if_user_without_deposit(self, bank, client):
        logger.info("Testing interest calculation without deposit")
        result = bank.calc_interest_rate(client)
        if result != 0:
            logger.error(f"Client {client} calc interest rate failed")
        assert result == 0
        logger.info(f"Test completed at: {time.strftime('%Y-%m-%d %H:%M:%S')}")

    def test_close_deposit_if_user_with_deposit(self, bank, client):
        logger.info("Testing deposit closure with deposit")
        bank.open_deposit_account(client, 1000, 1)
        result = bank.close_deposit(client)
        if result != 1104.71:
            logger.error(f"Client {client} close deposit failed")
        assert result == 1104.71
        logger.info(f"Test completed at: {time.strftime('%Y-%m-%d %H:%M:%S')}")

    def test_close_deposit_if_user_without_deposit(self, bank, client):
        logger.info("Testing deposit closure without deposit")
        result = bank.close_deposit(client)
        if result != 0:
            logger.error(f"Client {client} close deposit failed: {result}")
        assert result == 0
        logger.info(f"Test completed at: {time.strftime('%Y-%m-%d %H:%M:%S')}")

    def test_close_deposit_if_unregister_user(self, bank):
        logger.info("Testing deposit closure for unregistered user")
        result = bank.close_deposit("001")
        if result != 0:
            logger.error("Client close deposit failed")
        assert result == 0
        logger.info(f"Test completed at: {time.strftime('%Y-%m-%d %H:%M:%S')}")

    def test_convert_currency_usd_to_eur(self, currency_converter):
        logger.info("Testing currency conversion from USD to EUR")
        result = currency_converter.convert("USD", 1000, "EUR")
        if result != 961.37:
            logger.error(f"{result} convert currency failed, expected 961.37")
        assert result == 961.37
        logger.info(f"Test completed at: {time.strftime('%Y-%m-%d %H:%M:%S')}")

    def test_convert_currency_byn_to_usd(self, currency_converter):
        logger.info("Testing currency conversion from BYN to USD")
        result = currency_converter.convert("BYN", 1000, "USD")
        if result != 306.03:
            logger.error(f"{result} convert currency failed, expected 306.03")
        assert result == 306.03
        logger.info(f"Test completed at: {time.strftime('%Y-%m-%d %H:%M:%S')}")

    def test_convert_incorrect_to_currency(self, bank):
        logger.info("Testing incorrect currency from BYN to EEUR")
        with pytest.raises(ValueError) as info:
            assert bank.exchange_currency("BYN", 1000, "EEUR")
        result = str(info.value)
        if result != "Unsupported currency: EEUR":
            logger.error(f"{result} incorrect currency from BYN to EEUR")
        assert result == "Unsupported currency: EEUR"
        logger.info(f"Test completed at: {time.strftime('%Y-%m-%d %H:%M:%S')}")

    def test_convert_incorrect_from_currency(self, bank):
        logger.info("Testing incorrect currency from EEUR to BYN")
        with pytest.raises(ValueError) as info:
            assert bank.exchange_currency("EEUR", 1000, "BYN")
        result = str(info.value)
        if result != "Unsupported currency: EEUR":
            logger.error(f"{result} incorrect currency from EEUR to BYN")
        assert result == "Unsupported currency: EEUR"
        logger.info(f"Test completed at: {time.strftime('%Y-%m-%d %H:%M:%S')}")
