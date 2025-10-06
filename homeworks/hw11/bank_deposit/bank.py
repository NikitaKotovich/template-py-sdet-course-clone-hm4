from .currency import CurrencyConverter


class Bank:
    def __init__(self):
        self.client = {}
        self.deposit = {}
        self.currency_converter = CurrencyConverter()

    def register_client(self, client_id, name):
        if client_id in self.client:
            return False
        self.client[client_id] = name
        return True

    def open_deposit_account(self, client_id, start_balance, years):
        if client_id not in self.client:
            return False
        if client_id in self.deposit:
            return False
        self.deposit[client_id] = {'start_balance': start_balance,
                                   'years': years,
                                   'interest_rate': 10}
        return True

    def calc_interest_rate(self, client_id):
        if client_id not in self.deposit:
            return 0
        dep = self.deposit[client_id]
        start_balance = dep['start_balance']
        years = dep['years']
        interest_rate = dep['interest_rate']
        monthly_rate = interest_rate / 100 / 12
        months = years * 12
        final_amount = start_balance * (1 + monthly_rate) ** months
        return round(final_amount, 2)

    def close_deposit(self, client_id):
        if client_id not in self.deposit:
            return 0
        final_amount = self.calc_interest_rate(client_id)
        del self.deposit[client_id]
        return final_amount

    def exchange_currency(self, from_curr, amount, to_curr):
        return self.currency_converter.convert(from_curr, amount, to_curr)
