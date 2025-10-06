class CurrencyConverter:

    def __init__(self, exchange_rates=None):
            self.exchange_rates = {'BYN': 1.0, 'USD': 3.2677, 'EUR': 3.399}

    def convert(self, from_curr, amount, to_curr):
        if from_curr not in self.exchange_rates:
            raise ValueError(f"Unsupported currency: {from_curr}")
        if to_curr not in self.exchange_rates:
            raise ValueError(f"Unsupported currency: {to_curr}")
        in_byn_curr = amount * self.exchange_rates[from_curr]
        from_byn_curr = in_byn_curr / self.exchange_rates[to_curr]
        return round(from_byn_curr, 2)
