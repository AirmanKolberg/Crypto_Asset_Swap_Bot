import cryptocompare
from datetime import datetime


# Gets the current time in string format: 'HH:MM:SS'
def get_current_time():

    return datetime.now().strftime('%H:%M:%S')


def get_crypto_price(coin, currency):
    specific_value = cryptocompare.get_price(coin=coin,
                                             currency=currency,
                                             full=True)['RAW'][coin][currency]['PRICE']
    return specific_value


if __name__ == '__main__':
    pass
